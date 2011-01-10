#! /usr/bin/env python
# -*- coding:Utf8 -*-

class Satellite(object):
    def __init__(self, nom, masse =100, vitesse =0):
        self.nom, self.masse, self.vitesse = nom, masse, vitesse
         
    def impulsion(self, force, duree):
        self.vitesse = self.vitesse + force * duree / self.masse
        
    def energie(self):
        return self.masse * self.vitesse**2 / 2    
                
    def affiche_vitesse(self):
        print("Vitesse du satellite {} = {} m/s".\
              format(self.nom, self.vitesse))

# Programme de test :

s1 = Satellite('Zoé', masse =250, vitesse =10)

s1.impulsion(500, 15)
s1.affiche_vitesse()
print("énergie =", s1.energie())
s1.impulsion(500, 15)
s1.affiche_vitesse()
print("nouvelle énergie =", s1.energie())
