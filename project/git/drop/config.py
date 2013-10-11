#!/usr/bin/env python

import simplejson as json
import os
import sys

class Config:
	def __init__(self):
		# Check if file exists
		path = os.path.expanduser("~/.dewdrop/")
		# /home/ke/.dewdrop/
		if not os.path.exists(path):
			# Create Path
			os.makedirs(path)

		self.path = "{0}{1}".format(path,"config")
		# /home/ke/.dewdrop/config
		self.data = {}
		if os.path.exists(self.path):
			print('loading config from {0}'.format(self.path))
			self.load()

	def load(self):
		f = file(self.path, 'r')
		data = f.read()
		f.close()
		self.data = json.loads(data)

	def set(self, name, val):
		self.data[name] = val;

	def get(self, name):
		return self.data.get(name,None)

	def save(self):
		f = file(self.path, 'w')
		f.write(json.dumps(self.data))
		f.close()

def main():
	con = Config()
	con.set('email','test@gmail.com')
	con.set('passhash','123456')
	con.save()

	print con.get('email')
	print con.get('passhash')
	print con.get('xxx')


if __name__ == "__main__":
	main()
