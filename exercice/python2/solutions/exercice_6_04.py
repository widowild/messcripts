#! /usr/bin/env python
# -*- coding: Latin-1 -*-

# Entr�e d'�l�ments dans une liste

tt = []             # Liste � compl�ter (vide au d�part)
ch = "start"        # valeur quelconque (mais non nulle) 
while ch != "":
    print "Veuillez entrer une valeur : "
    ch = raw_input()
    if ch != "":
        tt.append(float(ch))        # variante : tt.append(ch)    

# affichage de la liste :
print tt
