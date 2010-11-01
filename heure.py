#!/usr/bin/env python
# -*- coding:utf8 -*-
#=================
from tkinter import *
import time
 
def tick():
    global time1
    time2 = time.strftime('%H:%M:%S')
    if time2 != time1:
        time1=time2
        var.set(time1)
        root.title(var.get())
    clock.after(200, tick)
 
root = Tk()
var = StringVar()
time1 = ' '
clock = Label(root, bg="green")
clock.pack(fill=BOTH, expand=1)
tick()
root.mainloop()
