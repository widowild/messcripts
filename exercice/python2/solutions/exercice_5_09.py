#! /usr/bin/env python
# -*- coding: Latin-1 -*-

# Inversion d'une cha�ne de caract�res

# Cha�ne fournie au d�part :
ch = "zorglub"
lc = len(ch)    # nombre de caract�res total
i = lc - 1      # le traitement commencera � partir du dernier caract�re
nch = ""        # nouvelle cha�ne � construire (vide au d�part)
while i >= 0:
    nch = nch + ch[i]
    i = i - 1    
# Affichage :
print nch   
