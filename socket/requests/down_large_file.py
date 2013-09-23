# -*- coding:utf-8 -*-
__author__ = "kezunlin"
import re
import requests
import os
import sys
import time

class LargeFileDownloader:
	def __init__(self):
		self.local_dir = ".\\largefile\\"
		self.url = "http://releases.ubuntu.com/precise/ubuntu-12.04.2-server-i386.iso"
		self.url2 = "http://the.earth.li/~sgtatham/putty/latest/x86/putty.exe"
		self.file_name = self.url.split('/')[-1]

	def Run(self):
		print "url: ", self.url
		print "filename: ", self.file_name
		print "Begin downloading ..."
		self.Download(self.url,self.file_name,self.local_dir)
		print "Downloading Finished."

	def ensure_dir(self,d):
		if not os.path.exists(d):
			os.makedirs(d)

	def Download(self,url,filename,localdir):
		try:
			print "Requesting url..."
			r = requests.get(url, stream = True)
			if r.status_code == 200:
				self.ensure_dir(localdir)
				filepath = localdir + filename
				if os.path.exists(filepath):
					print "File %s already exists." % filename
				else:
					print "Saving file to %s ..." % filepath
					with open(filepath,'wb') as f:
						f.write(r.content)
						'''
						for chunck in r.iter_content(1024):
							if chunck:
								f.write(chunk)
								f.flush()
						 '''
			else:
				print "server error."
		except:
			print "download except???"


if __name__ == "__main__":
	t1 = time.clock()
	d = LargeFileDownloader()
	d.Run()
	print "Time used: %5.4f minutes." % ((time.clock()-t1)/60.0)

