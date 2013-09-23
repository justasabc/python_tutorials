# -*- coding:utf-8 -*-
# file: TkinterFileDialog.py
#
'''
tkFileDialog 
1 fun
askopenfilename asksaveasfilename
2 attr
filetypes initialdir initialfile title
'''
# 1 import
import Tkinter
import tkFileDialog

#----------------------------------------
# user defined fun handler and classes
def FileOpen():
	r=tkFileDialog.askopenfilename(title='Python Tkinter',
			filetypes=[('Python','*.py *.pyw'),('All files','*')])
	print r
def FileSave():
	r=tkFileDialog.asksaveasfilename(title='Python Tkinter',
			initialdir=r'F:\Develop\Python\gui',
			initialfile='default.py')
	print r
#----------------------------------------
# layout
root=Tkinter.Tk()
# button1
button1=Tkinter.Button(root,
		text='file open',
		command=FileOpen) 
button1.pack(side='left')

# button2
button2=Tkinter.Button(root,
		text='file save as',
		command=FileSave) 
button2.pack(side='left')

#mainloop
root.mainloop()



