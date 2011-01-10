#! /usr/bin/env python
# -*- coding: Latin-1 -*-

# Exemple montrant comment faire en sorte que les objets dessin�s dans un
# canevas puissent �tre manipul�s � l'aide de la souris
# (C) G.Swinnen, Verviers, 2003.  Licence = GPL

from Tkinter import *
from random import randrange

class Draw(Frame):
    "classe d�finissant la fen�tre principale du programme"
    def __init__(self):
        Frame.__init__(self)
    	# mise en place du canevas - dessin de 15 ellipses color�s :
        self.c = Canvas(self, width =400, height =300, bg ='ivory')
        self.c.pack(padx =5, pady =3)
        for i in range(15):
            # tirage d'une couleur au hasard :
            coul =['brown','red','orange','yellow','green','cyan','blue',
                   'violet', 'purple'][randrange(9)]
            # trac� d'une ellipse avec coordonn�es al�atoires :
            x1, y1 = randrange(300), randrange(200)
            x2, y2 = x1 + randrange(10, 150), y1 + randrange(10, 150)
            self.c.create_oval(x1, y1, x2, y2, fill =coul)
        # liaison d'�v�nements <souris> au widget <canevas> :
        self.c.bind("<Button-1>", self.mouseDown)
        self.c.bind("<Button1-Motion>", self.mouseMove)
        self.c.bind("<Button1-ButtonRelease>", self.mouseUp)
        # mise en place d'un bouton de sortie :
        b_fin = Button(self, text ='Terminer', bg ='royal blue', fg ='white',
                       font =('Helvetica', 10, 'bold'), command =self.quit)
        b_fin.pack(pady =2)
        self.pack()

    def mouseDown(self, event):
        "Op. � effectuer quand le bouton gauche de la souris est enfonc�"
        self.currObject =None
        # event.x et event.y contiennent les coordonn�es du clic effectu� :
        self.x1, self.y1 = event.x, event.y
        # <find_closest> renvoie la r�f�rence du dessin le plus proche :
        self.selObject = self.c.find_closest(self.x1, self.y1)
        # modification de l'�paisseur du contour du dessin :
        self.c.itemconfig(self.selObject, width =3)
        # <lift> fait passer le dessin � l'avant-plan :
        self.c.lift(self.selObject)

    def mouseMove(self, event):
        "Op. � effectuer quand la souris se d�place, bouton gauche enfonc�"
        x2, y2 = event.x, event.y
        dx, dy = x2 -self.x1, y2 -self.y1
        if self.selObject:
            self.c.move(self.selObject, dx, dy)
            self.x1, self.y1 = x2, y2

    def mouseUp(self, event):
        "Op. � effectuer quand le bouton gauche de la souris est rel�ch�"
        if self.selObject:
            self.c.itemconfig(self.selObject, width =1)
            self.selObject =None

if __name__ == '__main__':
    Draw().mainloop()
