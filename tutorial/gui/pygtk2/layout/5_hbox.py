#!/usr/bin/env python

import gtk

class PyApp(gtk.Window):
    def __init__(self):
	super(PyApp,self).__init__()
	self.set_title('HBOX')
        self.set_default_size(200, 100)
        hbox = gtk.HBox(False, 5)
        button1 = gtk.Button("Button 1")
        button2 = gtk.Button("Button 2")
        button3 = gtk.Button("Button 3")

        hbox.pack_start(button1,False,False,0)
        hbox.pack_start(button2,False,False,0)
        hbox.pack_start(button3,False,False,0)
        
        self.add(hbox)
        
        self.connect("destroy", lambda w: gtk.main_quit())
        self.show_all()

PyApp()
gtk.main()
