#! /usr/bin/env python
# -*- coding: Latin-1 -*-

def nomMois(n):
    "renvoie le nom du n-i�me mois de l'ann�e"
    mois = ['Janvier,', 'F�vrier', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet',
            'Ao�t', 'Septembre', 'Octobre', 'Novembre', 'D�cembre']
    return mois[n -1]       # les indices sont num�rot�s � partir de z�ro

# test :
print nomMois(4)
