#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: igueye
"""
import pickle


def ajouter_infos(fichier, info):
    """
    Fonction chargée d'ajouter un info/tip
    """
    with open("..//data//infos//%s" % fichier, "rb") as file:
        lecteur = pickle.Unpickler(file)
        infos = lecteur.load()

    with open("..//data//infos//%s" % fichier, "wb") as file:
        writer = pickle.Pickler(file)
        infos.append(info)
        writer.dump(infos)


def modifier_info(fichier):
    """
    Fonction chargée de modifier un info/tip
    """
    i = 1
    with open("..//data//infos//%s" % fichier, "rb") as file:
        reader = pickle.Unpickler(file)
        liste_infos = reader.load()

    for info in liste_infos:
        print("%d: Modifier (%s)\n" % (i, info))
        i += 1
    print("Q pour annuler")
    chx = input(">>> ")

    if chx.capitalize() != "Q":
        chx = int(chx)
        liste_infos.pop((chx - 1))

        changements = input("Entrez les changements: ")
        liste_infos.append(changements)

        with open("..//data//infos//%s" % fichier, "wb") as file:
            writer = pickle.Pickler(file)
            writer.dump(liste_infos)
        print("Changements effectué!")


def supprimer_info(fichier):
    """
    Fonction chargée de supprimer un info/tip
    """
    i = 1
    with open("..//data//infos//%s" % fichier, "rb") as file:
        reader = pickle.Unpickler(file)
        liste_infos = reader.load()

    for info in liste_infos:
        print("%d: Supprimer (%s)\n" % (i, info))
        i += 1
    print("Q pour annuler")

    chx = input(">>> ")

    if chx.capitalize() != "Q":
        chx = int(chx)

        if len(liste_infos) > 1:
            liste_infos.pop((chx - 1))

            with open("..//data//infos//%s" % fichier, "wb") as file:
                writer = pickle.Pickler(file)
                writer.dump(liste_infos)
            print("Changements effectué!")

        else:
            print("Changements impossible")
