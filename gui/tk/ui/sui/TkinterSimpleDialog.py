# -*- coding:utf-8 -*-
# file: TkinterSimpleDialog.py
#
'''
tkSimpleDialog 
1 fun
askstring askinteger askfloat
2 attr
title prompt initalvalue
'''
# 1 import
import Tkinter
import tkSimpleDialog

#----------------------------------------
# user defined fun handler and classes
def InStr():
	r=tkSimpleDialog.askstring('Python Tkinter',
			'Input String',
			initialvalue='Tkinter')
	print r
def InInt():
	r=tkSimpleDialog.askinteger('Python Tkinter',
			'Input Integer')
	print r
def InFlo():
	r=tkSimpleDialog.askfloat('Python Tkinter',
			'Input Float')
	print r
#----------------------------------------
# layout
root=Tkinter.Tk()
# button1
button1=Tkinter.Button(root,
		text='input string',
		command=InStr) 
button1.pack(side='left')

# button2
button2=Tkinter.Button(root,
		text='input integer',
		command=InInt) 
button2.pack(side='left')

# button3
button3=Tkinter.Button(root,
		text='input float',
		command=InFlo) 
button3.pack(side='left')

#mainloop
root.mainloop()


