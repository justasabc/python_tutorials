# -*- coding:utf-8 -*-
# file: TkinterCheck.py
#
'''
Radiobutton Checkbutton
anchor  text width height bg fg
justify  (LEFT RIGHT BOTTOM TOP CENTER)
value :given a value to contol
variable :a var related to control
1 when control is selected,the value of 'variable' equals to 'value'
2 Radiobutton-StringVar(attr:value):when the value of 'variable' equals to 'value',this control remains selected.
3 Checkbutton-IntVar(attr:onvalue,offvalue):when the value of 'variable' equals to 'value',this control remains selected.

special attribute:indicatoron
when indicatoron=0,Radiobutton and Checkbutton is displayed as Button.
'''
import Tkinter
root=Tkinter.Tk()

#var related to Radiobutton
r=Tkinter.StringVar()
r.set('1')

#radio1
radio1=Tkinter.Radiobutton(root,
		text='radio1',
	        # indicatoron=0,
		variable=r, # variable=value,so radio1 remains selected
		value='1')
radio1.pack()

#radio2
radio2=Tkinter.Radiobutton(root,
		text='radio2',
	        # indicatoron=0,
		variable=r, # when radio2 is selected,the value of r is 2
		value='2')
radio2.pack()

#radio3
radio3=Tkinter.Radiobutton(root,
		text='radio3',
	        # indicatoron=0,
		variable=r, # when radio3 is selected,the value of r is 3
		value='3')
radio3.pack()

#radio4
radio4=Tkinter.Radiobutton(root,
		text='radio4',
	        # indicatoron=0,
		variable=r, # when radio4 is selected,the value of r is 4
		value='4')
radio4.pack()

#check
c=Tkinter.IntVar()
c.set(1)
check=Tkinter.Checkbutton(root,
		text='Checkbutton',
	        # indicatoron=0,
		variable=c,
		onvalue=1, # when checkbutton is selected,the value of c is 1
		offvalue=2) # when checkbutton is not selected,the value of c is 2
check.pack()

#mainloop
root.mainloop()

#print value
print r.get()
print c.get()



