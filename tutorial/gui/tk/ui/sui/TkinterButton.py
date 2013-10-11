# -*- coding=utf-8 -*-
#file : TkinterButton.py
#

'''
anchor:  
  N
W   E
  S
side: LEFT RIGHT BOTTOM TOP
'''

'''
Button attribute
anchor text width height bg state
'''
import Tkinter
root=Tkinter.Tk()
#button1
button1=Tkinter.Button(root,
		anchor=Tkinter.E,
		text='Button1',
		width=40,
		height=5,
		bg='red',
		state=Tkinter.DISABLED)
button1.pack()

#mainloop
root.mainloop()

