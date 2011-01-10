#! /usr/bin/env python
# -*- coding:Utf-8 -*-

class CompteBancaire(object):
    def __init__(self, nom ='Dupont', solde =1000):
        self.nom, self.solde = nom, solde
         
    def depot(self, somme):
        self.solde = self.solde + somme

    def retrait(self, somme):
        self.solde = self.solde - somme

    def affiche(self):
        print("Le solde du compte bancaire de {} est de {} euros.".\
              format(self.nom, self.solde))

# Programme de test :

if __name__ == '__main__':
    c1 = CompteBancaire('Duchmol', 800)
    c1.depot(350)
    c1.retrait(200)
    c1.affiche()
