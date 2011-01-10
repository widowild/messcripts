#! /usr/bin/env python
# -*- coding: Latin-1 -*-

## Cette variante utilise une liste de listes ##
## (que l'on pourrait ais�ment remplacer par deux listes distinctes)

# La liste ci-dessous contient deux �l�ments qui sont eux-m�mes des listes.
# l'�l�ment 0 contient les nombres de jours de chaque mois, tandis que
# l'�l�ment 1 contient les noms des douze mois :
mois = [[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        ['Janvier', 'F�vrier', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet',
         'Ao�t', 'Septembre', 'Octobre', 'Novembre', 'D�cembre']]

jour = ['Dimanche','Lundi','Mardi','Mercredi','Jeudi','Vendredi','Samedi']

ja, jm, js, m = 0, 0, 0, 0

while ja <365:
    ja, jm = ja +1, jm +1    # ja = jour dans l'ann�e, jm = jour dans le mois
    js = (ja +3) % 7         # js = jour de la semaine. Le d�calage ajout� 
                             #      permet de choisir le jour de d�part
  
    if jm > mois[0][m]:               # �l�ment m de l'�l�ment 0 de la liste
        jm, m = 1, m+1

    print jour[js], jm, mois[1][m]    # �l�ment m de l'�l�ment 1 de la liste
