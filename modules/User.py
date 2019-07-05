#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 13:08:03 2019

@author: igueye
"""


class User:
    """
    Classe utilisateur definit par son nom d'utilsateur et sa classe.
    L'attribut privilege determinera l'accesibilite a certaines fonctionalites.
    Et le score pourra augmenter ou diminuer selon certains cas.
    
    """

    def __init__(self, nom_utilisateur="", classe=""):
        self.nom_utilisateur = nom_utilisateur
        self.classe = classe
        self.score = 0
        self.privilege = 0

    # ..............................................................................
    def __repr__(self):
        return "{}; Classe: {} // Score: {} // Privilege: {} \
                ".format(self.nom_utilisateur, self.classe, self.score, self.privilege)

    # ..............................................................................
    def change_nom_utilisateur(self, nouveau):
        self.nom_utilisateur = nouveau
        print("Nom utilisateur changé a {}".format(nouveau))

    # ..............................................................................
    def reset_compte(self):
        self.score = 0
        self.privilege = 0
        print("Compte reinitilaisé")

    # ..............................................................................
    def aug_score(self, value):
        self.score += value

    # ..............................................................................
    def dim_score(self, value):
        self.score -= value
