#! /usr/bin/env python
# -*- coding:Utf8 -*-

# Affichage des éléments d'une liste

# Liste fournie au départ :
t2 = ['Janvier','Février','Mars','Avril','Mai','Juin',
      'Juillet','Août','Septembre','Octobre','Novembre','Décembre']

# Affichage :
i = 0
while i < len(t2):
    # affichage sans saut à la ligne (utilisation de l'argument 'end') :
    print(t2[i], end=' ')    
    i = i + 1
