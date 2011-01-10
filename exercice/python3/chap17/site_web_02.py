# -*- coding:Utf8 -*-

# Exemple de serveur web ne délivrant plusieurs pages simples.

import cherrypy

class MonSiteWeb(object):

    def index(self):
        # Renvoi d'une page HTML contenant un lien vers une autre page
        # (laquelle sera produite par une autre méthode) :
        return '<h2>Veuillez <a href="unMessage">cliquer ici</a> '\
        "pour accéder à une information d'importance cruciale.</h2>"
    index.exposed = True

    def unMessage(self):
        # Le message incontournable :
        return "<h1>La programmation, c'est génial !</h1>"
    unMessage.exposed = True

cherrypy.quickstart(MonSiteWeb(), config ="tutoriel.conf")
