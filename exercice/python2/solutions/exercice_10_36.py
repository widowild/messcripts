#! /usr/bin/env python
# -*- coding: Latin-1 -*-

# Insertion de nouveaux �l�ments dans une liste existante

t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['Janvier','F�vrier','Mars','Avril','Mai','Juin',
      'Juillet','Ao�t','Septembre','Octobre','Novembre','D�cembre']

c, d = 1, 0
while d < 12 :
     t2[c:c] = [t1[d]]       # ! l'�l�ment ins�r� doit �tre une liste
     c, d = c+2, d+1