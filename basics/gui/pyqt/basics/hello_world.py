#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui

def main():
	app = QtGui.QApplication(sys.argv)
	# A widget with no parent is called a window. 
	win = QtGui.QWidget()
	win.resize(250,150)
	win.move(300,300)
	win.setWindowTitle('hello world')
	win.show()
	# enter the mainloop of the application
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()
