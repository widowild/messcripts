#! /usr/bin/env python
# -*- coding: Latin-1 -*-

# Recherche d'un caract�re particulier dans une cha�ne

# Cha�ne fournie au d�part :
ch = "Monty python flying circus"
# Caract�re � rechercher :
cr = "e"
# Recherche proprement dite :
lc = len(ch)    # nombre de caract�res � tester
i = 0           # indice du caract�re en cours d'examen
t = 0           # "drapeau" � lever si le caract�re recherch� est pr�sent 
while i < lc:
    if ch[i] == cr:
        t = 1
    i = i + 1    
# Affichage :
print "Le caract�re", cr,        
if t == 1:
    print "est pr�sent",
else:
    print "est inrouvable",
print "dans la cha�ne", ch        

