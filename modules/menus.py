#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 23:41:11 2019

@author: igueye
"""

from . import fonctions

menu_principal_txt = [
    "Creer un compte",
    "Se connecter",
    "Afficher l'aide",
    "A propos",
    "Quitter"
]

menu_principal_funcs = [
    fonctions.creer_compte,
    fonctions.connecter,
    fonctions.aide,
    fonctions.apropos,
    fonctions.quitter
]

menu_utilisateur_txt = [
    "Jouer",
    "Voir les stats",
    "Afficher l'aide",
    "Parametres du compte",
    "Se deconnecter",
    "A propos",
    "Quitter"
]

menu_utilisateur_funcs = [
    fonctions.jouer,
    fonctions.voir_stats,
    fonctions.aide,
    fonctions.aff_parametres,
    fonctions.se_deconnecter,
    fonctions.apropos,
    fonctions.quitter
]

menu_parametres_txt = [
    "Changer le nom d'utilisateur",
    "Reinitialiser le compte",
    "Afficher l'aide",
    "Supprimer le compte",
    "Retour",
]

menu_parametres_funcs = [
    fonctions.change_nom_utilisateur,
    fonctions.reinitialiser_compte,
    fonctions.aide,
    fonctions.supprimer_compte,
    fonctions.retour
]
