#! /usr/bin/env python
# -*- coding: Latin-1 -*-

# Insertion d'un caract�re d'espacement dans une cha�ne

# Cha�ne fournie au d�part :
ch = "Gaston"
# Caract�re � ins�rer :
cr = "*"
# Le nombre de caract�res � ins�rer est inf�rieur d'une unit� au
# nombre de caract�res de la cha�ne. On traitera donc celle-ci �
# partir de son second caract�re (en omettant le premier).
lc = len(ch)    # nombre de caract�res total
i = 1           # indice du premier caract�re � examiner (le second, en fait)
nch = ch[0]     # nouvelle cha�ne � construire (contient d�j� le premier car.)
while i < lc:
    nch = nch + cr + ch[i]
    i = i + 1    
# Affichage :
print nch
