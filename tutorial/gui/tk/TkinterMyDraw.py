#-*- coding:utf-8 -*-
# file: TkinterMyDraw.py
#
'''
bind(sequence,func [,add])
bind_class(class,sequence,func [,add])
bind_all(sequence,func [,add])
sequence
1 mouse
<Button-1>
<ButtonPress-1>
<ButtonRelease-1>
<B1-Motion>
<Double-Button-1>
<Enter> <Leave>
<MouseWheel>
(1 Left,2 Middle,3 Right)
2 keyboard
<KeyPress-A>
<Alt-KeyPress-A>
<Ctrl-KeyPress-A>
<Shift-KeyPress-A>
<Double-KeyPress-A>
(KeyPress KeyRelease)
3 window
Activate Deactivate
Configure
Destroy
FocusIn FocusOut
Property
Visibility
Map Unmap
'''
# 1 necessary import
import Tkinter

#-------------------------------------------
# 2 user defined fun and class


#-------------------------------------------
# 3 layout (menu,popupmenu,canvas)
root=Tkinter.Tk()

# 3.1 menu
menu1=Tkinter.Menu(root)
#submenu1
submenu1=Tkinter.Menu(menu1,tearoff=0) 
submenu1.add_command(label='Line')
submenu1.add_command(label='Rect')
submenu1.add_command(label='Oval')
menu1.add_cascade(label='Draw',menu=submenu1)

#submenu3
submenu3=Tkinter.Menu(menu1,tearoff=0) 
submenu3.add_command(label='About')
menu1.add_cascade(label='Help',menu=submenu3)

# 3.2 canvas
canvas1=Tkinter.Canvas(root,
		width=600,
		height=480,
		bg='gray')
canvas1.pack()

# 3.3 popupmenu
#popupmenu1
popupmenu1=Tkinter.Menu(root,tearoff=0) 
popupmenu1.add_command(label='Line')
popupmenu1.add_command(label='Rect')
popupmenu1.add_command(label='Oval')

#popupmenu event method
def mypopupmenu(event):
	popupmenu1.post(event.x_root,event.y_root)
root.bind('<Button-3>',mypopupmenu)

# mainloop
root.config(menu=menu1)
root.mainloop()
