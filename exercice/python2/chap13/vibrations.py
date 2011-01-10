#! /usr/bin/env python
# -*- coding: Latin-1 -*-

##################################################
#                Vibrations.py                   #
#  Trac� de graphiques �longation/temps pour 3   #
#      mouvements vibratoires harmoniques        #
#                                                #
#      Auteur : G.Swinnen (Li�ge, Belgium)       #
#         02/03/2002 - Licence GPL               #
##################################################

from oscillo import *
from curseurs import *

class ShowVibra(Frame):
    "D�monstration de mouvements vibratoires harmoniques"
    def __init__(self, master =None):
        Frame.__init__(self, master)        # constr. classe parente
        self.couleur=['dark green','red','purple']
        self.trace=[0]*3            # liste des trac�s
        self.controle=[0]*3         # liste des panneaux de contr�le

        # Instanciation du canevas avec axes X et Y :
        self.gra = OscilloGraphe(self, larg =400, haut=300)
        self.gra.configure(bg ='white', bd=4, relief=GROOVE)
        self.gra.pack(side =TOP, pady=5)

        # Instanciation de 3 panneaux de contr�le (curseurs) :
        for i in range(3):
            self.controle[i] = ChoixVibra(self,self.couleur[i])
            self.controle[i].pack()

        # D�signation de l'�v�nement qui d�clenche l'affichage des trac�s :
        self.master.bind('<Control-Z>', self.montreCourbes)

        # Mise en place :
        self.master.title('Mouvements vibratoires harmoniques')
        self.pack()

    def montreCourbes(self,event):
        "(r�)affichage des 3 graphiques �longation/temps"
        for i in range(3):
            # D'abord, effacer le trac� pr�c�dent (�ventuel) :
            self.gra.delete(self.trace[i])
            # Ensuite, dessiner le nouveau trac� :
            if self.controle[i].chk.get():
                self.trace[i] = self.gra.traceCourbe(
                                    coul=self.couleur[i],
                                    freq=self.controle[i].freq,
                                    phase=self.controle[i].phase,
                                    ampl=self.controle[i].ampl)

#### Code pour tester la classe : ###

if __name__ == '__main__':
    ShowVibra().mainloop()
