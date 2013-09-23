# -*- coding=utf-8 -*-
#file : TkinterLabel.py
#

'''
label atribute
anchor text width height bg fg
justify LEFT RIGHT BOTTOM TOP CENTER
'''
import Tkinter
root=Tkinter.Tk()

#label1
label1=Tkinter.Label(root,
		anchor=Tkinter.E,
		text='Python',
		width=30,
		height=5,
		bg='red',
		fg='blue'
		)
label1.pack()

#label2
label2=Tkinter.Label(root,
		text='Python GUI\nTkinter',
		width=30,
		height=5,
		justify=Tkinter.LEFT)
label2.pack()

#label3
label3=Tkinter.Label(root,
		text='Python GUI\nTkinter',
		width=30,
		height=5,
		justify=Tkinter.LEFT)
label3.pack()

#label4
label4=Tkinter.Label(root,
		text='Python GUI\nTkinter',
		width=30,
		height=5,
		justify=Tkinter.RIGHT)
label4.pack()

#label5
label5=Tkinter.Label(root,
		text='Python GUI\nTkinter',
		width=30,
		height=5,
		justify=Tkinter.CENTER)
label5.pack()
#mainloop
root.mainloop()



