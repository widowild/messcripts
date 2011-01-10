# -*- coding:Utf8 -*-

# Exemple de serveur web ne délivrant qu'une page simple.

import cherrypy

class MonSiteWeb(object):
    # Classe produisant des objets gestionnaires de requêtes HTTP."

    def index(self):
        # Cherrypy invoquera cette méthode comme URL racine (/).
        # Sa valeur de retour sera la page HTML renvoyée au client :
        return "<h1>Bonjour à tous !</h1>"

    # Les méthodes doivent être "exposées" pour être accessibles via le web.
    # Pour ce faire, elles doivent être pourvues d'un attribut "exposed"
    # contenant une valeur booléenne "vraie" :
    index.exposed = True

    # Remarquons que les méthodes qui ne sont pas explicitement exposées ainsi
    # sont invisibles poour les clients. Vous pouvez donc y installer divers
    # traitements "internes" à votre application.

# Au démarrage, CherryPy doit disposer d'un objet racine, dont les méthodes
# seront des gestionnaires de requêtes HTTP renvoyant les pages à afficher
# comme valeurs de retour. Cas particulier : une requête HTTP invoquant
# l'URL racine : '/' est considérée comme équivalante à une requête invoquant
# l'URL /index, et produit donc un appel de la méthode index() de l'objet :

cherrypy.quickstart(MonSiteWeb(), config ="tutoriel.conf")


