#!/usr/bin/env python3
# -*- coding:utf8 -*-
#=================
# Dependance:
# python, tk, opera

from tkinter import *
import os
import subprocess

# Opera Devel
def operadevel():
    pid = subprocess.Popen(["opera-devel"]).pid
    fen1.destroy()

# opera-ragnarok-labs
def operalabs():
    pid = subprocess.Popen(["opera-ragnarok-labs"]).pid
    fen1.destroy()

# Opera
def opera():
    pid = subprocess.Popen(["opera"]).pid
    fen1.destroy()


fen1 = Tk()
fen1.title("Opera")
#fen1.maxsize(width=550, height=60)
#fen1.minsize(width=150, height=30)
fen1.resizable(width=YES, height=NO)
bou1 = Button(fen1, text='Opera Devel', command=operadevel)
bou1.pack(side=LEFT)
bou2 = Button(fen1, text='opera-labs', command=operalabs)
bou2.pack(side=LEFT)
bou3 = Button(fen1, text='Opera', command=opera)
bou3.pack(side=LEFT)
bou4= Button(fen1, text='Annuler', command=fen1.quit)
bou4.pack(side=LEFT)
fen1.mainloop()
