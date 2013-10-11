# -*- coding=utf-8 -*- 
#file : TkinterPopupMenu.py
# 
import Tkinter
root=Tkinter.Tk()

#popupmenu1
popupmenu1=Tkinter.Menu(root,tearoff=0) 
popupmenu1.add_command(label='Copy')
popupmenu1.add_command(label='Paste')
popupmenu1.add_separator()
popupmenu1.add_command(label='Cut')

#event method
def mypopupmenu(event):
	popupmenu1.post(event.x_root,event.y_root)
root.bind('<Button-3>',mypopupmenu)

#mainloop
root.mainloop()


