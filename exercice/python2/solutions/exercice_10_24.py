#! /usr/bin/env python
# -*- coding:Utf-8 -*-

# Fusion de lignes pour former des phrases

fiSource = raw_input("Nom du fichier à traiter (Latin-1) : ")
fiDest = raw_input("Nom du fichier destinataire (Utf-8) : ")
fs = open(fiSource, 'r')
fd = open(fiDest, 'w')

# On lit d'abord la première ligne :
ch1 = fs.readline().decode("Latin1")
# On lit ensuite les suivantes, en les fusionnant si nécessaire :
while 1:
    ch2 = fs.readline().decode("Latin1")
    if not ch2:           # Rappel : une chaîne vide est considérée 
        break             # comme "fausse" dans les tests
    # Si la chaîne lue commence par une majuscule, on transcrit
    # la précédente dans le fichier destinataire, et on la
    # remplace par celle que l'on vient de lire :
    if ch2[0] in u"ABCDEFGHIJKLMNOPQRSTUVWXYZÀÂÉÈÊËÎÏÔÙÛÇ":
        fd.write(ch1.encode("Utf8"))
        ch1 = ch2
    # Sinon, on la fusionne avec la précédente, en veillant à en
    # enlever au préalable le ou les caractère(s) de fin de ligne.
    # (Pour les fichiers texte sous Windows, il faut en enlever 2) :
    else:
        ch1 = ch1[:-1] + " " + ch2
        
# Attention : ne pas oublier de transcrire la dernière ligne :
fd.write(ch1.encode("Utf8"))
fd.close()    
fs.close()
