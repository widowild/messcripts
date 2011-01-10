#! /usr/bin/env python
# -*- coding:Utf-8 -*-

from exercice_12_02 import CompteBancaire

class CompteEpargne(CompteBancaire):
    def __init__(self, nom ='Durand', solde =500):
        CompteBancaire.__init__(self, nom, solde)
        self.taux =.3          # taux d'intérêt mensuel par défaut

    def changeTaux(self, taux):
        self.taux =taux

    def capitalisation(self, nombreMois =6):
        print "Capitalisation sur %s mois au taux mensuel de %s %%." %\
              (nombreMois, self.taux)
        for m in range(nombreMois):
            self.solde = self.solde * (100 +self.taux)/100

# Programme de test :

if __name__ == '__main__':
    c1 = CompteEpargne('Duvivier', 600)
    c1.depot(350)
    c1.affiche()
    c1.capitalisation(12)
    c1.affiche()
    c1.changeTaux(.5)
    c1.capitalisation(12)
    c1.affiche()

