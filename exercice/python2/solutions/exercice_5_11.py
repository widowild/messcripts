#! /usr/bin/env python
# -*- coding: Latin-1 -*-

# Combinaison de deux listes en une seule

# Listes fournies au d�part :
t1 = [31,28,31,30,31,30,31,31,30,31,30,31]
t2 = ['Janvier','F�vrier','Mars','Avril','Mai','Juin',
      'Juillet','Ao�t','Septembre','Octobre','Novembre','D�cembre']
# Nouvelle liste � construire (vide au d�part) :
t3 = []
# Boucle de traitement :
i = 0
while i < len(t1):
    t3.append(t2[i])
    t3.append(t1[i])
    i = i + 1

# Affichage :
print t3 

