# -*- coding=utf-8 -*-
#file : TkinterMenu.py
#

import Tkinter
root=Tkinter.Tk()

#menu
menu=Tkinter.Menu(root)
#submenu1
submenu1=Tkinter.Menu(menu,tearoff=0) 
submenu1.add_command(label='Open')
submenu1.add_command(label='Save')
submenu1.add_command(label='Close')
menu.add_cascade(label='File',menu=submenu1)

#submenu2
submenu2=Tkinter.Menu(menu,tearoff=0) 
submenu2.add_command(label='Copy')
submenu2.add_command(label='Paste')
submenu2.add_separator()
submenu2.add_command(label='Cut')
menu.add_cascade(label='Edit',menu=submenu2)

#submenu3
submenu3=Tkinter.Menu(menu,tearoff=0) 
submenu3.add_command(label='About')
menu.add_cascade(label='Help',menu=submenu3)

root.config(menu=menu)
root.mainloop()

