#!/usr/bin/env python

from config import Config
from version import new_version
from windows.loginWindow import LoginWindow
#from dapi import DAPI
from dewdrop import DewDrop

class App:
	def __init__(self):
		# check if there is a new version
		new_version()

		self._cfg = Config()
		if self._cfg.get('email') == None:
			# Time to login
			self.show_login()
		else:
			# Test the credentials
			if self.test_credentials(self._cfg.get('email'), self._cfg.get('passhash')) == True:
				self.login()
			else:
				self.relogin()

	def relogin(self):
		self._cfg.set('email', None)
		self._cfg.set('passhash', None)
		self._cfg.save()

		self.show_login()

	def show_login(self):
		login = LoginWindow(self)
		login.show()

	def test_credentials(self, email, passhash):
		return True

	def login(self):
		print('login ...')
		self.dew = DewDrop(self)
		self.dew.show()

	def logout(self):
		print('logout ...')
		self.dew.close()
