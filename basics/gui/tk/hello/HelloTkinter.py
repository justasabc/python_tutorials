# -*- coding=utf-8 -*-
#file: HelloTkinte.py
#
import Tkinter
root=Tkinter.Tk()
#label
label=Tkinter.Label(root,text='Hello,Tkinter!')
label.pack()
#button
button1=Tkinter.Button(root,text='button1')
button1.pack(side=Tkinter.LEFT)
button2=Tkinter.Button(root,text='button2')
button2.pack(side=Tkinter.RIGHT)
#mainloop
root.mainloop()

