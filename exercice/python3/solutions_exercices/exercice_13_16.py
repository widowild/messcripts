#! /usr/bin/env python
# -*- coding:Utf8 -*-

##################################################
#                Vibrations.py                   #
#  Tracé de graphiques élongation/temps pour 3   #
#      mouvements vibratoires harmoniques        #
#                                                #
#      Auteur : G.Swinnen (Liège, Belgium)       #
#       http://inforef.be/swi/python.htm         #
#           15/01/2010 - Licence GPL             #
##################################################

from tkinter import *
from math import sin, pi
from exercice_13_10 import OscilloGraphe

##################################################
#            Classe OscilloGrapheBis             #
#  Widget dérivé de <OscilloGraphe> spécialisé   #
#  pour le dessin de graphiques, avec surcharge  #
#  de sa méthode de tracé des axes.              #
##################################################

class OscilloGrapheBis(OscilloGraphe):
    """Classe dérivée du widget Oscillographe"""
    def __init__(self, master =None, larg =200, haut =150):
        # Appel du constructeur de la classe parente :
        OscilloGraphe.__init__(self, master, larg, haut)

    def traceAxes(self):
        "Surchage de la méthode de même nom dans la classe parente"
        # tracé de l'axe de référence Y :
        pas = (self.larg-25)/8.       # intervalles de l'échelle horizontale
        self.create_line(10+4*pas, self.haut-5, 10+4*pas, 5, fill ='grey90',
                         arrow=LAST)
        # tracé de l'axe de référence X :
        self.create_line(10, self.haut/2, self.larg, self.haut/2,
                         fill= 'grey90', arrow=LAST)
        # indication des grandeurs physiques aux extrémités des axes :
        self.create_text(20+4*pas, 15, anchor=CENTER, text="e", fill='red')
        self.create_text(self.larg-5, self.haut/2-12, anchor=CENTER, text ="t",
                         fill='red')

##################################################
#              Classe ChoixVibra                 #
#  Widget contenant un groupe de curseurs pour   #
#  contrôler trois paramètres (f,phi,a).         #
#  Un événement spécifique est généré à chaque   #
#  modification, pour informer le widget maître  #
#  qui peut alors réagir en conséquence          #
##################################################

class ChoixVibra(Frame):
    """Curseurs pour choisir fréquence, phase & amplitude d'une vibration"""
    def __init__(self, master=None, coul='red'):
        Frame.__init__(self)        # constructeur de la classe parente
        # Définition de quelques attributs d'instance :
        self.freq, self.phase, self.ampl, self.coul = 0, 0, 0, coul
        # Variable d'état de la case à cocher :
        self.chk = IntVar()                 # 'objet-variable' Tkinter
        Checkbutton(self, text='Afficher', variable=self.chk,
                    fg = self.coul, command=self.setCurve).pack(side=LEFT)
        # Définition des 3 widgets curseurs :
        Scale(self, length=150, orient=HORIZONTAL, sliderlength =25,
              label ='Fréquence (Hz) :', from_=1., to=9., tickinterval =2,
              resolution =0.25, showvalue =0,
              command = self.setFrequency).pack(side=LEFT, pady =5)
        Scale(self, length=150, orient=HORIZONTAL, sliderlength =15,
              label ='Phase (degrés) :', from_=-180, to=180, tickinterval =90,
              showvalue =0, command = self.setPhase).pack(side=LEFT, pady =5)
        Scale(self, length=150, orient=HORIZONTAL, sliderlength =25,
              label ='Amplitude :', from_=2, to=10, tickinterval =2,
              showvalue =0,
              command = self.setAmplitude).pack(side=LEFT, pady =5)

    def setCurve(self):
        self.master.event_generate('<Control-Z>')

    def setFrequency(self, f):
        self.freq = float(f)
        self.master.event_generate('<Control-Z>')

    def setPhase(self, p):
        pp =float(p)
        self.phase = pp*2*pi/360        # conversion degrés -> radians
        self.master.event_generate('<Control-Z>')

    def setAmplitude(self, a):
        self.ampl = float(a)
        self.master.event_generate('<Control-Z>')

###########################
#    Classe principale    #
###########################

class ShowVibra(Frame):
    """Démonstration de mouvements vibratoires harmoniques"""
    def __init__(self, master=None):
        Frame.__init__(self)          # constructeur de la classe parente
        self.couleur = ['green', 'yellow', 'orange']
        self.trace = [0]*3            # liste des tracés (courbes à dessiner)
        self.controle = [0]*3         # liste des panneaux de contrôle
        # Instanciation du canevas avec axes X et Y :
        self.gra = OscilloGrapheBis(self, larg =400, haut=300)
        self.gra.configure(bg ='grey40', bd=3, relief=SUNKEN)
        self.gra.pack(side =TOP, pady=3)
        # Instanciation de 3 panneaux de contrôle (curseurs) :
        for i in range(3):
            self.controle[i] = ChoixVibra(self, self.couleur[i])
            self.controle[i].configure(bd =3, relief = GROOVE)
            self.controle[i].pack(padx =10, pady =3)
        # Désignation de l'événement qui déclenche l'affichage des tracés :
        self.master.bind('<Control-Z>', self.montreCourbes)
        self.master.title('Mouvements vibratoires harmoniques')
        self.pack()

    def montreCourbes(self, event):
        """(Ré)Affichage des trois graphiques élongation/temps"""
        for i in range(3):
            # D'abord, effacer le tracé précédent (éventuel) :
            self.gra.delete(self.trace[i])
            # Ensuite, dessiner le nouveau tracé :
            if self.controle[i].chk.get():
                self.trace[i] = self.gra.traceCourbe(
                                    coul=self.couleur[i],
                                    freq=self.controle[i].freq,
                                    phase=self.controle[i].phase,
                                    ampl=self.controle[i].ampl)

#### Code pour tester la classe : ###

if __name__ == '__main__':
    ShowVibra().mainloop()

