#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 23:41:11 2019

@author: igueye
"""

from . import fonctions

menu_principal_txt = [
    "Creer un nouveau profile",
    "Se connecter",
    "Afficher l'aide",
    "A propos",
    "Quitter"
]

menu_principal_funcs = [
    fonctions.creer_profile,
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
    "Menu Admin",
    "Se deconnecter",
    "A propos",
    "Quitter"
]

menu_utilisateur_funcs = [
    fonctions.jouer,
    fonctions.voir_stats,
    fonctions.aide,
    fonctions.aff_parametres,
    fonctions.aff_menu_admin,
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

menu_admin1_txt = [
    "Ajouter une question a un quizz",
    "Modifier un parametre d'une question",
    "Supprimer un parametre d'une question"
    "Retour"

]

menu_admin1_funcs = [
    fonctions.check_ajouter_question,
    fonctions.check_modifier_question
]
