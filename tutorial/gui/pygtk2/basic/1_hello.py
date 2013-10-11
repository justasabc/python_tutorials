#!/usr/bin/python

# ZetCode PyGTK tutorial 
#
# This is a trivial PyGTK example
#
# author: jan bodnar
# website: zetcode.com 
# last edited: February 2009
import pygtk 
pygtk.require('2.0')
import gtk

class PyApp(gtk.Window):
    	def __init__(self):
        	super(PyApp, self).__init__()
        
        	self.set_size_request(250, 150)
        	self.set_position(gtk.WIN_POS_CENTER)
        	self.connect("destroy", gtk.main_quit)
		# The destroy signal is called when we click on the close button in the titlebar or press Alt + F4
		button = gtk.Button("Click Here")
		button.connect('clicked',self.print_hello_world,'XXX')
		self.add(button)
        	self.show_all()
	
	def print_hello_world(self,widget,data):
		print(data,"hello world")

def main():
	app = PyApp()
	gtk.main()

if __name__ =="__main__":
	main()
