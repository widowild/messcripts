# -*- coding:Utf8 -*-

"""
Sessions
Mémoriser des informations de session dans une application CherryPy
est très facile. Pour chaque utilisateur qui se connecte, vous disposez
automatiquement d'un dictionnaire de session nommé cherrypy.session
dans lequel vous pouvez stocker pratiquement n'importe quel type de donnée.
"""

import cherrypy

class CompteurAcces(object):
    def index(self):
        # Exemple simplissime : incrémentation d'un compteur d'accès.
        # On commence par récupérer le total actuel du comptage :
        count = cherrypy.session.get('count', 0)
        # ... on l'incrémente :
        count += 1
        # ... on mémorise sa nouvelle valeur dans le dictionnaire de session :
        cherrypy.session['count'] = count
        # ... et on affiche le compte actuel :
        return '''
            Durant la présente session, vous avez déjà visité
            cette page {} fois ! Votre vie est bien excitante !
        '''.format(count)
    index.exposed = True

cherrypy.quickstart(CompteurAcces(), config='tutoriel.conf')