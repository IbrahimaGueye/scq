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
            return "Une erreur est survenue ici..."

    else:
        return " "


def barre_infos():
    """
    Juste pour la deco...
    """
    print("===== Utilisateur: %s ===== Privilege: %s ===== Score: %d pts\n"
          % (var.utilisateur.nom_utilisateur.capitalize(),
             var.privileges[var.utilisateur.privilege],
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
        check_privilege()


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


def creer_profile(nom_utilisateur=""):
    """
    Fonction chargée de creer un un nouveau utilisateur.
    """
    cookies = {}

    clear_screen()

    if nom_utilisateur == "":
        nom_utilisateur = input("Choisissez un nom d'utilisateur (Q pour revenir au menu): ")

    if nom_utilisateur.capitalize() != "Q":
        if len(nom_utilisateur) < 6:
            print("Nom utilisateur invalide. Il doit au moins avoir 6 caracteres, choisissez encore...\n")
            input("<<< retour")
            creer_profile()

        else:
            with open("..//data//users//users", "rb") as fichier:
                lecteur = pickle.Unpickler(fichier)
                users = lecteur.load()

                if nom_utilisateur in users:
                    clear_screen()
                    print("Ce nom est deja pris")
                    time.sleep(2)
                    creer_profile()
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
                        creer_profile(nom_utilisateur)

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
            print("%s (%s)" % (user.capitalize(), user), end=' | ')

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
                    creer_profile(nom_utilisateur)
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
    """
    from . import menus
    afficher_menu(menus.menu_parametres_txt, menus.menu_parametres_funcs)


def aff_menu_admin():
    """
    Fonction chargée d'afficher le menu administrateur
    """
    from . import menus

    clear_screen()
    if var.utilisateur.privilege == 0:
        print(var.admin_message)
        input("<<< Retour")
    elif var.utilisateur.privilege >= 1:
        afficher_menu(menus.menu_admin1_txt, menus.menu_admin1_funcs)


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


def check_privilege():
    """
    Fonction chargée de controler le privilege utilisateur
    :return:
    """
    nv = 0

    if var.utilisateur.score < 500:
        nv = 0

    elif 500 <= var.utilisateur.score < 1000:
        nv = 1

    elif 1000 <= var.utilisateur.score < 2000:
        nv = 2
    else:
        nv = 3

    var.utilisateur.set_privilege(nv)


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


# ................Fonctions Administrateur..............

# Questions management
def creer_quizz(classe, lecon):
    """
    Fonction chargee de creer une liste et fichier vierge de questions
    """
    path_to_classe = "..//data//questions//%s" % classe
    path_to_questions = "..//data//questions//%s//%s" % (classe, lecon)
    empty_questions_list = []

    # Enregistrement du fichier
    with open(path_to_questions, "wb") as file:
        writer = pickle.Pickler(file)
        writer.dump(empty_questions_list)

    # Enregistrement sur la liste
    with open(path_to_classe + '//liste_lecons', 'rb') as file:
        lecteur = pickle.Unpickler(file)
        liste_lecons = lecteur.load()
        liste_lecons.append(lecon)

    with open(path_to_classe + '//liste_lecons', 'wb') as file:
        writer = pickle.Pickler(file)
        writer.dump(liste_lecons)


def ajouter_question(classe, lecon, question):
    """
    Fonction chargee d'ajouter une question sur la liste
    """
    clear_screen()
    path_to_questions = "..//data//questions//%s//%s" % (classe, lecon)

    with open(path_to_questions, "rb") as file:
        reader = pickle.Unpickler(file)
        questions = reader.load()

    questions.append(question)

    with open(path_to_questions, "wb") as file:
        writer = pickle.Pickler(file)
        writer.dump(questions)
        print("Question ajoutée avec succés")


def creer_question():
    """
    Fonction chargee de creer une nouvelle question
    """
    clear_screen()
    liste = list()

    question = input("La question: ")

    right_answer = input("La bonne réponse: ")
    clear_screen()

    liste.append(question)
    liste.append(right_answer)

    chx = "O"
    while chx.capitalize() != "N":
        answer = input("Add a false answer: ")
        liste.append(answer)
        clear_screen()

        chx = input("Ajouter une autre reponse incorrecte?  (O/N)?: \n")
        clear_screen()

    explications = input("Les explications maintenant: \n")
    liste.append(explications)

    return liste


def supprimer_question(classe, lecon, q_id):
    """

    :param lecon:
    :return:
    """
    pass


def modifier_elt_question(classe, lecon, q_id):
    """
    Fonction chargée de modifier une question selon son q_id
    """
    with open("..//data//questions//%s//%s" % (classe, lecon), "rb") as fichier:
        lecteur = pickle.Unpickler(fichier)
        questions = lecteur.load()
    question = questions[q_id]
    i = 1

    for elt in question:
        print("{} : Modifier ({})\n".format(i, elt))
        i += 1

    print("Q pour annuler")

    chx = input(">>> ")

    if chx.capitalize() != "Q":
        try:
            chx = int(chx)
        except ValueError:
            print("Choisissez un nombre valide\n")
            input("<<< Retour...")
            modifier_elt_question(classe, lecon, q_id)

        else:
            try:
                print(question[chx - 1], "\n\n")
            except IndexError:
                print("Choisissez un nombre disponible\n")
                modifier_elt_question(classe, lecon, q_id)
            else:
                modif = input("Entrez la nouvelle valeur: \n")
                question.pop(chx - 1)
                question.insert(chx - 1, modif)

                chx = input("Voulez vous sauvegarder les modifications? (O/N): ")

                # La sauvegarde
                if chx.capitalize() != "N":
                    questions.pop(q_id)
                    questions.insert(q_id, question)

                    with open("..//data//questions//%s//%s" % (classe, lecon), "wb") as fichier:
                        writer = pickle.Pickler(fichier)
                        writer.dump(questions)
                        print("Changements effectué!")


                else:
                    chx = input("Appliquer d'autres modifications?(O/N): ")

                    if chx.capitalize() != "N":
                        modifier_elt_question(classe, lecon, q_id)


def supprimer_elt_question(classe, lecon, q_id):
    """
    Fonction chargée de supprimer un element d'une question
    """
    with open("..//data//questions//%s//%s" % (classe, lecon), "rb") as fichier:
        lecteur = pickle.Unpickler(fichier)
        questions = lecteur.load()
    question = questions[q_id]
    i = 1

    for elt in question:
        print("{} : Supprimer ({})\n".format(i, elt))
        i += 1

    chx = int(input(">>> "))
    print(question[chx - 1], "\n\n")

    question.pop(chx - 1)

    chx = input("Voulez vous sauvegarder les modifications? (O/N): ")

    # La sauvegarde
    if chx.capitalize() != "N":
        questions.pop(q_id)
        questions.insert(q_id, question)

        with open("..//data//questions//%s//%s" % (classe, lecon), "wb") as fichier:
            writer = pickle.Pickler(fichier)
            writer.dump(questions)


def check_ajouter_question():
    """
    Fonction admin charger du cas ou 'utilisateur veut ajouter une question a une lecon specifique
    """
    clear_screen()
    i = 1
    with open("..//data//questions//%s//liste_lecons" % var.utilisateur.classe, "rb") as file:
        reader = pickle.Unpickler(file)
        lecons = reader.load()

    print("Voici les lecons disponibles:\n")

    for lecon in lecons:
        print("%d: %s" % (i, lecon))
        i += 1
    print("\n")

    chx = input("Sur quelle lecon souhaitez-vous ajouter la question?: ")

    try:
        chx = int(chx)
        lecon = lecons[(chx - 1)]
        ajouter_question(var.utilisateur.classe, lecon, creer_question())

    except ValueError:
        clear_screen()
        print("Veillez choisir un numero\n")
        input("<<< Retour")
        check_ajouter_question()

    except IndexError:
        clear_screen()
        print("Veillez choisir un numero disponible")
        input("<<< Retour")
        check_ajouter_question()


def check_modifier_elt_question(lecon=""):
    """
    Fonction chargée du cas ou l'utilsateur souhaite modifier une question

    """
    i = 1
    with open("..//data//questions//%s//liste_lecons" % var.utilisateur.classe, "rb") as file:
        reader = pickle.Unpickler(file)
        lecons = reader.load()

    print("Voici les lecons disponibles:\n")

    for lecon in lecons:
        print("%d: %s" % (i, lecon))
        i += 1
    print("\n")

    chx = input("Sur quelle lecon se trouve la question?: ")
    clear_screen()

    try:
        chx = int(chx)
        lecon = lecons[(chx - 1)]

        q_id = input("Veillez saisir le id de la question: ")
        try:
            q_id = int(q_id)

        except ValueError:
            clear_screen()
            print("Veillez choisir un numero\n")
            input("<<< Retour")
            check_modifier_elt_question(lecon)
        else:
            modifier_elt_question(var.utilisateur.classe, lecon, q_id)

    except ValueError:
        clear_screen()
        print("Veillez choisir un numero\n")
        input("<<< Retour")
        check_modifier_elt_question(lecon)

    except IndexError:
        clear_screen()
        print("Veillez choisir un numero disponible")
        input("<<< Retour")
        check_modifier_elt_question(lecon)


def check_supprimer_elt_question(lecon=""):
    """
    Fonction chargée du cas ou l'utilsateur souhaite supprimer un element d'une question

    """
    clear_screen()
    i = 1
    with open("..//data//questions//%s//liste_lecons" % var.utilisateur.classe, "rb") as file:
        reader = pickle.Unpickler(file)
        lecons = reader.load()

    print("Voici les lecons disponibles:\n")

    for lecon in lecons:
        print("%d: %s" % (i, lecon))
        i += 1
    print("\n")

    chx = input("Sur quelle lecon se trouve la question?: ")
    clear_screen()

    try:
        chx = int(chx)
        lecon = lecons[(chx - 1)]

        q_id = input("Veillez saisir le id de la question: ")
        try:
            q_id = int(q_id)

        except ValueError:
            clear_screen()
            print("Veillez choisir un numero\n")
            input("<<< Retour")
            check_supprimer_elt_question(lecon)
        else:
            supprimer_elt_question(var.utilisateur.classe, lecon, q_id)

    except ValueError:
        clear_screen()
        print("Veillez choisir un numero\n")
        input("<<< Retour")
        check_supprimer_elt_question(lecon)

    except IndexError:
        clear_screen()
        print("Veillez choisir un numero disponible")
        input("<<< Retour")
        check_supprimer_elt_question(lecon)
