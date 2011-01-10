#! /usr/bin/env python
# -*- coding:Utf-8 -*-

from tkinter import *

# === Définition de quelques gestionnaires d'événements :

def start_it():
    "Démarrage de l'animation"
    global flag
    if flag ==0:
        flag =1
        move()

def stop_it():
    "Arrêt de l'animation"
    global flag
    flag =0
    
def move():
    "Animation du serpent par récursivité"
    global flag
    # Principe du mouvement opéré : on déplace le carré de queue, dont les
    # caractéristiques sont mémorisées dans le premier élément de la liste
    # <serp>, de manière à l'amener en avant du carré de tête, dont les
    # caractéristiques sont mémorisées dans le dernier élément de la liste.
    # On définit ainsi un nouveau carré de tête pour le serpent, dont on
    # mémorise les caractéristiques en les ajoutant à la liste.
    # Il ne reste plus qu'à effacer alors le premier élément de la liste,
    # et ainsi de suite ... :
    c = serp[0]             # extraction des infos concernant le carré de queue
    cq, xq, yq = c[0], c[1], c[2]        # réf. et coordonnées de ce carré
    l =len(serp)            # longueur actuelle du serpent (= n. de carrés)
    c = serp[l-1]           # extraction des infos concernant carré de tête
    ct, xt, yt = c[0], c[1], c[2]        # réf. et coordonnées de ce carré
    # Effectuer le déplacement proprement dit :
    xq, yq = xt+cc, yt            # coord. du nouveau carré de tête
    can.coords(cq, xq, yq, xq+cc, yq+cc)
    serp.append([cq, xq, yq])     # mémorisation du nouveau carré de tête
    del(serp[0])                  # effacement retrait de la liste
    # Appel récursif de la fonction par elle-même (=> boucle d'animation) : 
    if flag >0:
        fen.after(50, move)
    
# === Programme principal : ========

# Création de l'espace de jeu (fenêtre, canevas, boutons ...) :
fen =Tk()
can =Canvas(fen, bg ='dark gray', height =500, width =500)
can.pack(padx =10, pady =10)
bou1 =Button(fen, text="Start", width =10, command =start_it)
bou1.pack(side =LEFT)
bou2 =Button(fen, text="Stop", width =10, command =stop_it)
bou2.pack(side =LEFT)

# Création du serpent initial (= ligne de 5 carrés).
# On mémorisera les infos concernant les carrés créés dans une liste de listes :
serp =[]                        # liste vide
x, y, cc = 100, 100, 10         # coordonnées et coté du premier carré
flag =0                         # commutateur pour l'animation
# Création et mémorisation des 5 carrés : le dernier (à droite) est la tête.
i =0
while i <5:
    carre =can.create_rectangle(x, y, x+cc, y+cc, fill="red")
    # Pour chaque carré, on mémorise une petite sous-liste contenant
    # 3 éléments : la référence du carré et ses coordonnées de base :
    serp.append([carre, x, y])
    x =x+cc                     # le carré suivant sera un peu plus à droite
    i =i+1

fen.mainloop()
