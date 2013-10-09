#!/usr/bin/env python

import gtk, gobject

class ProgressBar:
    def __init__(self):
        window = gtk.Window()
        window.set_default_size(200, -1)
        
        vbox = gtk.VBox(False, 5)

        self.progressbar = gtk.ProgressBar()
        self.check_text = gtk.CheckButton("Display text")
        
        vbox.pack_start(self.progressbar)
        vbox.pack_start(self.check_text)
        
        window.connect("destroy", lambda w: gtk.main_quit())
        self.check_text.connect("toggled", self.text)
        
        window.add(vbox)
        window.show_all()
        
        self.run()
    
    def run(self):
        gobject.timeout_add(500, self.update)
    
    def update(self):       
        if self.progressbar.get_fraction() >= 1.0:
            value = 0.0
        else:
            value = self.progressbar.get_fraction() + 0.1
            
        self.progressbar.set_fraction(value)
        
        if self.check_text.get_active():
            percent = value * 100
            percent = str(int(percent))
            self.progressbar.set_text(percent + "%")
        
        return True
    
    def text(self, widget):
        if self.check_text.get_active() == False:
            self.progressbar.set_text("")

ProgressBar()
gtk.main()
