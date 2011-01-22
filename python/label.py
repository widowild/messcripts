#!/usr/bin/env python3
# -*- coding:utf8 -*-
#=================

from tkinter import *
root=Tk()

def changeLabel():
    myString.set("I'm, a-fraid we're fresh out of red Leicester, sir. ")

myString=StringVar()
Label(root,textvariable=myString).pack()
myString.set("Well, eh, how about a little red Leicester.")
Button(root,text='Click Me',command=changeLabel).pack()
root.mainloop()
