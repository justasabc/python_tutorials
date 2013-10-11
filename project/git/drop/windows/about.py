#!/usr/bin/env python

import pygtk
pygtk.require('2.0')

import gtk
import pkg_resources
# parent module
import version

class About:
	def __init__(self):
		self.about = gtk.AboutDialog()
		self.about.set_program_name("dewdrop")
		self.about.set_version(version.get_version())
		self.about.set_authors(['Steve Gricci', 'Adam Galloway', 'Uri Herrera'])
		self.about.set_copyright("(c) Steve Gricci")
		self.about.set_comments("dewdrop is an Open Source Droplr client for Linux\n\nThe source code is available: http://github.com/sgricci/dewdrop")
		self.about.set_website("http://dewdrop.deepcode.net")
		self.about.set_logo(gtk.gdk.pixbuf_new_from_file("./windows/resource/icon/dewdrop-128-black.png"))

	def show(self):
		self.about.run()
		self.about.destroy()
