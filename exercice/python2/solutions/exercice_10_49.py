# -*- coding: Utf-8 -*-
# Encodage d'un texte dans un dictionnaire

nFich = raw_input('Nom du fichier à traiter : ')
fi = open(nFich, 'r')
# Conversion du fichier en une chaîne de caractères unicode.
# Suivant l'encodage du fichier source, activer l'une ou l'autre ligne :

texte = fi.read().decode("Utf8")	
#texte = fi.read().decode("Latin1")

fi.close()

# On considère que les mots sont des suites de caractères faisant partie
# de la chaîne ci-dessous. Tous les autres sont des séparateurs :

alpha = u"abcdefghijklmnopqrstuvwxyzéèàùçâêîôûäëïöü"

# Construction du dictionnaire :
dico ={}
# Parcours de tous les caractères du texte :
i =0                     # indice du caractère en cours de lecture
im =-1                   # indice du premier caractère du mot
mot = u""                # variable de travail : mot en cours de lecture
for c in texte:
    c = c.lower()        # conversion de chaque caractère en minuscule
    
    if c in alpha:       # car. alphabétique => on est à l'intérieur d'un mot
        mot = mot + c
        if im < 0:       # mémoriser l'indice du premier caractère du mot
            im =i   
    else:                # car. non-alphabétique => fin de mot
        if mot != u"":   # afin d'ignorer les car. non-alphab. successifs
            # pour chaque mot, on construit une liste d'indices :
            if dico.has_key(mot):       # mot déjà répertorié :
                dico[mot].append(im)    # ajout d'un indice à la liste
            else:                       # mot rencontré pour la 1e fois :
                dico[mot] =[im]         # création de la liste d'indices
            mot =u""     # préparer la lecture du mot suivant
            im =-1
    i += 1               # indice du caractère suivant
      
# Affichage du dictionnaire, en clair :
listeMots =dico.items()           # Conversion du dico en une liste de tuples
listeMots.sort()                  # tri alphabétique de la liste
for clef, valeur in listeMots:
    print clef, ":", valeur

