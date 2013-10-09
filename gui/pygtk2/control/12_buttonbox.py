#!/usr/bin/env python

import gtk

class ButtonBox:
    def __init__(self):
        window = gtk.Window()
        window.set_default_size(300, -1)
        buttonbox = gtk.HButtonBox()
        
        button1 = gtk.Button("Button 1")
        button2 = gtk.Button("Button 2")
        button3 = gtk.Button("Button 3")
        button_help = gtk.Button("Help")
        button_about = gtk.Button("About")
        
        window.add(buttonbox)
        buttonbox.add(button1)
        buttonbox.add(button2)
        buttonbox.add(button3)
	buttonbox.add(button_help)	
	buttonbox.add(button_about)	

	# set_child_secondary
	buttonbox.set_child_secondary(button_help,True)
	buttonbox.set_child_secondary(button_about,True)

        window.connect("destroy", lambda w: gtk.main_quit())
        
        window.show_all()

ButtonBox()
gtk.main()
