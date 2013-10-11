#!/usr/bin/env python
"""
pynotify is a module in gtk
"""
import pynotify # gtk-2.0/pynotify
def update(link):
	# init pynotify with anything
	if not pynotify.init ("summary-body"):
		return False

	app_icon = "./windows/resource/icon/dewdrop_32.png"
	n = pynotify.Notification ("DewDrop", "Update Available: {0}".format(link), app_icon)
	n.show()
	return True

if __name__=="__main__":
	update('http://www.baidu.com')
