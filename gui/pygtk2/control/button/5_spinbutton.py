#!/usr/bin/env python

import gtk

class SpinButton:
    def __init__(self):
        window = gtk.Window()
        vbox = gtk.VBox(False, 5)
        
        adjustment = gtk.Adjustment(10, 0, 100, 1, 10, 0)
        self.spinbutton = gtk.SpinButton(adjustment)
	# set_numeric only allow number to be inputed
	self.spinbutton.set_numeric(True)
	# The value of "digits" determines the number of decimal places (up to 20 digits) to be displayed by the spinbutton
	# allow 4 digits after .
	# 10.0000
	self.spinbutton.set_digits(4)
        check_snapticks = gtk.CheckButton("Snap to Ticks")
        
        window.connect("destroy", lambda w: gtk.main_quit())
        check_snapticks.connect("toggled", self.snapticks)
        
        window.add(vbox)
        vbox.pack_start(self.spinbutton, False, False, 0)
        vbox.pack_start(check_snapticks, False, False, 0)
        
        window.show_all()
    
    def snapticks(self, widget):
	# snap_to_ticks 
	# if True invalid values should be corrected.
        self.spinbutton.set_snap_to_ticks(widget.get_active())
        
SpinButton()
gtk.main()
