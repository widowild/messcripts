#!/usr/bin/env python3
# -*- coding:utf8 -*-
#=================
# python3
# tkinter
# xset
#=================
# Eteindre l'écran avec xset
#=================
from tkinter import *
import os
import subprocess

# Eteindre l'ecran
def blackall():
    print("Eteindre l'écran")
    output = subprocess.Popen(['xset', 'dpms', 'force', 'off'])

fen1 = Tk()
fen1.title("Ecran")
fen1.maxsize(width=300, height=60)
fen1.minsize(width=150, height=30)
fen1.resizable(width=YES, height=NO)
bou1 = Button(fen1, text="Eteindre l'écran", fg='red', command=blackall)
bou1.pack()
bou4 = Button(fen1, text='Annuler', command=fen1.quit)
bou4.pack()
fen1.mainloop()
