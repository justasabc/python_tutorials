#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial 

In this example, we select a file with a
QtGui.QFileDialog and display its contents
in a QtGui.QTextEdit.

author: Jan Bodnar
website: zetcode.com 
last edited: October 2011
"""

import sys
from PyQt4 import QtGui


class Example(QtGui.QMainWindow):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

	# open file
        openFile = QtGui.QAction(QtGui.QIcon('open.png'), '&Open...', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.openDialog)
	
	# save file
        saveFile = QtGui.QAction(QtGui.QIcon('save.png'), '&Save...', self)
        saveFile.setShortcut('Ctrl+S')
        saveFile.setStatusTip('Save file')
        saveFile.triggered.connect(self.saveDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)       
        fileMenu.addAction(saveFile)       

	toolbar = self.addToolBar('File')
	toolbar.addAction(openFile)
	toolbar.addAction(saveFile)
	
	statusbar = self.statusBar()
        
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File dialog')
        self.show()
        
    def openDialog(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/home')
       	if fname.isEmpty(): 
		return
        f = open(fname, 'r')
        
        with f:        
            data = f.read()
            self.textEdit.setText(data) 
        
    def saveDialog(self):
	strfilter="ini files (*.ini);;Text files (*.txt)"
	fname = QtGui.QFileDialog.getSaveFileName(self,'choose a file name','.',strfilter)
	if fname.isEmpty():
		return
	print fname
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
