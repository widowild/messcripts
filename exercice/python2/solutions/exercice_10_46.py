#! /usr/bin/env python
# -*- coding: Latin-1 -*-

# �change des cl�s et des valeurs dans un dictionnaire

def inverse(dico):
    "Construction d'un nouveau dico, pas � pas"
    dic_inv ={} 
    for cle in dico:
        item = dico[cle]  
        dic_inv[item] = cle
        
    return dic_inv

# programme test :

dico = {'Computer':'Ordinateur',
        'Mouse':'Souris',
        'Keyboard':'Clavier',
        'Hard disk':'Disque dur',
        'Screen':'Ecran'}

print dico
print inverse(dico)