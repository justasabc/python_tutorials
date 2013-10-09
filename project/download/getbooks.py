#/usr/bin/python
# book fetcher   utf-8  gbk gb2312
__author__ = "kezunlin"
__version__ = "0.1"
import re
import requests
from bs4 import BeautifulSoup
import os
import sys
import time

detail_url_pre = "http://book.zi5.me/books/detail/"
down_url_pre = "http://book.zi5.me"
regex_file_url = r"/books/down/MOBI/(.*).mobi"
regex_book_name = r'<title>(.*);(.*);(.*)</title>'
local_dir = ".\\mobibooks\\"

# global variable need to modify
down_url = ""
book_name = ""

def regex_parse(re_string): 
	global down_url,book_name
	match_url = re.search(regex_file_url,re_string) 
	if match_url: 
		down_url = down_url_pre + match_url.group() 
		print "DownURL:",down_url 

		match_book_name = re.search(regex_book_name, re_string)
        	if match_book_name:
              		book_name = match_book_name.group(3).strip()
       		else:
			book_name = "error"
			print "...no book name..."
	else:
		down_url = "error"			
		print "...no down url..."

def ensure_dir(d):
	if not os.path.exists(d):
		os.makedirs(d)

def down_book(down_url,book_name,local_dir):
	ensure_dir(local_dir)
	book_path = local_dir + book_name + ".mobi"
	if os.path.exists(book_path): 
    		print "Book ",book_path," already exists...."
	else:
		print "Reading book %s from server..." % book_name
		try:
    			r = requests.get(down_url)
			if r.status_code == 200:
				print "Saving book to %s..." % book_path
    				with open(book_path, "wb") as savefile:
        				savefile.write(r.content)
		except:
			print "request book?????????????????????????"

#http://book.zi5.me/books/detail/1250
# --->books/down/MOBI/2669a8229c1f502a5aa454c777b4d7f2/2855.mobi
# ---> <title>≈º∑¢ø’»± <title>
#http://book.zi5.me/books/down/MOBI/2669a8229c1f502a5aa454c777b4d7f2/2855.mobi
if __name__ == "__main__":
	t1 = time.clock()
	for i in range(866, 1500):
        	url = detail_url_pre + str(i)
		print "Page:", url    
		try:
	        	r = requests.get(url)
	        	if r.status_code == 200:
				# get down_url and book_name
				regex_parse(r.text) 
				if down_url != "error" and book_name != "error":
					book_name = format(i,"04d") + '_'+ book_name
					down_book(down_url,book_name,local_dir)
				print "Time used: %5.4f minutes." % ((time.clock()-t1)/60.0)
				print str(i)+"----------------------------------------------------"
	        	else:
				print "...404..."
		except:
			print "request url??????????????????????????"

	print ("Downing Finish")
