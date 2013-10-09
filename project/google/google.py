#!/usr/bin/python

from bs4 import BeautifulSoup
import requests
from pprint import pprint
import os
import sys
try:
	import json
except ImportError:
	import simplejson as json

__author__ = "justasabc <zunlin1234@gmail.com>"
__version__ = "0.1"

"""
Represents a standard google search result
"""
class GoogleResult:
	def __init__(self):
		self.name = None
		self.link = None
		self.description = None
		self.thumb = None
		self.cached = None
		self.page = None
		self.index = None

	def output(self):
		print(self.name)
		print(self.link)
		print(self.description)
        
"""
Defines the public static api methods
"""
class Google:
	DEBUG_MODE = True

	@staticmethod
	def search(query, pages = 1):
		results = []
		for i in range(pages):
			url = get_search_url(query, i)
	            	print(url)
			r = requests.get(url)
	            	html = r.content
			#print(html)
                	soup = BeautifulSoup(html)
                	lis = soup.find_all("li", attrs = { "class" : "g" })
	                j = 0
			li = lis[0]
			print(len(lis))
			#if li:
			for li in lis:
	       	             	res = GoogleResult()
	                    	res.page = i
	                    	res.index = j
	                    	a = li.find("a")
	                    	res.name = a.text.strip()
	                    	res.link = a["href"].strip()
				sdiv = li.find("div", attrs = { "class" : "s" })
	                    	if sdiv:
	                        	res.description = sdiv.text.strip()
	                    	results.append(res)
	                    	j = j + 1
	        return results
    
def normalize_query(query):
	return query.strip().replace(":", "%3A").replace("+", "%2B").replace("&", "%26").replace(" ", "+")
 
search_url_format = "http://www.google.com.hk/search?q={0}&start={1}&num={2}" 
def get_search_url(query, page = 0, per_page = 10):
	query = normalize_query(query)
	return search_url_format.format(query,page*per_page,per_page)

def test():
	results = Google.search("github")
	if results is None or len(results) == 0: 
		print "ERROR: No Search Results!"
	else: 
		print "PASSED: {0} Search Results".format(len(results))
	for r in results:
		r.output()
		print('*'*30)
        
def main():
	test()
        
if __name__ == "__main__":
	main()
    
