#epreuves_finale.py, pyfort-BELTZUNG-SORENSEN-CROZIER-A, BELTZUNG-SÖRENSEN Gwenaël. Ce fichier importe les modules random et json.
# Il permet d’effectuer l'épreuve finale.


import json
import random


#Cette fonction permet d'efféctuer l'épreuve finale.
#La fonction charge d’abord le fichier indicesSalle.json dans la norme utf-8 pour que l’affichage soit correct.
# Il y a ensuite un choix de manière aléatoire de l'émission donc des indices et du mot-code. Il y a ensuite la comparaison entre
# la réponse du candidat et celle de la machine, si la réponse est la même, le candidat gagne sinon
# le nombre d'essais est décrémenté de un et un indice de plus est révélé. Si au bout de trois essais
# le candidat n'a pas trouvé la bonne réponse, il perd le jeu et la fonction retourne false,
# si le joueur a trouvé la bonne réponse la fonction retourne true.
def salle_De_Tresor():
    print("Bienvenue à l'épreuve finale, vous allez devoir trouver le mot en lien avec les indices pour accéder au trésor !")
    #Ouverture du fichier indiceSalle.json puis téléchargement de ce dernier dans la variable jeu_tv.
    with open("./data" + "/indicesSalle.json", "r", encoding='utf8') as indicesSalle:
        jeu_tv = json.load(indicesSalle)
        #Création d'un tableau qui va stocker toutes les années et ajout de ces dernières avec la fonction for puis choix de l'année.
        total_annee = []
        for clef in jeu_tv["Fort Boyard"].keys():
            total_annee.append(clef)
        annee = random.choice(total_annee)
        #Création d'un tableau qui va stocker toutes les émissions (avec leur numéro) de l'année choisie précédemment
        # et ajout de ces dernières avec la fonction for puis choix aléatoire de l'émission avec la fonction random.choice.
        emission_annee = []
        for num_emission in jeu_tv["Fort Boyard"][annee].keys():
            emission_annee.append(num_emission)
        emission = random.choice(emission_annee)
        #Chargement des indices et du mot-code (de l'émission choisie) dans la variable indices et dans celle mot_code.
        indices = jeu_tv["Fort Boyard"][annee][emission]["Indices"]
        mot_code = jeu_tv["Fort Boyard"][annee][emission]["MOT-CODE"]
        #Initialisation du nombre d'indices à 3 puis affichage des 3 premiers.
        nb_indices = 3
        print("Voici les indices :\n", indices[:nb_indices])
        #Initialisation du nombre d'essais à 3 et de reponse_correct à False.
        nb_essais_restants = 3
        reponse_correcte = False
        #Format de la réponse demandée.
        print("Veuillez saisir votre réponse sans déterminant.")
        #Cette boucle saisit la réponse de l'utilisateur puis si ce dernier a raison : reponse_correcte égal True et on sort de la boucle.
        # Si l'utilisateur a faux, le nombre d'essais restants est décrémenté de 1, si ce dernier n'est pas inférieur ou égal à 0 :
        # affichage du nombre d'éssais restants puis, affichage des indices avec un de plus que précédemment.
        # Si le nombre d'essais est égal ou inférieur à 0 : affichage du mot-code et sort de la fonction car
        # la condition du while n'est pas vérifiée.
        while nb_essais_restants > 0:
            reponse_final_joueur = ""
            reponse_joueur = input("Saisissez votre réponse : ")
            for i in range(len(reponse_joueur)):
                #Transformation de la réponse du joueur tout en majuscules dans la variable reponse_final_joueur.
                if 97 <= ord(reponse_joueur[i]) <= 123 or 224 <= ord(reponse_joueur[i]) <= 255:
                    reponse_final_joueur = reponse_final_joueur + chr(ord(reponse_joueur[i]) - 32)
                else:
                    reponse_final_joueur = reponse_final_joueur + reponse_joueur[i]
            if reponse_final_joueur == mot_code:
                reponse_correcte = True
                break
            else:
                nb_essais_restants = nb_essais_restants-1
                if nb_essais_restants >0:
                    if nb_essais_restants == 1:
                        print("Il vous reste ", nb_essais_restants, "essai")
                    else:
                        print("Il vous reste ", nb_essais_restants, "essais")
                    nb_indices = nb_indices + 1
                    print(indices[:nb_indices])
                else:
                    print("Le mot était : ", mot_code)
        #Si la reponse_correcte vaut True (booléen), affichage d'un message de victoire et la fonction retourne True,
        # si la reponse_correcte vaut False (booléen), affichage d'un message de défaite et la fonction retourne False.
        if reponse_correcte:
            print("Bravo vous avez gagné !")
            return True
        else:
            print("Désolé, vous n'avez pas su trouver la réponse, vous perdez !")
            return  False