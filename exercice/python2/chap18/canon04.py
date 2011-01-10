# -*- coding:Latin-1 -*-

#######################################################
# Jeu des bombardes - version monoposte - 4 joueurs   #
# (C) G�rard Swinnen, Verviers (Belgique) - July 2004 #
# Licence : GPL                                       #
#######################################################

from Tkinter import *
from math import sin, cos, pi
from random import randrange
import canon03

class Canon(canon03.Canon):
    """Canon am�lior�"""
    def __init__(self, boss, id, x, y, sens, coul):
        canon03.Canon.__init__(self, boss, id, x, y, sens, coul)
  
    def deplacer(self, x, y, rel=False):
        "d�placement, relatif si <rel> est vrai, absolu si <rel> est faux"
        if rel:
            dx, dy = x, y
        else:
            dx, dy = x -self.x1, y -self.y1
        # limites horizontales :
        if self.sens ==1:
            xa, xb = 20, int(self.xMax *.33)
        else:
            xa, xb = int(self.xMax *.66), self.xMax -20
        # ne d�placer que dans ces limites :
        if self.x1 +dx < xa:
            dx = xa -self.x1
        elif self.x1 +dx > xb:
            dx = xb -self.x1
        # limites verticales :
        ya, yb = int(self.yMax *.4), self.yMax -20
        # ne d�placer que dans ces limites :
        if self.y1 +dy < ya:
            dy = ya -self.y1
        elif self.y1 +dy > yb:
            dy = yb -self.y1
        # d�placement de la buse et du corps du canon :     
        self.boss.move(self.buse, dx, dy) 
        self.boss.move(self.corps, dx, dy) 
        # renvoyer les nouvelles coord. au programme appelant :
        self.x1 += dx
        self.y1 += dy
        self.x2 += dx
        self.y2 += dy
        return self.x1, self.y1  

    def fin_animation(self):
        "actions � accomplir lorsque l'obus a termin� sa trajectoire"
        # d�placer le canon qui vient de tirer :
        self.appli.depl_aleat_canon(self.id)
        # cacher l'obus (en l'exp�diant hors du canevas) :
        self.boss.coords(self.obus, -10, -10, -10, -10)

    def effacer(self):
        "faire dispara�tre le canon du canevas"
        self.boss.delete(self.buse)
        self.boss.delete(self.corps)
        self.boss.delete(self.obus)        

class AppBombardes(Frame):
    '''Fen�tre principale de l'application'''
    def __init__(self, larg_c, haut_c):
        Frame.__init__(self)
        self.pack()
        self.xm, self.ym = larg_c, haut_c
        self.jeu = Canvas(self, width =self.xm, height =self.ym,
                          bg ='ivory', bd =3, relief =SUNKEN)
        self.jeu.pack(padx =4, pady =4, side =TOP)

        self.guns ={}           # dictionnaire des canons pr�sents
        self.pupi ={}           # dictionnaire des pupitres pr�sents
        self.specificites()     # objets diff�rents dans classes d�riv�es

    def specificites(self):
        "instanciation des canons et des pupitres de pointage"
        self.master.title('<<< Jeu des bombardes >>>')
        id_list =[("Paul","red"),("Rom�o","cyan"),
                  ("Virginie","orange"),("Juliette","blue")]
        s = False
        for id, coul in id_list:
            if s:
                sens =1
            else:
                sens =-1
            x, y = self.coord_aleat(sens)
            self.guns[id] = Canon(self.jeu, id, x, y, sens, coul)
            self.pupi[id] = canon03.Pupitre(self, self.guns[id])
            s = not s           # changer de c�t� � chaque it�ration

    def depl_aleat_canon(self, id):
        "d�placer al�atoirement le canon <id>"
        gun =self.guns[id]
        dx, dy = randrange(-60, 61), randrange(-60, 61)
        # d�placement (avec r�cup�ration des nouvelles coordonn�es) :
        x, y = gun.deplacer(dx, dy, True)
        return x, y

    def coord_aleat(self, s):
        "coordonn�es al�atoires, � gauche (s =1) ou � droite (s =-1)" 
        y =randrange(int(self.ym /2), self.ym -20)
        if s == -1:
            x =randrange(int(self.xm *.7), self.xm -20)
        else:
            x =randrange(20, int(self.xm *.3))
        return x, y
  
    def goal(self, i, j):
        "le canon n�i signale qu'il a atteint l'adversaire n�j"
        # de quel camp font-ils partie chacun ?
        ti, tj = self.guns[i].sens, self.guns[j].sens        
        if ti != tj :               # ils sont de sens oppos�s :
            p = 1                   # on gagne 1 point
        else:                       # ils sont dans le m�me sens :
            p = -2                  # on a touch� un alli� !!
        self.pupi[i].attribuerPoint(p)
        # celui qui est touch� perd de toute fa�on un point :
        self.pupi[j].attribuerPoint(-1)

    def dictionnaireCanons(self):
        "renvoyer le dictionnaire d�crivant les canons pr�sents" 
        return self.guns

if __name__ =='__main__':
    AppBombardes(650, 300).mainloop()
