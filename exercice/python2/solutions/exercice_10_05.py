#! /usr/bin/env python
# -*- coding: Utf8 -*-

# Comptage des occurrences d'un caractère donné dans une chaîne

def compteCar(ch, car):
    "trouve l'indice du caractère car dans la chaîne ch"
    ch = ch.decode("Utf8")      # conversion 'string' => 'unicode'
    car = car.decode("Utf8")

    i, nc = 0, 0                # initialisations
    while i < len(ch):
        if ch[i] == car:
            nc = nc + 1         # caractère est trouvé -> on incrémente le compteur
        i = i + 1
    return nc

# Test :
if __name__ == '__main__':
    print compteCar("ananas au jus", "a")
    print compteCar("Gédéon est déjà là", "é")
    print compteCar("Gédéon est déjà là", "à")

