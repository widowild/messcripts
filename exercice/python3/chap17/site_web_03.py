# -*- coding:Utf8 -*-

# Exemple de serveur web acceptant les données d'un formulaire.
# (passage d'arguments via GET/POST).

import cherrypy

class Bienvenue(object):
    def index(self):
        # Formulaire demandant son nom à l'utilisateur :
        return '''
            <form action="salutations" method="GET">
            Bonjour. Quel est votre nom ?
            <input type="text" name="nom" />
            <input type="submit" value="OK"/>
            </form>
        '''
    index.exposed = True

    def salutations(self, nom =None):
        # CherryPy passe les valeurs entrées dans un formulaire comme de
        # simples arguments lors de l'appel de la méthode destinataire de
        # la requête (vous pouvez indifféremment utiliser GET ou POST).
        # Comme d'habitude sous Python, vous pouvez définir des valeurs
        # par défaut pour chaque paramètre. Dans cet exemple, le paramètre
        # "nom" contient par défaut un objet vide. On peut donc vérifier
        # aisément que le nom ait été effectivement entré.

        if nom:
            # Accueil de l'utilisateur :
            return "Bonjour, {}, comment allez-vous ?".format(nom)
        else:
            # Aucun nom n'a été fourni :
            return 'Veuillez svp fournir votre nom <a href="/">ici</a>.'

    salutations.exposed = True

cherrypy.quickstart(Bienvenue(), config ="tutoriel.conf")

