#!/usr/bin/env python

import gtk

class Frame:
    def __init__(self):
        window = gtk.Window()
        window.set_default_size(200, 200)
        frame = gtk.Frame("Frame")

        window.connect("destroy", lambda w: gtk.main_quit())
        
        window.add(frame)
        window.show_all()

Frame()
gtk.main()
