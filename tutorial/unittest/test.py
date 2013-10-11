#!/usr/bin/python
"""
testcase.py

Created by justasabc on 2013-10-11
Copyright (c) 2013 justasabc. All rights reserved.
"""
import unittest
import sys
import os

class BaseTestCase(unittest.TestCase):

	def setUp(self):
		pass

	def tearDown(self):
		pass
	
	def test_1(self):
		rest = True
		self.assertTrue(rest==True,'bad test')
		pass

class BaseTestCase2(unittest.TestCase):

	def setUp(self):
		pass

	def tearDown(self):
		pass
	
	def test_2(self):
		rest = False
		self.assertTrue(rest==True,'bad test')
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
