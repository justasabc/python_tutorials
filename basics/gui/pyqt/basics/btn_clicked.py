#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui,QtCore

class Window(QtGui.QWidget):
	"""
	A simple window wigdet
	"""
	def __init__(self):
		super(Window,self).__init__()
		self.initUI()
	
	def initUI(self):
		btn = QtGui.QPushButton('Quit',self)
		# when click quit button ,quit the application
		btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
		btn.resize(btn.sizeHint())
		btn.move(50,50)
		# set window 
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
