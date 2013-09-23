# -*- coding=utf-8 -*-
#file : TkinterEntry.py
#

'''
anchor:  
  N
W   E
  S
side: LEFT RIGHT BOTTOM TOP
'''

'''
Entry attribute
width state
show (* #)
selectbackground selectforeground
'''
import Tkinter
root=Tkinter.Tk()
#entry1
entry1=Tkinter.Entry(root,
		width=40,
		show='*')
entry1.pack()

#entry2
entry2=Tkinter.Entry(root,
		bg='red',
		fg='blue',
		selectbackground='black',
		selectforeground='yellow')
entry2.pack()

#entry3
entry3=Tkinter.Entry(root,
		state=Tkinter.DISABLED)
entry3.pack()

#text1
text1=Tkinter.Text(root,
		selectbackground='gray',
		selectforeground='blue')
text1.pack()

#mainloop
root.mainloop()


