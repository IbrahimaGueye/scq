#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 13:09:28 2019

@author: igueye
"""
import os

import modules.fonctions as fonctions
import modules.menus as menus
import modules.variables as var

os.chdir('modules')

while var.continuer:
    """
    MainLoop...
    """
    if var.utilisateur != var.default:
        # Menu utilisateur
        var.on_screen = "utilisateur"
        fonctions.afficher_menu(menus.menu_utilisateur_txt, menus.menu_utilisateur_funcs)
    else:
        # Menu principal
        var.on_screen = "principale"
        fonctions.afficher_menu(menus.menu_principal_txt, menus.menu_principal_funcs)