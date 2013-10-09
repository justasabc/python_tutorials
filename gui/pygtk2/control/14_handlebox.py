#!/usr/bin/env python

import gtk

class HandleBox:

	def __init__(self):
	        window = gtk.Window()
	        window.set_default_size(200, -1)
	        
	        handlebox = gtk.HandleBox()
		handlebox.set_handle_position(gtk.POS_LEFT)
	        #handlebox.set_snap_edge(gtk.POS_LEFT)
	        handlebox.set_snap_edge(gtk.POS_TOP)
		handlebox.connect("child-attached",self.attached)
		handlebox.connect("child-detached",self.detached)
	        
	        toolbar = gtk.Toolbar()
	        toolbar.set_size_request(200, -1)
	        
	        toolbutton1 = gtk.ToolButton(gtk.STOCK_NEW)
	        toolbutton2 = gtk.ToolButton(gtk.STOCK_OPEN)
	        toolbutton3 = gtk.ToolButton(gtk.STOCK_SAVE)
	        toolbar.insert(toolbutton1, 0)
	        toolbar.insert(toolbutton2, 1)
	        toolbar.insert(toolbutton3, 2)
	        
	        window.connect("destroy", lambda w: gtk.main_quit())
	
	        window.add(handlebox)
	        handlebox.add(toolbar)
	        window.show_all()
	
	def attached(self,widget,data):
		print "attached"

	def detached(self,widget,data):
		print "detached"

HandleBox()
gtk.main()


