#epreuves_pendu.py, pyfort-BELTZUNG-SORENSEN-CROZIER-A, BELTZUNG-SÖRENSEN Gwenaël. Ce fichier importe les modules random et json.
# Il permet d’effectuer l'épreuve du pendu. Le programme saisit d'abord un mot de manière aléatoire dans le fichier
# liste_mot_pendu.json puis demande au joueur s’il veut saisir une lettre ou un mot. Le programme vérifie ensuite
# si la lettre choisie est dans le mot qui a été défini après l'avoir transformé en minuscules sans accent,
# si le joueur a choisi de saisir un mot le programme le compare également en minuscule et sans accent
# au mot choisi de manière aléatoire en minuscules et sans accent. Enfin, si la réponse est correcte,
# le programme renvoie true sinon il renvoie false.


import random
import json

#Fonction qui charge la liste de mots et la retourne.
def chargement_enigmes():
    with open("data/liste_mot_pendu.json", "r", encoding='utf8') as fichier_mots:
        liste_mots = json.load(fichier_mots)
        return liste_mots

#Transforme la lettre prise en paramètre et la retourne sans accent et en minuscule.
def remplace_lettre(lettre):
    #Lettre a.
    if 224 <= ord(lettre) <= 229:
        return 'a'
    #Lettre e.
    elif 232 <= ord(lettre) <= 235:
        return 'e'
    #Lettre i.
    elif 236 <= ord(lettre) <= 239:
        return 'i'
    #Lettre o.
    elif 242 <= ord(lettre) <= 246:
        return 'o'
    #Lettre u
    elif 249 <= ord(lettre) <= 252:
        return 'u'
    #Autre lettre.
    else:
        return lettre

#Transforme le mot pris en paramètre et le retourne sans accent et en minuscules.
def mot_simplifie(mot):
    mot_simple = ""
    for i in range(len(mot)):
        mot_simple = mot_simple + remplace_lettre(mot[i])
    return mot_simple

#Fonction qui vérifie que le choix du joueur est correct et retourne le choix du joueur.
def saisie_choix_joueur():
    choix_joueur = 0
    while True:
        try:
            choix_joueur = int(input("\nSi vous voulez écrire une lettre saisissez 1, si vous voulez écrire un mot saisissez 2 : "))
            if choix_joueur == 1 or choix_joueur == 2:
                return choix_joueur
        except ValueError:
            print("Votre réponse n'est pas valide.")

#Fonction qui vérifie que la lettre saisie par le joueur est correcte et la convertit en minuscules puis la renvoie.
def saisie_lettre_joueur():
    while True:
        try:
            lettre_joueur = input("Saisissez votre lettre : ")
            if len(lettre_joueur) == 1:
                if 65 <= ord(lettre_joueur) <= 91 or 192 <= ord(lettre_joueur) <= 223:
                    lettre_final_joueur = remplace_lettre(chr(ord(lettre_joueur) + 32))
                    return lettre_final_joueur
                else:
                    return lettre_joueur
        except ValueError:
            print("Votre réponse n'est pas valide.")

#Fonction qui saisit et convertit le mot final du joueur en minuscules et le retourne.
def saisie_mot_joueur():
    mot_joueur = input("Saisissez votre mot. ")
    mot_final_joueur = ""
    for i in range(len(mot_joueur)):
        # Transformation de la réponse du joueur tout en minuscules dans la variable mot_final_joueur.
        if 65 <= ord(mot_joueur[i]) <= 91 or 192 <= ord(mot_joueur[i]) <= 223:
            mot_final_joueur = mot_final_joueur + chr(ord(mot_joueur[i]) + 32)
        else:
            mot_final_joueur = mot_final_joueur + mot_joueur[i]
    return mot_final_joueur

#Cette fonction retourne une chaine de caractères où sont présentes les lettres utilisées et leur position dans le mot.
def affichage_lettre_trouvees(lettres_utilisees, mot):
    lettre = {}
    affichage = ""
    for i in range(len(mot)):
        if mot[i] in lettres_utilisees:
            lettre[i] = mot[i]
        else:
            lettre[i] = "_"
    for valeur in lettre.values():
        affichage += valeur
    return affichage

#Cette fonction permet d'afficher le pendu en fonction du nombre de tentatives déja effectuées, saisi en paramètre,
# elle retourne un espace pour plus de lisibilité.
def affichage_pendu(tentatives):
    mat_verticale = " |  "
    ligne1 = " ______\n"
    ligne2 = " |  (°~°)\n"
    ligne3 = " |   /|\\\n"
    ligne4 = " |   / \\\n"
    ligne5 = "---"

    if tentatives == 0:
        return " "
    elif tentatives == 1:
        print("\n"*4, ligne5)
        return " "
    elif tentatives == 2:
        print("\n", mat_verticale, "\n", mat_verticale, "\n", mat_verticale, "\n",  ligne5)
        return ""
    elif tentatives == 3:
        print(ligne1, mat_verticale, "\n", mat_verticale, "\n", mat_verticale, "\n", ligne5)
        return " "
    elif tentatives == 4:
        print(ligne1, ligne2, mat_verticale, "\n", mat_verticale, "\n", ligne5)
        return " "
    elif tentatives == 5:
        print(ligne1, ligne2, mat_verticale, " |\n", mat_verticale, "\n", ligne5)
        return " "
    elif tentatives == 6:
        print(ligne1, ligne2, mat_verticale, "/|\n", mat_verticale, "\n", ligne5)
        return " "
    elif tentatives == 7:
        print(ligne1, ligne2, ligne3, mat_verticale, "\n", ligne5)
        return " "
    elif tentatives == 8:
        print(ligne1, ligne2, ligne3, mat_verticale, "/\n", ligne5)
        return " "
    else:
        print(ligne1, ligne2, ligne3, ligne4, ligne5)
        return " "

#Fonction principale qui permet de coordonner le jeu et qui retourne à la fin false si le mot n'a pas été trouvé et true s'il a été trouvé.
def jeu_pendu():
    print("Bienvenue au jeu du pendu, vous allez devoir deviner un mot avant que vous ne soyez pendu (9 tentatives).\nBonne chance !\n")
    tentatives = 0
    liste_mots = chargement_enigmes()
    mot_choisi = random.choice(liste_mots)
    mot = mot_simplifie(mot_choisi)
    mot_joueur = ""
    lettres_utilisees = []
    print("Voici la longueur du mot : ", end="")
    #Affiche un tiret pour chaque lettre du mot.
    for i in range(len(mot)):
        print("_", end="")
    while mot != mot_joueur and tentatives < 9:
        #Vérifie que le choix du joueur est correct.
        choix_joueur = saisie_choix_joueur()
        if choix_joueur == 1:
            #Vérifie que la lettre saisie par le joueur est correcte.
            lettre_joueur = saisie_lettre_joueur()
            #Ajoute la lettre dans le tableau lettres_utilisees.
            lettres_utilisees.append(remplace_lettre(lettre_joueur))
            #Affiche les lettres trouvées dans le mot sinon un tiret.
            print(affichage_lettre_trouvees(lettres_utilisees, mot))
            #Vérifie si la lettre est dans le mot et sinon, décrémentation du nombre de tentatives.
            if remplace_lettre(lettre_joueur) not in mot:
                tentatives += 1
                print("La lettre n'est pas dans le mot :")
            #Affiche l'avancée du pendu.
            print(affichage_pendu(tentatives))
            #Vérification si toutes les lettres correspondent à celles du mot et message correspondant.
            if affichage_lettre_trouvees(lettres_utilisees, mot) == mot:
                print("\nBravo, vous avez gagné !")
                return True
            #Affiche la ou les lettres déjà utilisées par le joueur.
            if len(lettres_utilisees) != 1:
                print("Voici les lettres que vous avez déjà choisies : ", end="")
                for i in range(len(lettres_utilisees)):
                    print(lettres_utilisees[i], end=", ")
            else:
                print("Voici la lettre que vous avez déjà choisie : ", end="")
                for i in range(len(lettres_utilisees)):
                    print(lettres_utilisees[i], end="")
        else:
            #Vérification si réponse juste affichage du message correspondant.
            if mot_simplifie(saisie_mot_joueur()) == mot_simplifie(mot):
                print("\nBravo, vous avez gagné !")
                return True
            else:
                print("\nDésolé, vous n'avez pas trouvé le mot qui était : ", mot_choisi)
                return False
    #Vérification si réponse juste affichage du message correspondant.
    if mot_simplifie(affichage_lettre_trouvees(lettres_utilisees, mot)) == mot_simplifie(mot):
        print("\nBravo, vous avez gagné !")
        return True
    else:
        print("\nDésolé, vous n'avez pas trouvé le mot qui était : ", mot_choisi)
        return False