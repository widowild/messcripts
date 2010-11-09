#!/usr/bin/env python3
# -*- coding:Utf-8 -*-
#=================
# Donner la valeur md5 d'un fichier

from tkinter import *
from tkinter.filedialog import askopenfilename
import subprocess

# détermine la valeur md5sum
def resultat():
        try:
             fichier = askopenfilename()
        except IOError as e:
            sys.exit(e)
        else:
            if fichier:
                p = subprocess.Popen(["/usr/bin/md5sum", fichier], stdout=subprocess.PIPE)
                myString.set(p.stdout.readline().split()[0])
                print("Ouverture du fichier :", fichier)
            else:
                print("Vous n'avez pas selectionne de fichier")

fen1 = Tk()
fen1.title("MD5SUM")
fen1.maxsize(width=300, height=60)
fen1.minsize(width=300, height=30)
fen1.resizable(width=YES, height=NO)

# Afficher le chemin du fichier
#lbl = Label(fen1, textvariable=fichier,width=160)
#lbl.pack()

# Valeur md5
myString=StringVar()
Entry(fen1, textvariable=myString, width=160).pack()
myString.set("valeur md5sum.")
# Creation des boutons
bou1 = Button(fen1, text='Lancer', command=resultat)
bou1.pack(side="left")
bou4 = Button(fen1, text='Annuler', command=fen1.quit)
bou4.pack(side="left")
fen1.mainloop()
