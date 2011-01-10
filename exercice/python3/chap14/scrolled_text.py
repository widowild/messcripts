#! /usr/bin/env python
# -*- coding:Utf8 -*-

# Construction d'un widget composite à l'aide du widget Text et d'un ascenseur :

from tkinter import *

class ScrolledText(Frame):
    """Widget composite, associant un widget Text et une barre de défilement"""
    def __init__(self, boss, baseFont ="Times", width =50, height =25):
        Frame.__init__(self, boss, bd =2, relief =SUNKEN)
        self.text =Text(self, font =baseFont, bg ='ivory', bd =1,
                        width =width, height =height)
        scroll =Scrollbar(self, bd =1, command =self.text.yview)
        self.text.configure(yscrollcommand =scroll.set)
        self.text.pack(side =LEFT, expand =YES, fill =BOTH, padx =2, pady =2)
        scroll.pack(side =RIGHT, expand =NO, fill =Y, padx =2, pady =2)

    def importFichier(self, fichier, encodage ="Utf8"):
        "insertion d'un texte dans le widget, à partir d'un fichier"
        of =open(fichier, "r", encoding =encodage)
        lignes =of.readlines()
        of.close()
        for li in lignes:
            self.text.insert(END, li)

def chercheCible(event=None):
    "défilement du texte jusqu'à la balise <cible>, grâce à la méthode see()"
    index = st.text.tag_nextrange('cible', '0.0', END)
    st.text.see(index[0])

### Programme principal : fenêtre avec un libellé et un 'ScrolledText' ###
fen =Tk()
lib =Label(fen, text ="Widget composite : Text + Scrollbar",
           font ="Times 14 bold italic", fg ="navy")
lib.pack(padx =10, pady =4)
st =ScrolledText(fen, baseFont="Helvetica 12 normal", width =40, height =10)
st.pack(expand =YES, fill =BOTH, padx =8, pady =8)

# Définition de balises, liaison d'un événement <clic du bouton droit> :
st.text.tag_configure("titre", foreground ="brown",
                      font ="Helvetica 11 bold italic")
st.text.tag_configure("lien", foreground ="blue",
                      font ="Helvetica 11 bold")
st.text.tag_configure("cible", foreground ="forest green",
                      font ="Times 11 bold")
st.text.tag_bind("lien", "<Button-3>", chercheCible)

titre ="""Le Corbeau et le Renard
par Jean de la Fontaine, auteur français
\n"""
auteur ="""
Jean de la Fontaine
écrivain français (1621-1695)
célèbre pour ses Contes en vers,
et surtout ses Fables, publiées
de 1668 à 1694."""

# Remplissage du widget Text (2 techniques) :
st.importFichier("CorbRenard.txt", encodage ="Latin1")
st.text.insert("0.0", titre, "titre")
st.text.insert(END, auteur, "cible")
# Insertion d'une image :
photo =PhotoImage(file= "penguin.gif")
st.text.image_create("6.14", image =photo)
# Ajout d'une balise supplémentaire :
st.text.tag_add("lien", "2.4", "2.23")

fen.mainloop()
