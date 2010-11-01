#!/usr/bin/env python
# -*- coding:utf8 -*-
#=================
# Dependance:
#python rsync, xterm

from Tkinter import *
import os
import subprocess

def synchronisation():
    pid = subprocess.Popen(["rsync -e ssh -avz --delete-after /media/TERATOR/mirror/ root@192.168.0.10:/shares/mirror/"]).pid
    fen1.destroy()

# Fenetre
fen1 = Tk()
fen1.title("synchronisation")
fen1.resizable(width=YES, height=NO)
bou1 = Button(fen1, text='synchronisation', command=synchronisation)
bou1.pack(side=LEFT)
bou2 = Button(fen1, text='Annuler', command=fen1.quit)
bou2.pack(side=LEFT)
fen1.mainloop()

