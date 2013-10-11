#!/usr/bin/env python

import gtk

class Notebook:
    def __init__(self):
        window = gtk.Window()
        window.set_default_size(200, 200)
        
        notebook = gtk.Notebook()
        for page in range(0, 3):
            label = gtk.Label('label'+str(page))
            notebook.append_page(label)

        window.connect("destroy", lambda w: gtk.main_quit())
        
        window.add(notebook)
        window.show_all()

Notebook()
gtk.main()
