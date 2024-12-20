import json
import random

#Cette fonction permet d'efféctuer l'épreuve finale.
def salle_De_Tresor():
    print("Bienvenu à l'épreuve finale, vous allez devoir trouver le mot en lien avec les indices pour accéder au trésors !")
    #Ouverture du fichier indiceSalle.json puis téléchargement de ce dernier dans la variable jeu_tv.
    with open("./data" + "/indicesSalle.json", "r", encoding='utf8') as indicesSalle:
        jeu_tv = json.load(indicesSalle)
        #Création d'un tableau qui va stocker toutes les années et ajout de ces dernières avec la fonction for puis choix de l'année.
        total_annee = []
        for clef in jeu_tv["Fort Boyard"].keys():
            total_annee.append(clef)
        annee = random.choice(total_annee)
        #Choix de l'émission puis chargement des indices et du mot code (de l'émission choisie) dans la variable indices et celle mot_code.
        emission = "Émission 00"
        while emission == "Émission 00":
            num_emission = random.choice(annee)
            emission = str("Émission 0" + num_emission)
        indices = jeu_tv["Fort Boyard"][annee][emission]["Indices"]
        mot_code = jeu_tv["Fort Boyard"][annee][emission]["MOT-CODE"]
        #Initialisation du nombre d'indices à 3 puis affiches les 3 premiers.
        nb_indices = 3
        print("Voici les indices :\n", indices[:nb_indices])
        #Initialisation du nombre d'essais à 3 et de reponse_correct à False.
        nb_essais_restants = 3
        reponse_correcte = False
        #Format de la réponse demandé.
        print("Veuillez saisir votre réponse en majuscule, sans accents et sans déterminant.")
        #Cette boucle saisie la réponse de l'utilisateur puis si ce dernier à raison : reponse_correct égale True et on sort de la boucle.
        # Si l'utilisateur à faux, le nombre d'éssais réstants est décrémenté de 1, si ce dernier n'est pas inférieur ou égale à 0 :
        # affichage du nombre d'éssais réstants puis, affichage des indices avec un de plus que précédemment.
        # Si le nombre d'éssais est égale ou inférieur à 0 : affichage du mot code et sort de la fonction car
        # la condition du while n'est pas vérifiée.
        while nb_essais_restants > 0:
            reponse_joueur = input("Saisissez votre réponse : ")
            if reponse_joueur == mot_code:
                reponse_correcte = True
                break
            else:
                nb_essais_restants = nb_essais_restants-1
                if nb_essais_restants >0:
                    print("Il vous reste ", nb_essais_restants, "réstants.")
                    nb_indices = nb_indices + 1
                    print(indices[:nb_indices])
                else:
                    print("Le mot était : ", mot_code, ".")
        #Si la réponse_correcte vaut True (booléen), affichage d'un message de victoire et la fonction retourne True,
        # si la réponse_correcte vaut False (booléen), affichage d'un message de défaite et la fonction retourne False.
        if reponse_correcte:
            print("Bravo vous avez gagner !")
            return True
        else:
            print("Désolé, vous n'avez pas su trouver la réponse, vous perdez !")
            return  False