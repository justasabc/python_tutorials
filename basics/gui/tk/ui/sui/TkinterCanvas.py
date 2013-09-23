# -*- coding:utf-8 -*-
#file: TkinterCanvas.py
#
'''
1 canvas attribute
bg fg width height
2 canvas method
create_arc/bitmap/image/line/oval/polygon/rectangle/text/window
delete
'''
import Tkinter
root=Tkinter.Tk()
canvas=Tkinter.Canvas(root,
		width=600,
		height=480,
		bg='white')
canvas.create_text(100,100,
		text='Use canvas',
		fill='red')
canvas.create_line(200,200,250,250)
canvas.create_rectangle(300,300,350,350,
		width=10)
canvas.create_polygon(50,0,100,50,50,100,0,50,
		fill='blue')
canvas.create_arc(150,150,200,200,
		start=45,extent=180,
		fill='yellow')
canvas.pack()
root.mainloop()



