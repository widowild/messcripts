# -*- coding: Utf-8 -*-
# Encodage d'un texte dans un dictionnaire
# Suivant l'encodage du fichier source, activer l'une ou l'autre ligne :
encodage ="Latin-1"
#encodage ="Utf-8"

nFich = input('Nom du fichier à traiter ({}) : '.format(encodage))
# Conversion du fichier en une chaîne de caractères :
fi = open(nFich, 'r', encoding =encodage)
texte = fi.read()
fi.close()

# On considère que les mots sont des suites de caractères faisant partie
# de la chaîne ci-dessous. Tous les autres sont des séparateurs :
alpha = "abcdefghijklmnopqrstuvwxyzéèàùçâêîôûäëïöü"

# Construction du dictionnaire :
dico ={}
# Parcours de tous les caractères du texte :
i =0                     # indice du caractère en cours de lecture
im =-1                   # indice du premier caractère du mot
mot = ""                 # variable de travail : mot en cours de lecture
for c in texte:
    c = c.lower()        # conversion de chaque caractère en minuscule
    
    if c in alpha:       # car. alphabétique => on est à l'intérieur d'un mot
        mot = mot + c
        if im < 0:       # mémoriser l'indice du premier caractère du mot
            im =i   
    else:                # car. non-alphabétique => fin de mot
        if mot != "":    # afin d'ignorer les car. non-alphab. successifs
            # pour chaque mot, on construit une liste d'indices :
            if mot in dico:             # mot déjà répertorié :
                dico[mot].append(im)    # ajout d'un indice à la liste
            else:                       # mot rencontré pour la 1e fois :
                dico[mot] =[im]         # création de la liste d'indices
            mot =""      # préparer la lecture du mot suivant
            im =-1
    i += 1               # indice du caractère suivant
      
# Affichage du dictionnaire, en clair :
listeMots =list(dico.items())     # Conversion du dico en une liste de tuples
listeMots.sort()                  # tri alphabétique de la liste
for clef, valeur in listeMots:
    print(clef, ":", valeur)

