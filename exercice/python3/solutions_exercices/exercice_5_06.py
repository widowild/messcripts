#! /usr/bin/env python
# -*- coding:Utf8 -*-

# Recherche d'un caractère particulier dans une chaîne

# Chaîne fournie au départ :
ch = "Monty python flying circus"
# Caractère à rechercher :
cr = "e"
# Recherche proprement dite :
lc = len(ch)    # nombre de caractères à tester
i = 0           # indice du caractère en cours d'examen
t = 0           # "drapeau" à lever si le caractère recherché est présent 
while i < lc:
    if ch[i] == cr:
        t = 1
    i = i + 1
# Affichage sans saut à la ligne (utilisation de 'end =') :
print("Le caractère", cr, end=' ')
if t == 1:
    print("est présent", end=' ')
else:
    print("est inrouvable", end=' ')
print("dans la chaîne", ch)

