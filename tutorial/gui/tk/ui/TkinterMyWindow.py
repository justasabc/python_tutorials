#-*- coding:utf-8 -*-
# file: TkinterMyWindow.py
#
# necessary import
import Tkinter
import tkMessageBox

#----------------------------------------------------------------------------------------------------------------------------------------------------------
# user defined fun and class
class MyWindow:
	def __init__(self,root):
		self.label1=Tkinter.Label(root,text='name')
		self.label2=Tkinter.Label(root,text='age')
		self.label1.place(x=5,y=5)
		self.label2.place(x=5,y=30)

		self.entry1=Tkinter.Entry(root)
		self.entry2=Tkinter.Entry(root)
		self.entry1.place(x=40,y=5)
		self.entry2.place(x=40,y=30) 
		self.entry1.focus() # get focus 

		self.button1=Tkinter.Button(root,text='Ok',command=self.OkHandler) 
		self.button2=Tkinter.Button(root,text='Cancel',command=self.CancelHandler) 
		self.button1.place(x=40,y=55)
		self.button2.place(x=75,y=55)

		# name
		self.name='xxx'
		# age
		self.age=0
	def OkHandler(self):
		# name 
		self.name=self.entry1.get()
		# age 
		self.age=self.entry2.get()
		root.destroy()  # close dialog
	def CancelHandler(self):
		root.destroy()  # close dialog
#----------------------------------------------------------------------------------------------------------------------------------------------------------

# root
root=Tkinter.Tk()
mywindow=MyWindow(root) #main window
root.mainloop()


