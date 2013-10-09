#!/usr/bin/python
import pygtk 
pygtk.require('2.0')
import gtk
import sys

class PyApp(gtk.Window):
    def __init__(self):
        super(PyApp, self).__init__()
        
	self.set_title('icon')
        self.set_size_request(250, 150)
        self.set_position(gtk.WIN_POS_CENTER)
	try:
		self.set_icon_from_file("apple.png")
	except Exception,e:
		print(e)
		#sys.exit(1)

        self.connect("destroy", gtk.main_quit)
	# The destroy signal is called when we click on the close button in the titlebar or press Alt + F4
        self.show()

def main():
	app = PyApp()
	gtk.main()

if __name__ =="__main__":
	main()
