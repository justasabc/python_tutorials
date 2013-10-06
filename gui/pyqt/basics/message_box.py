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
		# set window 
		self.setGeometry(300,300,250,150)
		self.setWindowTitle('hello world')
		self.setWindowIcon(QtGui.QIcon('apple.png'))
		self.show()

	def closeEvent(self,event):
		reply = QtGui.QMessageBox.question(self,'Message',"Are you sure to quit?",QtGui.QMessageBox.Yes|QtGui.QMessageBox.No,QtGui.QMessageBox.No)
		if reply == QtGui.QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()

def main():
	app = QtGui.QApplication(sys.argv)
	win = Window()
	# enter the mainloop of the application
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()
