#!/usr/bin/env python
import pygtk
pygtk.require('2.0')
import gtk
import gobject
gobject.threads_init()

import sys

from windows.about import About
from windows.settingsWindow import SettingsWindow
from windows.dropWindow import DropWindow
from config import Config
import notify

import pkg_resources
import time
import appindicator
import base64
import webbrowser
from threading import Thread
import threading
import thread

class DewDrop:
	def __init__(self, app):
		self._app = app
		self._app.dew = self # REQUIRE

		#self.app_icon = "./windows/resource/icon/dewdrop_32.png"
		# add statusIcon for app
		if not hasattr(self._app, 'statusIcon'):
			self._app.statusIcon = appindicator.Indicator('Dewdrop', "indicator-messages", appindicator.CATEGORY_APPLICATION_STATUS)

		self._app.statusIcon.set_status(appindicator.STATUS_ACTIVE)
        	self._app.statusIcon.set_attention_icon ("indicator-messages-new")
        	self._app.statusIcon.set_icon("distributor-logo")

		self.init_menu()
		self.show_hide_drop()

	def init_menu(self):
		menu = gtk.Menu()

		takescreenshot = gtk.MenuItem("Capture Screenshot...")
		uploadfile = gtk.MenuItem("Upload a file...")
		createnote = gtk.MenuItem("Create note...")
		settings = gtk.MenuItem("Settings...")
		separator1 = gtk.SeparatorMenuItem()
		recent = gtk.MenuItem("Recent Drops")
		separator2 = gtk.SeparatorMenuItem()
		about = gtk.MenuItem("About")
		logout = gtk.MenuItem("Logout")
		quit = gtk.MenuItem("Quit DewDrop")

		#takescreenshot.connect("activate", self.take_screenshot)
		#createnote.connect("activate", self.create_note)
		#uploadfile.connect("activate", self.upload_file)
		settings.connect("activate", self.show_settings)
		#recent.connect("activate", self.show_recent)
		about.connect("activate", self.about)
		logout.connect("activate", self.logout)
		quit.connect("activate", self.quit)

		menu.append(takescreenshot)
		menu.append(uploadfile)
		menu.append(createnote)
		menu.append(settings)
		menu.append(separator1)
		menu.append(recent)
		menu.append(separator2)
		menu.append(about)
		menu.append(logout)
		menu.append(quit)
	
		menu.show_all()

		self._app.statusIcon.set_menu(menu)

	def show_hide_drop(self, widget=None):
		#return 
		if hasattr(self, 'drop'):
			self.drop.hide()
			delattr(self, 'drop')

		dropzone = self._app._cfg.get('dropzone')
		if dropzone is not None and dropzone != 'hide':
			self.drop = DropWindow(self._app)
			self.drop.show()

	def show(self):
		# gtk.main   --- gtk.main_quit
		gtk.main()
		
	def close(self):
		# 1 statusIcon
		self._app.statusIcon.set_status(appindicator.STATUS_PASSIVE)
		print('appindicator closed')
		# 2 DropWindow
		if hasattr(self, 'drop'):
			self.drop.hide()
		# 3 main_quit
		gtk.main_quit()
		print('dewdrop exited')
		# 4 exit 
		sys.exit(1)

	def show_settings(self, widget):
		settings = SettingsWindow(self._app)
		settings.show()

	def about(self, widget):
		about = About()
		about.show()

	def logout(self, widget):
		self._app.logout()

	def quit(self, widget):
		self.logout(None)

