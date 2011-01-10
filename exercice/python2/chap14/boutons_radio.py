#! /usr/bin/env python
# -*- coding: Latin-1 -*-

# Utilisation de boutons radio

from Tkinter import *

class RadioDemo(Frame):
    """D�mo : utilisation de widgets 'boutons radio'"""
    def __init__(self, master=None):
        """Cr�ation d'un champ d'entr�e avec 4 boutons radio"""
        Frame.__init__(self)
        self.pack()
        # Champ d'entr�e contenant un petit texte :
        self.texte = Entry(self, width =28, font ="Arial 14")
        self.texte.insert(END,"La programmation, c'est g�nial")
        self.texte.pack(padx =8, pady =8)
        # Nom fran�ais et nom technique des quatre styles de police :                  
        stylePoliceFr =["Normal", "Gras", "Italique", "Gras/Italique"]
        stylePoliceTk =["normal", "bold", "italic", "bold italic"]
        # Le style actuel est m�moris� dans une 'variable Tkinter' ;
        self.choixPolice = StringVar()
        self.choixPolice.set(stylePoliceTk[0])
        # Cr�ation des quatre 'boutons radio' :
        for n in range(4):
            bout = Radiobutton(self,
                               text = stylePoliceFr[n],
                               variable = self.choixPolice,
                               value = stylePoliceTk[n],
                               command = self.changePolice)
            bout.pack(side =LEFT, padx =5)

    def changePolice(self):
        """Remplacement de la police actuelle"""
        police = "Arial 15 " + self.choixPolice.get() 
        self.texte.configure(font =police)
                           
RadioDemo().mainloop()
