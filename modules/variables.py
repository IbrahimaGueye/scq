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

infos_utilisateur = [
    ""
]

infos_generales = [
    "New Updates coming soon..."
]

aide = """
Tapez le numero devant l'option pour la choisir puis appuyez sur "Entrée" pour valider.

"""