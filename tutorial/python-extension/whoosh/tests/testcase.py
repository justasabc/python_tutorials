#!/usr/bin/python
"""
testcase.py

Created by justasabc on 2013-10-11
Copyright (c) 2013 justasabc. All rights reserved.
"""
import unittest
import sys
import os

#from whoosh.searching import Results,Hit
from demo import *

class BaseTestCase(unittest.TestCase):

	def setUp(self):
		pass

	def tearDown(self):
		pass
	
	def test_search_files(self):
		index_dir = 'indexdir'
		results = search_files(index_dir,'first')
		l = len(results)
		self.assertTrue(l == 2,'hit {0} results'.format(l))

class BaseTestCase2(unittest.TestCase):

	def setUp(self):
		pass

	def tearDown(self):
		pass
	
def run(testCase):
	suite = unittest.TestLoader().loadTestsFromTestCase(testCase)
	runner = unittest.TextTestRunner(verbosity=2)
	runner.run(suite)

def run_all():
	run(BaseTestCase)
	run(BaseTestCase2)
	pass

if __name__ == "__main__":
	run_all()
