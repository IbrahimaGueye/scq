#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 16:58:36 2019

@author: igueye
"""
import modules.User as User

default = User.User()

utilisateur = default

continuer = True

on_screen = "principale"

working_function = ""

questions = list()

congrats = [
    "Bravo!",
    "Magnifique!",
    "Super!",
    "Formidable!",
    "Tres bien!",
    "Bien joué!"
]

classes = [
    "2nd",
    "1er",
    "tle"
]

risques = [50, 100, 150, 200]

aide = """
Tapez le numero devant l'option pour la choisir puis appuyez sur "Entrée" pour valider.

"""

apropos = """Sources des Questions et lecons: http://qcm-sciencesphysiques.blogspot.com, www.bac-s.net/quiz\n
Crée par Igueye avec <3 et Python\n\nContacter:\n    Email: ibzero28700@gmail.com\n    Tel: [Something here, lol]        
"""

admin_message = """Il vous faut plus de points pour acceder a ce menu.\n    100pts: privilege 1\n   200pts: privilege 2
\n
"""
