#! /usr/bin/env python
# -*- coding: Latin-1 -*-

##################################################
#                 Oscillo.py                     #
#  Widget d�riv� de <Canvas>, sp�cialis� pour    #
#  dessiner des graphiques �longation/temps      #
#                                                #
#      Auteur : G.Swinnen (Li�ge, Belgium)       #
#         16/03/2002 - Licence GPL               #
##################################################

from Tkinter import *
from math import sin, pi

class OscilloGraphe(Canvas):
    "Canevas sp�cialis�, pour dessiner des courbes �longation/temps"
    def __init__(self, master=None, larg=200, haut=150):
        "Constructeur du graphique : axes et �chelle horiz."
        # construction du widget parent :
        Canvas.__init__(self)                             # appel au constructeur 
        self.configure(width=larg, height=haut)           # de la classe parente 
        self.larg, self.haut = larg, haut                         # m�morisation
        # trac� des axes de r�f�rence :
        self.create_line(10, haut/2, larg, haut/2, arrow=LAST)    # axe X
        self.create_line(10, haut-5, 10, 5, arrow=LAST)           # axe Y
        # trac� d'une �chelle avec 8 graduations :
        pas = (larg-25)/8.          # intervalles de l'�chelle horizontale
        for t in range(1, 9):
            stx = 10 + t*pas        # +10 pour partir de l'origine
            self.create_line(stx, haut/2-4, stx, haut/2+4)
        
    def traceCourbe(self, freq=1, phase=0, ampl=10, coul='red'):
        "trac� d'un graphique �longation/temps sur 1 seconde"
        curve =[]                       # liste des coordonn�es
        pas = (self.larg-25)/1000.      # l'�chelle X correspond � 1 seconde
        for t in range(0,1001,5):       # que l'on divise en 1000 ms.
            e = ampl*sin(2*pi*freq*t/1000 - phase)
            x = 10 + t*pas
            y = self.haut/2 - e*self.haut/25
            curve.append((x,y))
        n = self.create_line(curve, fill=coul, smooth=1)
        return n                        # n = num�ro d'ordre du trac�

#### Code pour tester la classe : ####

if __name__ == '__main__':
    root = Tk()
    gra = OscilloGraphe(root, 250, 180)
    gra.pack()
    gra.configure(bg ='ivory', bd =2, relief=SUNKEN)
    gra.traceCourbe(2, 1.2, 10, 'purple')
    root.mainloop()
    
