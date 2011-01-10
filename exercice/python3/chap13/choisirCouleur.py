#! /usr/bin/env python
# -*- coding:Utf8 -*-

# Démo de l'utilitaire "colorchooser" de tkinter

from tkinter import colorchooser

input("Prêt à choisir une couleur : frappez <enter>")

couleur = colorchooser.askcolor()

print("couleur choisie", couleur)
