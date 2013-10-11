#!/usr/bin/env python

import gtk

class ToggleButton:
    def __init__(self):
        window = gtk.Window()
        vbox = gtk.VBox()
        
        togglebutton1 = gtk.ToggleButton("ToggleButton 1")
        togglebutton2 = gtk.ToggleButton("ToggleButton 2")
        togglebutton2.set_active(True)
            
        window.add(vbox)
        vbox.add(togglebutton1)
        vbox.add(togglebutton2)
            
        window.connect("destroy", lambda w: gtk.main_quit())
        togglebutton1.connect("toggled", self.toggled, "1")
        togglebutton2.connect("toggled", self.toggled, "2")
            
        window.show_all()
    
    def toggled(self, widget, button):
        print "ToggleButton", button, "was turned %s" % ("off", "on")[widget.get_active()]

ToggleButton()
gtk.main()
