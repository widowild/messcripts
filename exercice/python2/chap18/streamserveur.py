#! /usr/bin/env python
# -*- coding: Latin-1 -*-

# D�finition d'un serveur r�seau rudimentaire
# Ce serveur attend la connexion d'un client

import socket, sys

HOST = '192.168.0.235'
PORT = 50000
counter =0          # compteur de connexions actives

# 1) cr�ation du socket :
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2) liaison du socket � une adresse pr�cise :
try:
    mySocket.bind((HOST, PORT))
except socket.error:
    print "La liaison du socket � l'adresse choisie a �chou�."
    sys.exit

while 1:
    # 3) Attente de la requ�te de connexion d'un client :
    print "Serveur pr�t, en attente de requ�tes ..."
    mySocket.listen(2)

    # 4) Etablissement de la connexion :
    connexion, adresse = mySocket.accept()
    counter +=1
    print "Client connect�, adresse IP %s, port %s" % (adresse[0], adresse[1])

    # 5) Dialogue avec le client :
    connexion.send("Vous �tes connect� au serveur Marcel. Envoyez vos messages.")
    msgClient = connexion.recv(1024)
    while 1:
        print "C>", msgClient
        if msgClient.upper() == "FIN" or msgClient =="":
            break
        msgServeur = raw_input("S> ")
        connexion.send(msgServeur)
        msgClient = connexion.recv(1024)

    # 6) Fermeture de la connexion :
    connexion.send("fin")
    print "Connexion interrompue."
    connexion.close()

    ch = raw_input("<R>ecommencer <T>erminer ? ")
    if ch.upper() =='T':
        break
        
    
