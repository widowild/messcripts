#! /usr/bin/env python
# -*- coding: Latin-1 -*-

# D�finition d'un serveur r�seau g�rant un syst�me de CHAT simplifi�.
# Utilise les threads pour g�rer les connexions clientes en parall�le.

HOST = '192.168.0.235'
PORT = 40000

import socket, sys, threading

class ThreadClient(threading.Thread):
    '''d�rivation d'un objet thread pour g�rer la connexion avec un client'''
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn
        
    def run(self):
        # Dialogue avec le client :
        nom = self.getName()            # Chaque thread poss�de un nom
        while 1:
            msgClient = self.connexion.recv(1024)
            if msgClient.upper() == "FIN" or msgClient =="":
                break
            message = "%s> %s" % (nom, msgClient)
            print message
            # Faire suivre le message � tous les autres clients :
            for cle in conn_client:
                if cle != nom:          # ne pas le renvoyer � l'�metteur
                    conn_client[cle].send(message)
                    
        # Fermeture de la connexion :
        self.connexion.close()      # couper la connexion c�t� serveur
        del conn_client[nom]        # suppr. son entr�e dans le dictionnaire
        print "Client %s d�connect�." % nom
        # Le thread se termine ici    

# Initialisation du serveur - Mise en place du socket :
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mySocket.bind((HOST, PORT))
except socket.error:
    print "La liaison du socket � l'adresse choisie a �chou�."
    sys.exit()
print "Serveur pr�t, en attente de requ�tes ..."
mySocket.listen(5)

# Attente et prise en charge des connexions demand�es par les clients :
conn_client = {}                # dictionnaire des connexions clients
while 1:    
    connexion, adresse = mySocket.accept()
    # Cr�er un nouvel objet thread pour g�rer la connexion :
    th = ThreadClient(connexion)
    th.start()
    # M�moriser la connexion dans le dictionnaire : 
    it = th.getName()        # identifiant du thread
    conn_client[it] = connexion
    print "Client %s connect�, adresse IP %s, port %s." %\
           (it, adresse[0], adresse[1])
    # Dialogue avec le client :
    connexion.send("Vous �tes connect�. Envoyez vos messages.")
