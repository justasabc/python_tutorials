# -*- coding:utf-8 -*-
__author__ = "kezunlin"
import re
import requests
import os
import sys
import time

url_page_pre = "http://desk.zol.com.cn/pc/"
url_down_pre = "http://desk.zol.com.cn"
regex_group_url = r"(<li class=\"photo-list-padding\"><a class=\"pic\" href=)\"(/bizhi/\d+_\d+_\d+.html)"	
regex_group_name = r"(<h3>.*>)(.+)(</a>.*>)" 
regex_group_next_page_url = r"(id=\"pageNext\".*href=\")(/bizhi/\d+_\d+_\d+.html)\"\s(title=\")"
regex_image_html_url = r"(id=\"1920x1080\"\s.*href=\")(/showpic/\d+x\d+_\d+_\d+.html)(\">1920x1080)"
regex_image_url_name = r"(http://.*/)(\d+.png|\d+.jpg|\d+.jpeg)"
local_dir = ".\\images\\"


class ImageFetcher:
	def __init__(self):
		self.group_url_list = []
		self.group_name = ""
		self.group_next_page_url = ""
		self.image_html_url = ""
		self.image_name = ""
		self.image_url = ""
	
	def Fetch(self,page_re_string):
		self.get_group_url_list(page_re_string)
		self.process_group_url_list(self.group_url_list)

	# http://desk.zol.com.cn/pc/2.html
	# ---> 15 groups url list
	# "http://desk.zol.com.cn/bizhi/2370_30231_2.html
	def get_group_url_list(self,page_re_string):
		group_url_list_temp = re.findall(regex_group_url,page_re_string) # tuple
		for match in group_url_list_temp:
			self.group_url_list.append(url_down_pre + match[1])
		print self.group_url_list
	
	# process all groups
	def process_group_url_list(self,group_url_list):
		for g in group_url_list:
			self.process_group(g)
	
	# process group 
	# get group name and process all group pages
	def process_group(self,g):
		print "Group URL:",g
		try:
			rgroup = requests.get(g)
			if rgroup.status_code ==200:
				# get group name
				self.get_group_name(rgroup.text)
				# get all group pages url
				self.group_next_page_url = g
				while True:
					rgroup_page = requests.get(self.group_next_page_url)
					self.process_group_page(rgroup_page.text)
					if self.group_next_page_url == g or self.group_next_page_url == "":
						break
			print "Group %s finished..." % self.group_name
			print "--------------Group-------------"
		except:
			print "process_group????????????????????????????????"
	
	# get group name for once
	def get_group_name(self,group_re_string):
		match_group_name = re.search(regex_group_name,group_re_string)
		if match_group_name:
			self.group_name = match_group_name.group(2)
		else:
			self.group_name = ""
		print "Group Name:",self.group_name
	
	# process one group page
	def process_group_page(self,group_page_re_string):
		#process current page
		print "Current Page URL:",self.group_next_page_url
		self.get_image_html_url(self.group_next_page_url)
		self.get_image_url_name(self.image_html_url)
		if self.image_url !="" and self.image_name != "":
			self.down_image(self.image_url,self.image_name,local_dir)
	
		# get next page url
		match_group_next_page_url = re.search(regex_group_next_page_url,group_page_re_string)
		if match_group_next_page_url:
			self.group_next_page_url = url_down_pre + match_group_next_page_url.group(2)
		else:
			self.group_next_page_url = ""
	
	
	def get_image_html_url(self,group_page_url):
		try:
			rgroup_page = requests.get(group_page_url)
			if rgroup_page.status_code == 200:
				match_image_html_url = re.search(regex_image_html_url,rgroup_page.text)
				if match_image_html_url:
					self.image_html_url = url_down_pre + match_image_html_url.group(2)
				else:
					self.image_html_url = ""
			print "Image html URL: ",self.image_html_url
		except:
			print "get_image_html_url?????????????????????????"
	
	def get_image_url_name(self,image_html_url):
		try:
			rimage_html = requests.get(image_html_url)
			if rimage_html.status_code == 200:
				match_image_url_name = re.search(regex_image_url_name,rimage_html.text)
				if match_image_url_name:
					self.image_url = match_image_url_name.group()
					self.image_name = match_image_url_name.group(2)
				else:
					self.image_url = ""
					self.image_name = ""
			print "Image URL: ", self.image_url
			print "Image Name: ", self.image_name
		except:
			print "get_image_url_name????????????????????????"

	
	def ensure_dir(self,d):
		if not os.path.exists(d):
			os.makedirs(d)
	
	def down_image(self,image_url,image_name,local_dir):
		self.ensure_dir(local_dir)
		self.ensure_dir(local_dir+self.group_name)
		image_path = local_dir + self.group_name +"\\"+ self.image_name
		if os.path.exists(image_path): 
	    		print "Image ",image_path," already exists...."
		else:
			print "Reading Image %s from server..." % image_name
	    		r = requests.get(image_url)
			if r.status_code == 200:
				print "Saving image to %s..." % image_path
	    			with open(image_path, "wb") as savefile:
	        			savefile.write(r.content)
		print "------------------------------------------------"

if __name__ == "__main__":
	t1 = time.clock()
	for i in range(30,500):
		page_url = url_page_pre + str(i) + ".html"
		print "Page ID: %d *************************************************", i
		print "Start page url:",page_url
		try:
			rpage = requests.get(page_url)
			if rpage.status_code == 200:
				fetcher = ImageFetcher()
				fetcher.Fetch(rpage.text)	
				print "Time used: %5.4f  ms." % (time.clock()-t1)/60.0
		except:
			print "request page?????????????????????"
