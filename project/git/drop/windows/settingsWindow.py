#!/usr/bin/env python
import pygtk
pygtk.require('2.0')
import gtk
#import sys

class SettingsWindow:
	def __init__(self, app):
		self.app = app
		self.app_icon = "./windows/resource/icon/dewdrop-128-black.png"
		self.glade = "./windows/data/ui/settingsWindow.glade"

		self.builder = gtk.Builder()
		self.builder.add_from_file(self.glade)
		self.builder.connect_signals(self)

		# access app
		dropzone = self.app._cfg.get('dropzone')

		# if dropzone == null, then name = btnHide
		name = "btnHide"
		if dropzone == "custom":
			name = "btnCustom"
		elif dropzone == "tl":
			name = "btnTopLeft"
		elif dropzone == "tm":
			name = "btnTopMiddle"
		elif dropzone == "tr":
			name = "btnTopRight"
		elif dropzone == "ml":
			name = "btnMiddleLeft"
		elif dropzone == "mr":
			name = "btnMiddleRight"
		elif dropzone == "bl":
			name = "btnBottomLeft"
		elif dropzone == "bm":
			name = "btnBottomMiddle"
		elif dropzone == "br":
			name = "btnBottomRight"

		self.builder.get_object(name).set_active(True)

		self.win = self.builder.get_object('settingsWindow')
		self.win.set_focus(self.builder.get_object(name))
		self.win.set_modal(False)
		self.win.set_icon_from_file(self.app_icon)

		# connect events
		self.win.connect('destroy',self.close)
		self.builder.get_object('btnSave').connect('clicked',self.save)
		self.win.show_all()

	def show(self):
		gtk.main()

	def close(self,widget,data=None):
		print('settingsWindow is going to close...')
		gtk.main_quit()

	def test_group(self):
		hide_button = self.builder.get_object('btnHide')
		g = hide_button.get_group() # 10 buttons in group list 
		print (len(g)) # 10 buttons
		for btn in g:
			name = gtk.Buildable.get_name(btn)
			print(btn.get_active(),name)
		print('-'*30)

	def save(self, widget, data=None):
		#self.test_group()
		hide_button = self.builder.get_object('btnHide')
		active = [btn for btn in hide_button.get_group() if btn.get_active()][0]
		name = gtk.Buildable.get_name(active)
		print(name) # button_name

		dropzone = "hide"

		if name == 'btnCustom':
			dropzone = "custom"

			# try to get the current position
			x = self.app._cfg.get('x')
			y = self.app._cfg.get('y')
			if hasattr(self.app.dew, 'drop'):
				x,y = self.app.dew.drop.dialog.get_position()
			else:
				if x is None:
					x = 0
				if y is None:
					y = 0
			self.app._cfg.set('x', x)
			self.app._cfg.set('y', y)
		else:
			self.app._cfg.set('x', None)
			self.app._cfg.set('y', None)
			if name == 'btnTopLeft':
				dropzone = "tl"
			elif name == 'btnTopMiddle':
				dropzone = "tm"
			elif name == 'btnTopRight':
				dropzone = "tr"
			elif name == 'btnMiddleLeft':
				dropzone = "ml"
			elif name == 'btnMiddleRight':
				dropzone = "mr"
			elif name == 'btnBottomLeft':
				dropzone = "bl"
			elif name == 'btnBottomMiddle':
				dropzone = "bm"
			elif name == 'btnBottomRight':
				dropzone = "br"

		self.app._cfg.set('dropzone', dropzone)
		self.app._cfg.save()
		# force settingsWindow to destroy
		self.win.destroy()
		#refresh dropzone
		#self.app.dew.show_hide_drop()
		
