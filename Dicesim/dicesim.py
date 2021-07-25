import random
import tkinter.font as font
from tkinter import *

root=Tk()
root.geometry('800x800')
col = ['red','green','yellow','violet','blue','brown','black','pink']
l1 = Label(root,text='',font=('times',300))
l2 = Label(root,text='',font=('times',300))
def roll():
	num = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
	l1.config(text=random.choice(num),fg=random.choice(col))
	l1.pack()
	l2.config(text=random.choice(num),fg=random.choice(col))
	l2.pack()


buttonFont = font.Font(family='Helvetica', size=16, weight='bold')
b = Button(root,text="Let's Roll!",height=2,width=20,command=roll,font=buttonFont,fg=random.choice(col))
b.place(x=270,y=0)

root.mainloop()