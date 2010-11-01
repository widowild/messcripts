#!/usr/bin/env python3
# -*- coding:latin1 -*-
# Donner la valeur md5 d'un fichier
# dépendances: zenity

from tkinter import *
import os

def md5file():
    fichier = os.popen("zenity --file-selection").read().strip()
    if not fichier: exit(0)

def resultat():
    result = os.system(md5sum fichier)

fen1 = Tk()
fen1.title("Openbox")
#fen1.maxsize(width=300, height=60)
#fen1.minsize(width=150, height=30)
#fen1.resizable(width=YES, height=NO)
bou1 = Button(fen1, text='Lancer', command=md5file)
bou1.pack()
bou4 = Button(fen1, text='Annuler', command=fen1.quit)
bou4.pack()
fen1.mainloop()
