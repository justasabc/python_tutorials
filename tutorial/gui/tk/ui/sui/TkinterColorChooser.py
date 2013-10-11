# -*- coding:utf-8 -*-
# file: TkinterColorChooser.py
#
'''
tkColorChooser
1 fun
askcolor
2 attr
initialcolor title
'''
# 1 import
import Tkinter
import tkColorChooser

#----------------------------------------
# user defined fun handler and classes
def ChooseColor():
	r=tkColorChooser.askcolor(title='Python Tkinter')
	print r
#----------------------------------------
# layout
root=Tkinter.Tk()
# button1
button1=Tkinter.Button(root,
		text='choose color',
		command=ChooseColor) 
button1.pack(side='left')

#mainloop
root.mainloop()




