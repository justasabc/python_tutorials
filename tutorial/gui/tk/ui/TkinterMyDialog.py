#-*- coding:utf-8 -*-
# file: TkinterMyDialog.py
#
# necessary import
import Tkinter
import tkMessageBox

#----------------------------------------------------------------------------------------------------------------------------------------------------------
# user defined fun and class
class MyDialog:
	def __init__(self,root):
		# top
		self.top=Tkinter.Toplevel(root)  # use 'Toplevel' to create a dialog
		self.label1=Tkinter.Label(self.top,text='name')
		self.label2=Tkinter.Label(self.top,text='age')
		self.label1.place(x=5,y=5)
		self.label2.place(x=5,y=30)

		self.entry1=Tkinter.Entry(self.top)
		self.entry2=Tkinter.Entry(self.top)
		self.entry1.place(x=40,y=5)
		self.entry2.place(x=40,y=30) 
		self.entry1.focus() # get focus 

		self.button1=Tkinter.Button(self.top,text='Ok',command=self.OkHandler) 
		self.button2=Tkinter.Button(self.top,text='Cancel',command=self.CancelHandler) 
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
		self.top.destroy()  # close dialog
	def CancelHandler(self):
		self.top.destroy()  # close dialog
	'''
	def GetName(self):
		return self.name
	def GetAge(self):
		return self.age
	'''
#----------------------------------------------------------------------------------------------------------------------------------------------------------

# root
root=Tkinter.Tk()
# user defined fun
def InputDialog():
	d=MyDialog(root)
        root.wait_window(d.top) # wait for top to close
	strinfo=d.name+str(d.age)
        tkMessageBox.showinfo('Info',strinfo) # show info

# 3.1 menu
menu1=Tkinter.Menu(root)
#submenu1
submenu1=Tkinter.Menu(menu1,tearoff=0) 
submenu1.add_command(label='MyDialog',command=InputDialog)
menu1.add_cascade(label='Dlg',menu=submenu1)

# mainloop
root.config(menu=menu1)
root.mainloop()

