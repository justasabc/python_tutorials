#!/usr/bin/env python

import gtk

class PyApp(gtk.Window):
    def __init__(self):
	super(PyApp,self).__init__()
	self.set_title('vbox')
        self.set_default_size(200, 100)
        vbox = gtk.VBox(False, 5)
        button1 = gtk.Button("Button 1")
        button2 = gtk.Button("Button 2")
        button3 = gtk.Button("Button 3")

        vbox.pack_start(button1,False,False,0)
        vbox.pack_start(button2,False,False,0)
        vbox.pack_start(button3,False,False,0)
        
        self.add(vbox)
        
        self.connect("destroy", lambda w: gtk.main_quit())
        self.show_all()

PyApp()
gtk.main()
