# -*- coding:Latin-1 -*-

from Tkinter import *

def cercle(can, x, y, r):
    "dessin d'un cercle de rayon <r> en <x,y> dans le canevas <can>"
    can.create_oval(x-r, y-r, x+r, y+r)

class Application(Tk):
    def __init__(self):
        Tk.__init__(self)        # constructeur de la classe parente
        self.can =Canvas(self, width =475, height =130, bg ="white")
        self.can.pack(side =TOP, padx =5, pady =5)
        Button(self, text ="Train", command =self.dessine).pack(side =LEFT)
        Button(self, text ="Hello", command =self.coucou).pack(side =LEFT)
        
    def dessine(self):
        "instanciation de 4 wagons dans le canevas"
        self.w1 = Wagon(self.can, 10, 30)
        self.w2 = Wagon(self.can, 130, 30)
        self.w3 = Wagon(self.can, 250, 30)
        self.w4 = Wagon(self.can, 370, 30)
        
    def coucou(self):
        "apparition de personnages dans certaines fen�tres"
        self.w1.perso(3)        # 1er wagon, 3e fen�tre
        self.w3.perso(1)        # 3e wagon, 1e fen�tre
        self.w3.perso(2)        # 3e wagon, 2e fen�tre
        self.w4.perso(1)        # 4e wagon, 1e fen�tre
        
class Wagon(object):
    def __init__(self, canev, x, y):
        "dessin d'un petit wagon en <x,y> dans le canevas <canev>"
        # m�morisation des param�tres dans des variables d'instance :
        self.canev, self.x, self.y = canev, x, y
        # rectangle de base : 95x60 pixels :
        canev.create_rectangle(x, y, x+95, y+60)
        # 3 fen�tres de 25x40 pixels, �cart�es de 5 pixels :
        for xf in range(x +5, x +90, 30):
            canev.create_rectangle(xf, y+5, xf+25, y+40)
        # 2 roues de rayon �gal � 12 pixels  :
        cercle(canev, x+18, y+73, 12)
        cercle(canev, x+77, y+73, 12)
  
    def perso(self, fen):
        "apparition d'un petit personnage � la fen�tre <fen>"
        # calcul des coordonn�es du centre de chaque fen�tre :
        xf = self.x + fen*30 -12
        yf = self.y + 25
        cercle(self.canev, xf, yf, 10)      # visage
        cercle(self.canev, xf-5, yf-3, 2)   # oeil gauche        
        cercle(self.canev, xf+5, yf-3, 2)   # oeil droit
        cercle(self.canev, xf, yf+5, 3)     # bouche

app = Application()
app.mainloop()
