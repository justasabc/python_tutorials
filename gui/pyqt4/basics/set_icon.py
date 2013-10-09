#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui

class Window(QtGui.QWidget):
	"""
	A simple window wigdet
	"""
	def __init__(self):
		super(Window,self).__init__()
		self.initUI()
	
	def initUI(self):
		self.setGeometry(300,300,250,150)
		self.setWindowTitle('hello world')
		self.setWindowIcon(QtGui.QIcon('apple.png'))
		self.show()

def main():
	app = QtGui.QApplication(sys.argv)
	win = Window()
	# enter the mainloop of the application
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()
