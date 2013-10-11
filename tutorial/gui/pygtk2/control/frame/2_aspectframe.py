#!/usr/bin/env python

import gtk

class AspectFrame:
    def __init__(self):
        window = gtk.Window()
        window.set_default_size(200, 200)
        
        frame = gtk.AspectFrame("Frame", 0.5, 0.5, 0.5, False)
        image = gtk.Image()
        image.set_from_file("android.jpg")
        frame.add(image)

        window.connect("destroy", lambda w: gtk.main_quit())
        
        window.add(frame)
        window.show_all()

AspectFrame()
gtk.main()
