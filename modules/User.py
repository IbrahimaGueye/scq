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

    def __init__(self, nom_utilisateur="", classe="", cookies=None):
        if cookies is None:
            cookies = {}

        self.nom_utilisateur = nom_utilisateur
        self.classe = classe
        self.score = 0
        self.privilege = 0
        self.reponses_cookies = cookies

    # ..............................................................................
    def __repr__(self):
        return "%s; Classe: %s // Score: %d // Privilege: %d\n cookies: %s " % (self.nom_utilisateur, self.classe,
                                                                                self.score, self.privilege,
                                                                                str(self.reponses_cookies))

    # ..............................................................................
    def change_nom_utilisateur(self, nouveau):
        self.nom_utilisateur = nouveau
        print("Nom utilisateur changé a {}".format(nouveau))

    # ..............................................................................
    def reset_compte(self):
        self.score = 0
        self.privilege = 0
        self.reponses_cookies = {}
        print("Compte reinitilaisé")

    # ..............................................................................
    def aug_score(self, value):
        self.score += value

    # ..............................................................................
    def dim_score(self, value):
        self.score -= value
