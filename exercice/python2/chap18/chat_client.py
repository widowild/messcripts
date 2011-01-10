#! /usr/bin/env python
# -*- coding: Latin-1 -*-

# D�finition d'un client r�seau g�rant en parall�le l'�mission
# et la r�ception des messages (utilisation de 2 THREADS).

host = '192.168.0.235'
port = 46000

import socket, sys, threading

class ThreadReception(threading.Thread):
    """objet thread g�rant la r�ception des messages"""
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn           # r�f. du socket de connexion
        
    def run(self):
        while 1:
            message_recu = self.connexion.recv(1024)
            print "*" + message_recu + "*"
            if message_recu =='' or message_recu.upper() == "FIN":
                break
        # Le thread <r�ception> se termine ici.
        # On force la fermeture du thread <�mission> :
        th_E._Thread__stop()
        print "Client arr�t�. Connexion interrompue."
        self.connexion.close()
    
class ThreadEmission(threading.Thread):
    """objet thread g�rant l'�mission des messages"""
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn           # r�f. du socket de connexion
        
    def run(self):
        while 1:
            message_emis = raw_input()
            self.connexion.send(message_emis)

# Programme principal - �tablissement de la connexion :
connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    connexion.connect((host, port))
except socket.error:
    print "La connexion a �chou�."
    sys.exit()    
print "Connexion �tablie avec le serveur."
            
# Dialogue avec le serveur : on lance deux threads pour g�rer
# ind�pendamment l'�mission et la r�ception des messages :
th_E = ThreadEmission(connexion)
th_R = ThreadReception(connexion)
th_E.start()
th_R.start()
