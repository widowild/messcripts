#! /usr/bin/env python
# -*- coding:Utf8 -*-

# Tirage de cartes

from random import randrange

couleurs = ['Pique', 'Trèfle', 'Carreau', 'Cœur']
valeurs = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'valet', 'dame', 'roi', 'as']

# Construction de la liste des 52 cartes :
carte =[]
for coul in couleurs:
     for val in valeurs:
          carte.append("{} de {}".format(val, coul))

# Tirage au hasard :
while 1:
     k = input("Frappez <c> pour tirer une carte, <Enter> pour terminer ") 
     if k =="":
          break
     r = randrange(52)      # tirage au hasard d'un entier entre 0 et 51
     print(carte[r])
