#! /usr/bin/env python
# -*- coding: Latin-1 -*-

# Recherche du plus grand �l�ment d'une liste

# Liste fournie au d�part :
tt = [32, 5, 12, 8, 3, 75, 2, 15]
# Au fur et � mesure du traitement de la liste, on m�morisera dans
# la variable ci-dessous la valeur du plus grand �l�ment d�j� trouv� :
max = 0
# Examen de tous les �l�ments :
i = 0
while i < len(tt):
    if tt[i] > max:
        max = tt[i]         # m�morisation d'un nouveau maximum    
    i = i + 1
# Affichage :
print "Le plus grand �l�ment de cette liste a la valeur", max
