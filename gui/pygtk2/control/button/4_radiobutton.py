#!/usr/bin/env python

import gtk

class RadioButton:
    def __init__(self):
        window = gtk.Window()
        vbox = gtk.VBox()
        
        radiobutton1 = gtk.RadioButton(None, "RadioButton 1")
        radiobutton2 = gtk.RadioButton(radiobutton1, "RadioButton 2")
        radiobutton3 = gtk.RadioButton(radiobutton1, "RadioButton 3")
            
        window.add(vbox)
        vbox.pack_start(radiobutton1)
        vbox.pack_start(radiobutton2)
        vbox.pack_start(radiobutton3)
            
        window.connect("destroy", lambda w: gtk.main_quit())
            
        window.show_all()

RadioButton()
gtk.main()
