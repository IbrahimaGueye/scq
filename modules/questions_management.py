#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pickle


# import fonctions


def create_quizz_question(classe, lecon):
    """
    Fonction chargee de creer une liste et fichier vierge de questions
    """
    path_to_classe = "..//data//questions//" + classe
    path_to_questions = "..//data//questions//" + classe + "//" + lecon
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


# ..............................................................................
def add_question(classe, lecon, question):
    """
    Fonction chargee d'ajouter une question sur la liste
    """
    path_to_questions = "..//data//questions//" + classe + "//" + lecon

    with open(path_to_questions, "rb") as file:
        reader = pickle.Unpickler(file)
        questions = reader.load()

    questions.append(question)

    with open(path_to_questions, "wb") as file:
        writer = pickle.Pickler(file)
        writer.dump(questions)
        print("Question ajoutée avec succés")


# ..............................................................................
def create_question():
    """
    Fonction chargee de creer une nouvelle question
    """
    from . import fonctions
    liste = list()

    question = input("La question: ")
    fonctions.clear_screen()

    right_answer = input("The bonne réponse: ")
    fonctions.clear_screen()

    liste.append(question)
    liste.append(right_answer)

    chx = "O"
    while chx.capitalize() != "N":
        answer = input("Add a false answer: ")
        liste.append(answer)
        fonctions.clear_screen()

        chx = input("Add another false answer (O/N)?: \n")
        fonctions.clear_screen()

    explications = input("Les explications maintenant: \n")
    liste.append(explications)

    return liste


# ..............................................................................
def modify_question(classe, lecon, q_id):
    """
    Fonction chargée de modifier une question selon son q_id
    """
    with open("..//data//questions//" + classe + "//" + lecon, "rb") as fichier:
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
            modify_question(classe, lecon, q_id)

        else:
            try:
                print(question[chx - 1], "\n\n")
            except IndexError:
                print("Choisissez un nombre disponible\n")
                modify_question(classe, lecon, q_id)
            else:
                modif = input("Entrez la nouvelle valeur: \n"
                              )
                question.pop(chx - 1)
                question.insert(chx - 1, modif)

                chx = input("Voulez vous sauvegarder les modifications? (O/N): ")

                # La sauvegarde
                if chx.capitalize() != "N":
                    questions.pop(q_id)
                    questions.insert(q_id, question)

                    with open("..//data//questions//" + classe + "//" + lecon, "wb") as fichier:
                        writer = pickle.Pickler(fichier)
                        writer.dump(questions)
                        print("Changements effectué!")


                else:
                    chx = input("Appliquer d'autres modifications?(O/N): ")

                    if chx.capitalize() != "N":
                        modify_question(classe, lecon, q_id)



def supprimer_elt_question(classe, lecon, q_id):
    """
    Fonction chargée de supprimer un element d'une question
    """
    with open("..//data//questions//" + classe + "//" + lecon, "rb") as fichier:
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

        with open("..//data//questions//" + classe + "//" + lecon, "wb") as fichier:
            writer = pickle.Pickler(fichier)
            writer.dump(questions)

# liste = ["Temps et cinématique",
#          "Temps, cinématique et dynamique newtoniennes",
#          "Lois de Newton : conservation de la quantité de mouvement",
#          ]
#
# for lecon in liste:
#     create_quizz_question("tle", lecon)
#     print("(%s) Crée avec succés" % lecon)

# add_question("2nd", "Mouvement", create_question())

liste = create_question()
