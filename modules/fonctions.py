#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 13:07:20 2019

@author: igueye

Todo: Add a true or false sort of quizz
"""

import os
import pickle
import random
import time
#a comment


from . import User as User
from . import variables as var


def infos():
    """
    Fonction chargée de.. charger les elements de la barre d'info/tip
    """
    if var.on_screen == "principale":
        try:
            with open("..//data//infos//principale", "rb") as file:
                lecteur = pickle.Unpickler(file)
                infos = lecteur.load()

            return random.choice(infos)
        except:
            return "Une erreur est survenu ici..."

    elif var.on_screen == "utilisateur":
        try:
            with open("..//data//infos//%s" % var.utilisateur.classe, "rb") as file:
                lecteur = pickle.Unpickler(file)
                infos = lecteur.load()
            return f'Le saviez vous?: {random.choice(infos)}'

        except:
            return "Une erreur est survenu ici..."

    else:
        return " "


def barre_infos():
    """
    Juste pour la deco...
    """
    print("===== Utilisateur: %s ===== Score: %d pts\n" % (var.utilisateur.nom_utilisateur.capitalize(),
                                                           var.utilisateur.score))

    print("=" * 80, "\n")
    print(infos(), "\n")
    print("=" * 80, "\n")
    print("-----> %s\n\n" % var.working_function)


def clear_screen():
    """
    Fonction chargée de "nettoyer" l'ecran
    """
    name = os.name
    # for windows
    if name == 'nt':
        _ = os.system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')

    if var.continuer:
        barre_infos()


def afficher_menu(txt, funcs):
    """
    Fonction chargée de gerer un menu, affichage et redirection vers les autres fonctions
    """
    clear_screen()
    i = 1
    for elt in txt:
        print("{}: {} \n".format(i, elt))
        i += 1

    chx = input(">>> ")

    try:
        chx = int(chx)

    except ValueError:
        clear_screen()
        print("Veillez choisir un numero, (3 pour voir l'aide)\n")
        input("<<< Retour")
        afficher_menu(txt, funcs)

    else:
        try:
            var.working_function = txt[int(chx) - 1]
            funcs[int(chx) - 1]()  # on appelle la fonction correspondante
            var.working_function = ""
        except IndexError:
            clear_screen()
            print("Veillez choisir un numero disponible (3 pour voir l'aide)")
            input("<<< Retour")
            afficher_menu(txt, funcs)

    clear_screen()


def creer_compte(nom_utilisateur=""):
    """
    Fonction chargée de creer un un nouveau utilisateur.
    """
    cookies = {}  #

    clear_screen()

    if nom_utilisateur == "":
        nom_utilisateur = input("Choisissez un nom d'utilisateur (Q pour revenir au menu): ")

    if nom_utilisateur.capitalize() != "Q":
        if len(nom_utilisateur) < 6:
            print("Nom utilisateur invalide. Il doit au moins avoir 6 caracteres, choisissez encore...\n")
            input("<<< retour")
            creer_compte()

        else:
            with open("..//data//users//users", "rb") as fichier:
                lecteur = pickle.Unpickler(fichier)
                users = lecteur.load()

                if nom_utilisateur in users:
                    clear_screen()
                    print("Ce nom est deja pris")
                    time.sleep(2)
                    creer_compte()
                else:
                    clear_screen()
                    print("Nom utisateur valide\n\n")

                    classe = input("Maintenant dites nous votre classe(2nd, 1er ou tle): ")

                    if classe in var.classes:
                        # Creations des cookies de questions
                        with open("..//data//questions//%s//liste_lecons" % classe, "rb") as file:
                            reader = pickle.Unpickler(file)
                            lecons = reader.load()

                        for lecon in lecons:
                            cookies[lecon] = []

                        # on enregistre l'utilistateur
                        utilisateur = User.User(nom_utilisateur, classe, cookies)

                        with open("..//data//users//" + nom_utilisateur, "wb") as usr:
                            writer = pickle.Pickler(usr)
                            writer.dump(utilisateur)

                        users.append(nom_utilisateur)

                        with open("..//data//users//users", "wb") as fd:
                            writer = pickle.Pickler(fd)
                            writer.dump(users)

                        clear_screen()
                        print("Compte crée avec succes\n")
                        print("Bienvenue, %s" % nom_utilisateur.capitalize())
                        time.sleep(2)
                        connecter(nom_utilisateur)

                    else:
                        clear_screen()
                        print("Classe invalide, choisissez encore\n")
                        input("<<< Retour ")
                        creer_compte(nom_utilisateur)

    else:
        pass


def connecter(nom_utilisateur=""):
    """
    Fonction chargée de connecter un utilisateur
    """
    clear_screen()
    with open("..//data//users//users", "rb") as fichier:
        lecteur = pickle.Unpickler(fichier)
        users = lecteur.load()
        print("Utilisateurs enregistrés:\n")

        for user in users:
            print("%s (%s)" % (user.capitalize(), user), end=', ')

        print("\n")

    if nom_utilisateur == "":
        nom_utilisateur = input("Nom utilisateur ('Q' pour revenir au menu): ")

    if nom_utilisateur.capitalize() != "Q":
        with open("..//data//users//users", "rb") as fichier:
            lecteur = pickle.Unpickler(fichier)
            users = lecteur.load()

            if nom_utilisateur in users:
                with open("..//data//users//" + nom_utilisateur, "rb") as usr:
                    lecteur = pickle.Unpickler(usr)
                    new_utilisateur = lecteur.load()

                clear_screen()
                print("Bon retour, %s\n" % nom_utilisateur.capitalize())
                input("Continuer >>> ...")

                var.utilisateur = new_utilisateur

            else:
                chx = input("Cet utilisateur n'existe pas encore, voulez vous le creer (O/N): ")
                if chx.capitalize() != "N":
                    creer_compte(nom_utilisateur)
    else:
        pass

def save():
    """
    Fonction chargée de Sauvegarder les infos utilisateur

    """
    clear_screen()
    print("Enregistrement des données...\n")
    time.sleep(0.5)

    # Ne sauvegarder que quand on a un utilisateur connecté
    if var.utilisateur != var.default:
        with open("..//data//users//%s" % var.utilisateur.nom_utilisateur, "wb") as usr:
            writer = pickle.Pickler(usr)
            writer.dump(var.utilisateur)
    else:
        pass

    print("Enregistrés avec succés!")
    time.sleep(0.5)


def aide():
    """
    Fonction chargée d'afficher l'aide d'un menu
    :return none:
    """
    clear_screen()
    print(var.aide)
    input("<<< Retour")


def apropos():
    clear_screen()
    print(var.apropos)
    input("<<< Retour")


def quitter():
    """
    Fonction appellée quand on quitte le jeu
    :return:
    """
    clear_screen()

    chx = input("Etes vous sur de vouloir quitter (O/N) ?: ")

    if chx.capitalize() != "N":
        save()
        print("A la prochaine!!")
        var.continuer = False

# ................Fonctions accessibles seulement apres connection..............

def aff_parametres():
    """
    Fonction chargée d'afficher le menu parametre
    :return:
    """
    from . import menus
    afficher_menu(menus.menu_parametres_txt, menus.menu_parametres_funcs)


def retour():
    """
    Nothing to do here, just pass and go back to user's menu
    :return:
    """
    pass


def voir_stats():
    """
    Fonctions chargée d'afficher les infos utilisateur
    :return:
    """
    clear_screen()
    print("Nom utilisateur: %s\nClasse: %s\nScore: %d\nPrivilege: Nv %d\n" % (var.utilisateur.nom_utilisateur,
                                                                              var.utilisateur.classe,
                                                                              var.utilisateur.score,
                                                                              var.utilisateur.privilege))

    input("<<< Retour")


def se_deconnecter():
    """
    Fonction chargée de deconnecter l'utilisateur
    """
    clear_screen()
    print("A la prochaine!\n")
    input("<<< Sortir... ")
    var.utilisateur = var.default
    var.on_screen = "principale"
    clear_screen()


def reinitialiser_compte():
    """
    Fonction chargée de reinitialiser les données de l'utilisateur
    """
    clear_screen()
    chx = input("Etes vous sur de vouloir reinitialiser votre compte(O/N): ")

    if chx.capitalize() != "N":
        var.utilisateur.reset_compte()
        save()


def change_nom_utilisateur():
    clear_screen()
    nouveau = input("Choisissez un nouveau nom d'utilisateur: ")

    chx = input("Confirmer le changement(O/N): ")
    if chx.capitalize() != "N":
        var.utilisateur.change_nom_utilisateur(nouveau)
        save()


def supprimer_compte():
    """
    Fonction chargée de supprimer un utilisateur
    """
    clear_screen()
    chx = input("Etes vous sur de vouloir supprimer votre compte(O/N): ")

    if chx.capitalize() != 'N':
        with open("..//data//users//users", "rb") as fichier:
            lecteur = pickle.Unpickler(fichier)
            users = lecteur.load()
            users.remove(var.utilisateur.nom_utilisateur)

        with open("..//data//users//users", "wb") as fd:
            writer = pickle.Pickler(fd)
            writer.dump(users)

        os.remove("..//data//users//%s" % var.utilisateur.nom_utilisateur)
        se_deconnecter()


def init_question(classe, lecon):
    """
    Fonction chargée de charger (lol) et de retourner une liste de question specifique selon la matiere
    et la classe.

    :param lecon:
    :param classe: matiere:
    :return une liste:
    """

    with open("..//data//questions//%s//%s" % (classe, lecon), "rb") as fichier:
        lecteur = pickle.Unpickler(fichier)
        questions = lecteur.load()

        for elt in var.utilisateur.reponses_cookies[lecon]:
            questions.pop(elt)

        return questions


def poser_question(questions, lecon):
    """
    Fonction chargée de poser une question parmi la liste donnée en parametre et de le supprimer de la liste
    :param questions:
    :return questions sans la question choisie:
    """
    clear_screen()
    print("Questions sur %s\n" % lecon)

    q_id = random.randrange(len(questions))
    risque = random.choice(var.risques)  # Points perdus ou gagnés

    question_choisie = questions[q_id]  # La question choisie parmi la liste donnée.
    right_answer = question_choisie[1]  # La bonne reponse.
    answers = question_choisie[1:-1]  # liste des reponses
    explications = question_choisie[-1]  # les explications

    random.shuffle(answers)

    # On pose la question
    print("===== Question id: %d ===== Risque: %d\n\n" % (q_id, risque))
    print("%s\n\n" % question_choisie[0])

    i = 1

    for answer in answers:
        print("{}: {} \n".format(i, answer))
        i += 1

    user_input = int(input("Choisissez un numero >>> "))

    clear_screen()
    print("===== Question id: %d\n\nQuestion: %s" % (q_id, question_choisie[0]))

    if answers[user_input - 1] == right_answer:
        var.utilisateur.aug_score(risque)
        print("\n%s, points +%d\n" % (random.choice(var.congrats), risque))
        # On ajoute la question a la liste des questions trouvées...
        var.utilisateur.reponses_cookies[lecon].append(q_id)


    else:
        var.utilisateur.dim_score(risque)
        print("\nDésolé, la bonne réponse est:\n\n      %s, points -%d \n\n" % (right_answer, risque))

    print(explications, "\n" * 2)

    questions.pop(q_id)

    return questions


def jouer():
    """
    Fonction chargée de controler une partie

    """
    i = 1
    on_play = True

    clear_screen()

    with open("..//data//questions//%s//liste_lecons" % var.utilisateur.classe, "rb") as file:
        reader = pickle.Unpickler(file)
        lecons = reader.load()

    print("Voici les lecons disponibles:\n")

    for lecon in lecons:
        print("%d: %s" % (i, lecon))
        i += 1
    print("\n")

    chx = input("Sur quelle lecon souhaitez-vous travaillez?: ")

    try:
        chx = int(chx)
        lecon = lecons[(chx - 1)]

    except ValueError:
        clear_screen()
        print("Veillez choisir un numero\n")
        input("<<< Retour")
        jouer()

    else:
        try:
            var.questions = init_question(var.utilisateur.classe, lecons[(chx - 1)])
            lecon = lecons[(chx - 1)]
        except IndexError:
            clear_screen()
            print("Veillez choisir un numero disponible")
            input("<<< Retour")
            jouer()

    while on_play:
        if len(var.questions) == 0:
            clear_screen()
            print("Vous avez repondu correctement à toutes les questions! %s!" % (random.choice(var.congrats)))
            input("<<< Retour")
            on_play = False
            save()
        else:
            var.questions = poser_question(var.questions, lecon)
            chx = input("Continuer ou quitter (Q) ?: ")

            if chx.capitalize() == "Q":
                on_play = False
                save()
