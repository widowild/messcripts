#! /usr/bin/env python
# -*- coding: Latin-1 -*-

# Notes de travaux scolaires

notes = []           # liste � construire  
n = 2                # valeur positive quelconque pour initier la boucle
while n >= 0 :
    print "Entrez la note suivante, s.v.p. : ",
    n = float(raw_input())      # conversion de l'entr�e en un nombre r�el
    if n < 0 :
        print "OK. Termin�."
    else:    
        notes.append(n)         # ajout d'une note � la liste
        # Calculs divers sur les notes d�j� entr�es :
        # valeurs minimale et maximale + total de toutes les notes. 
        min = 500               # valeur sup�rieure � toute note
        max, tot, i = 0, 0, 0        
        nn = len(notes)         # nombre de notes d�j� entr�es
        while i < nn:
            if notes[i] > max:
                max = notes[i]
            if notes[i] < min:
                min = notes[i]
            tot = tot + notes[i]
            moy = tot/nn
            i = i + 1
        print nn, "notes entr�es. Max =", max, "Min =", min, "Moy =", moy
