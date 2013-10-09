#!/usr/bin/env python

import gtk

class Expander:
    def __init__(self):
        window = gtk.Window()
        window.set_default_size(200, -1)
       	""" 
        expander = gtk.Expander(None)
        label = gtk.Label("Expander")
        expander.set_label_widget(label)
	"""
        expander = gtk.Expander("Expander")

        window.connect("destroy", lambda w: gtk.main_quit())
        expander.connect("notify::expanded", self.expanded)
        
        window.add(expander)
        window.show_all()

    def expanded(self, expander, parameter):
        if expander.get_expanded():
            label = gtk.Label("Label")
            label.set_size_request(200, 100)
            expander.add(label)
            label.show()
        else:
            expander.remove(expander.child)
            expander.get_parent().resize(200, 1)
        
        print "The Expander is currently %s" % ("closed", "open")[expander.get_expanded()]


# (0,1)[True] --->1
# (0,1)[False] --->0
Expander()
gtk.main()
