#! /usr/bin/env python
# -*- coding: Latin-1 -*-

##################################################
#                 Colordic.py                    #
#      Auteur : G.Swinnen (Li�ge, Belgium)       #
#    http://www.ulg.ac.be/cifen/inforef/swi      #
#           21/07/2004 - Licence GPL             #
##################################################

from Tkinter import *
# Module donnant acc�s aux bo�tes de dialogue standard pour
# la recherche de fichiers sur disque :
from tkFileDialog import asksaveasfile, askopenfile

class Application(Frame):
    '''Fen�tre d'application'''
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Cr�ation d'un dictionnaire de couleurs")

        self.dico ={}       # cr�ation du dictionnaire

        # Les widgets sont regroup�s dans deux cadres (Frames) : 
        frSup =Frame(self)      # cadre sup�rieur contenant 6 widgets 
        Label(frSup, text ="Nom de la couleur :",
              width =20).grid(row =1, column =1)
        self.enNom =Entry(frSup, width =25)        # champ d'entr�e pour
        self.enNom.grid(row =1, column =2)         # le nom de la couleur
        Button(frSup, text ="Existe d�j� ?", width =12,
               command =self.chercheCoul).grid(row =1, column =3)
        Label(frSup, text ="Code hexa. corresp. :",
              width =20).grid(row =2, column =1)
        self.enCode =Entry(frSup, width =25)        # champ d'entr�e pour
        self.enCode.grid(row =2, column =2)         # le code hexa.
        Button(frSup, text ="Test", width =12,
               command =self.testeCoul).grid(row =2, column =3)
        frSup.pack(padx =5, pady =5)
        
        frInf =Frame(self)      # cadre inf�rieur contenant le reste
        self.test = Label(frInf, bg ="white", width =45,    # zone de test
                          height =7, relief = SUNKEN)
        self.test.pack(pady =5)   
        Button(frInf, text ="Ajouter la couleur au dictionnaire",
               command =self.ajouteCoul).pack()
        Button(frInf, text ="Enregistrer le dictionnaire", width =25,
               command =self.enregistre).pack(side = LEFT, pady =5)
        Button(frInf, text ="Restaurer le dictionnaire", width =25,
               command =self.restaure).pack(side =RIGHT, pady =5)
        frInf.pack(padx =5, pady =5)
        self.pack()        
        
    def ajouteCoul(self):
        "ajouter la couleur pr�sente au dictionnaire"
        if self.testeCoul() ==0:        # une couleur a-t-elle �t� d�finie ?
            return       
        nom = self.enNom.get()
        if len(nom) >1:                 # refuser les noms trop petits
            self.dico[nom] =self.cHexa
        else:
            self.test.config(text ="%s : nom incorrect" % nom, bg ='white') 

    def chercheCoul(self):
        "rechercher une couleur d�j� inscrite au dictionnaire"
        nom = self.enNom.get()
        if self.dico.has_key(nom):
            self.test.config(bg =self.dico[nom], text ="")
        else:
            self.test.config(text ="%s : couleur inconnue" % nom, bg ='white') 
    
    def testeCoul(self):
        "v�rifier la validit� d'un code hexa. - afficher la couleur corresp."
        try:
            self.cHexa =self.enCode.get()
            self.test.config(bg =self.cHexa, text ="")
            return 1
        except:
            self.test.config(text ="Codage de couleur incorrect", bg ='white')
            return 0

    def enregistre(self):
        "enregistrer le dictionnaire dans un fichier texte"
        # Cette m�thode utilise une bo�te de dialogue standard pour la
        # s�lection d'un fichier sur disque. Tkinter fournit toute une s�rie
        # de fonctions associ�es � ces bo�tes, dans le module tkFileDialog.
        # La fonction ci-dessous renvoie un objet-fichier ouvert en �criture :
        ofi =asksaveasfile(filetypes=[("Texte",".txt"),("Tous","*")]) 
        for clef, valeur in self.dico.items():
            ofi.write("%s %s\n" % (clef, valeur))
        ofi.close()

    def restaure(self):
        "restaurer le dictionnaire � partir d'un fichier de m�morisation"
        # La fonction ci-dessous renvoie un objet-fichier ouvert en lecture :
        ofi =askopenfile(filetypes=[("Texte",".txt"),("Tous","*")]) 
        lignes = ofi.readlines()
        for li in lignes:
            cv = li.split()     # extraction de la cl� et la valeur corresp.
            self.dico[cv[0]] = cv[1]
        ofi.close()

if __name__ == '__main__':
    Application().mainloop()

