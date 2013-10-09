#!/usr/bin/env python

import gtk

class LinkButton:
    def __init__(self):
        window = gtk.Window()
        linkbutton = gtk.LinkButton("http://www.pygtk.org/", "LinkButton")

        window.connect("destroy", lambda w: gtk.main_quit())
            
        window.add(linkbutton)
        window.show_all()

LinkButton()
gtk.main()
