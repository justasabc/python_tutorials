#!/usr/bin/env python

import gtk

class Alignment:
    def __init__(self):
        window = gtk.Window()
        label = gtk.Label("Alignment")
        alignment = gtk.Alignment(0.5, 0.5, 0.5, 0.5)
        
        window.connect("destroy", lambda w: gtk.main_quit())
        
        window.add(alignment)
        alignment.add(label)
        window.show_all()

Alignment()
gtk.main()
