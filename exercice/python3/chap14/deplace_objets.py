#! /usr/bin/env python
# -*- coding:Utf8 -*-

# Exemple montrant comment faire en sorte que les objets dessinés dans un
# canevas puissent être manipulés à l'aide de la souris
# (C) G.Swinnen, Verviers, 2009.  Licence = GPL

from tkinter import *
from random import randrange

class Bac_a_sable(Canvas):
    "Canevas modifié pour prendre en compte quelques actions de la souris"
    def __init__(self, boss, width=80, height=80, bg="white"):
        # invocation du constructeur de la classe parente :
        Canvas.__init__(self, boss, width=width, height=height, bg=bg)
        # association-liaison d'événements <souris> au présent widget :
        self.bind("<Button-1>", self.mouseDown)
        self.bind("<Button1-Motion>", self.mouseMove)
        self.bind("<Button1-ButtonRelease>", self.mouseUp)

    def mouseDown(self, event):
        "Opération à effectuer quand le bouton gauche de la souris est enfoncé"
        self.currObject =None
        # event.x et event.y contiennent les coordonnées du clic effectué :
        self.x1, self.y1 = event.x, event.y
        # <find_closest> renvoie la référence du dessin le plus proche :
        self.selObject = self.find_closest(self.x1, self.y1)
        # modification de l'épaisseur du contour du dessin :
        self.itemconfig(self.selObject, width =3)
        # <lift> fait passer le dessin à l'avant-plan :
        self.lift(self.selObject)

    def mouseMove(self, event):
        "Op. à effectuer quand la souris se déplace, bouton gauche enfoncé"
        x2, y2 = event.x, event.y
        dx, dy = x2 -self.x1, y2 -self.y1
        if self.selObject:
            self.move(self.selObject, dx, dy)
            self.x1, self.y1 = x2, y2

    def mouseUp(self, event):
        "Op. à effectuer quand le bouton gauche de la souris est relâché"
        if self.selObject:
            self.itemconfig(self.selObject, width =1)
            self.selObject =None

if __name__ == '__main__':      # ---- Programme de test ----
    couleurs =('red','orange','yellow','green','cyan','blue','violet','purple')
    fen =Tk()
    # mise en place du canevas - dessin de 15 ellipses colorés :
    bac =Bac_a_sable(fen, width =400, height =300, bg ='ivory')
    bac.pack(padx =5, pady =3)
    # bouton de sortie :
    b_fin = Button(fen, text ='Terminer', bg ='royal blue', fg ='white',
                   font =('Helvetica', 10, 'bold'), command =fen.quit)
    b_fin.pack(pady =2)
    # tracé de 15 ellipses avec couleur et coordonnées aléatoires :
    for i in range(15):
        coul =couleurs[randrange(8)]
        x1, y1 = randrange(300), randrange(200)
        x2, y2 = x1 + randrange(10, 150), y1 + randrange(10, 150)
        bac.create_oval(x1, y1, x2, y2, fill =coul)
    fen.mainloop()
