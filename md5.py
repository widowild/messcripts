#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#=================
# Donner la valeur md5 d'un fichier

from tkinter import *
from tkinter.filedialog import askopenfilename
import subprocess

# détermine la valeur md5sum
def resultat():
    fichier = askopenfilename()
    p = subprocess.Popen(["/usr/bin/md5sum", fichier], stdout=subprocess.PIPE)
    myString.set(p.stdout.readline().split()[0])

fen1 = Tk()
fen1.title("MD5SUM")
fen1.maxsize(width=300, height=60)
fen1.minsize(width=150, height=30)
fen1.resizable(width=YES, height=NO)

# Valeur md5
myString=StringVar()
Label(fen1,textvariable=myString).pack()
myString.set("valeur md5sum.")

# Creation des boutons

bou1 = Button(fen1, text='Lancer', command=resultat)
bou1.pack(side="left")
bou4 = Button(fen1, text='Annuler', command=fen1.quit)
bou4.pack(side="left")
fen1.mainloop()
