# -*- coding:utf-8 -*-
# file: TkinterMessageBox.py
#
'''
tkMessageBox 
1 fun
askokcancel askquestion askyesno
showinfo showwarning showerror
2 attr
title message
'''
# 1 import
import Tkinter
import tkMessageBox

#----------------------------------------
# user defined fun handler and classes
def cmd():
	global n 
	global bt
	n=n+1
	if n==1:
		tkMessageBox.askokcancel('Python Tkinter','askokcancel')
		bt.set('askquestion')
	elif n==2:
		tkMessageBox.askquestion('Python Tkinter','askquestion')
		bt.set('askyesno')
	elif n==3:
		tkMessageBox.askyesno('Python Tkinter','askyesno')
		bt.set('showinfo')
	elif n==4:
		tkMessageBox.showinfo('Python Tkinter','showinfo')
		bt.set('showwarning')
	elif n==5:
		tkMessageBox.showwarning('Python Tkinter','showwarning')
		bt.set('showerror')
	else:
		tkMessageBox.showerror('Python Tkinter','showerror')
		bt.set('askokcancel')
#----------------------------------------
# init args
n=0

# layout
root=Tkinter.Tk()
#init args
bt=Tkinter.StringVar()
bt.set('askokcancel')
button1=Tkinter.Button(root,
		textvariable=bt, # related var
		command=cmd) 
button1.pack()

#mainloop
root.mainloop()

