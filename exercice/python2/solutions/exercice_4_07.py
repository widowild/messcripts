# -*- coding:Latin-1 -*-

# affichage des 20 premiers termes de la table par 7,
# avec signalement des multiples de 3 :

i = 1               # compteur : prendra successivement les valeurs de 1 � 20
while i < 21:
    # calcul du terme � afficher :
    t = i * 7
    # affichage sans saut � la ligne (utilisation de la virgule) :
    print t,
    # ce terme est-il un multiple de 3 ? (utilisation de l'op�rateur modulo) :
    if t % 3 == 0:
        print "*",      # affichage d'une ast�risque dans ce cas
    i = i + 1           # incr�mentation du compteur dans tous les cas   