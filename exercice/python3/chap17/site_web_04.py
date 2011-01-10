# -*- coding:Utf8 -*-

# Exemple montrant comment créer une structure de site web comportant un
# certain nombre de pages hiérachisées, gérées par l'intermédiaire d'un
# ensembles de classes, hiérachisées elles aussi.

import cherrypy

class HomePage(object):
    def __init__(self):
        # Les objets gestionnaires de requêtes peuvent instancier eux-mêmes
        # d'autres gestionnaires "esclaves", et ainsi de suite :
        self.maxime = MaximeDuJour()
        self.liens = PageDeLiens()
        # L'instanciation d'objets gestionnaires de requêtes peut bien entendu
        # être effectuée à n'importe quel niveau du programme.

    def index(self):
        return '''
            <h3>Site des adorateurs du Python royal - Page d'accueil.</h3>
            <p>Veuillez visiter nos rubriques géniales :</p>
            <ul>
                <li><a href="/entreNous">Restons entre nous</a></li>
                <li><a href="/maxime/">Une maxime subtile</a></li>
                <li><a href="/liens/utiles">Des liens utiles</a></li>
            </ul>
        '''
    index.exposed = True

    def entreNous(self):
        return '''
            Cette page est produite à la racine du site.<br />
            [<a href="/">Retour</a>]
        '''
    entreNous.exposed =True

class MaximeDuJour(object):
    def index(self):
        return '''
            <h3>Il existe 10 sortes de gens : ceux qui comprennent
            le binaire, et les autres !</h3>
            <p>[<a href="../">Retour</a>]</p>
        '''
    index.exposed = True

class PageDeLiens(object):
    def __init__(self):
        self.extra = LiensSupplementaires()

    def index(self):
        return '''
        <p>Page racine des liens (sans utilité réelle).</p>
        <p>En fait, les liens <a href="utiles">sont plutôt ici</a></p>
        '''
    index.exposed = True

    def utiles(self):
        # Veuillez noter comment le lien vers les autres pages est défini :
        # on peut dans procéder de manière absolue ou relative (comme ici).
        return '''
            <p>Quelques liens utiles :</p>
            <ul>
                <li><a href="http://www.cherrypy.org">Site de CherryPy</a></li>
                <li><a href="http://www.python.org">Site de Python</a></li>
            </ul>
            <p>D'autres liens utiles vous sont proposés
            <a href="./extra/"> ici </a>.</p>
            <p>[<a href="../">Retour</a>]</p>
        '''
    utiles.exposed = True

class LiensSupplementaires(object):
    def index(self):
        # Notez le lien relatif pour retourner à la page maîtresse :
        return '''
            <p>Encore quelques autres liens utiles :</p>
            <ul>
                <li><a href="http://pythomium.net">Le site de l'auteur</a></li>
                <li><a href="http://ubuntu-fr.org">Ubuntu : le must</a></li>
            </ul>
            <p>[<a href="../">Retour à la page racine des liens</a>]</p>
        '''
    index.exposed = True

racine = HomePage()
cherrypy.quickstart(racine, config ="tutoriel.conf")

