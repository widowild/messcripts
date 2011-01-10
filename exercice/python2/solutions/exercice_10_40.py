#! /usr/bin/env python
# -*- coding: Latin-1 -*-

# Crible d'Eratosth�ne pour rechercher les nombres premiers de 1 � 999

# Cr�er une liste de 1000 �l�ments 1 (leurs indices vont de 0 � 999) :
lst = [1]*1000           
# Parcourir la liste � partir de l'�l�ment d'indice 2:
for i in range(2,1000):
    # Mettre � z�ro les �l�ments suivants dans la liste,
    # dont les indices sont des multiples de i :
    for j in range(i*2, 1000, i):
        lst[j] = 0

# Afficher les indices des �l�ments rest�s � 1 (on ignore l'�l�ment 0) :
for i in range(1,1000):
    if lst[i]:
        print i,
