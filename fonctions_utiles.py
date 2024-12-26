def introduction():
    print("Bonjour et bienvenue dans FORT BOYARD SIMULATOR.\nVous allez faire face à 4 défis. Pour chaque défi remporté, vous gagnerez une clé.\nIl vous faut obtenir au minimum 3 clés pour espérer accéder à la salle du trésor.")
    print("Vous aurez une épreuve de mathématiques, une épreuve de hasard, une épreuve de logique et enfin l'énigme de père Fouras.\n")

def menu_epreuves():
    print("Choisissez une épreuve parmi les quatre suivantes : \n")
    print("1. Epreuve de Mathématiques\n2. Epreuve de Logique\n3. Epreuve du hasard\n4. Enigme du Père Fourras")
    choix = input("Choix : ")
    while choix not in ["1","2","3","4"]:  #Vérifie que le choix saisi correspond à une épreuve
        choix = input("Choix invalide. Veuillez réessayez : ")
    return choix

def composer_equipe():
    nb_joueurs = input("Combien de joueurs souhaitez-vous inscrire dans l'équipe (nombre maximum de trois joueurs) : ")
    while nb_joueurs not in ["1","2","3"]:  #Vérifie que le nombre de joueurs est bien entre 1 et 3
        nb_joueurs = input("Choix invalide. Veuillez réessayez : ")
    verif_leader = False  #Création de la variable pour vérifier si l'un des joueurs est déjà leader
    equipe = []  #Initialisation de la liste équipe qui contiendra les infos des joueurs
    for i in range(int(nb_joueurs)):
        nom = input("Entrez le nom du joueur {} : ".format(i+1))
        profession = input("Entrez la profession du joueur {} : ".format(i+1))
        if not verif_leader:  #Si il n'y a eu aucun leader on rentre dans la boucle et on demande si le joueur est le leader
            leader = input("Ce joueur est-il le leader (répondez par oui ou non) : ")
            while leader not in ["oui", "non"]:
                leader = input("Choix incorrect. Veuillez répondre par oui ou non : ")
            if leader == "oui":  #Si un joueur répond qu'il est leader, la variable verif_leader devient Vrai et ainsi on ne redemandera plus si le joueur veut être leader
                verif_leader = True
        joueur = {"nom" : nom, "profession" : profession, "leader" : leader, "cles_gagnees" : 0}  #Initialise un dictionnaire avec toutes les informations sur un joueur, il va être initialisé à chaque boucle
        leader = "non"
        equipe.append(joueur)  #Ajoute le dictionnaire du joueur à la liste équipe
    if not verif_leader:  #Vérifie si la variable verif_leader est fausse c'est-à-dire si aucun joueur n'a été mis leader, dans ce cas-là on rentre dans la boucle
        equipe[0]["leader"] = "oui"  #Met le premier joueur leader
        print("Comme aucun joueur n'a été désigné leader, c'est le premier joueur soit", equipe[0]["nom"], "qui a été choisi leader.")
    return equipe

def choisir_joueur(equipe):
    taille = []  #initialise une liste pour contenir le choix du joueur, la liste va être remplie par les numéros des joueurs et dépend donc du nombre de joueurs
    print("")  #Ecris une ligne vide pour faire un saut de ligne et afficher la liste de joueurs distinctes des autres informations
    for i in range(len(equipe)):  #Boucle du nombre de joueurs pour afficher à chaque ligne les informations des joueurs
        if equipe[i]["leader"] == "oui":  #Si le joueur i est le leader alors la variable leader prend l'information à afficher
            leader = "Leader"
        else:
            leader = "Membre"
        print("{}. {} ({}) - {} ".format(i+1, equipe[i]["nom"], equipe[i]["profession"], leader))  #Affiche les informations du joueur i
        taille.append(str(i+1))  #Ajoute le numéro du joueur à la liste de choix possible pour sélectionner après le joueur que l'on veut
    print("")  #Ecris une ligne vide pour faire un saut de ligne et afficher la liste de joueurs distinctes des autres informations
    choix = input("Entrez le numéro du joueur souhaité : ")
    while choix not in taille:  #Tant que le choix du numéro du joueur n'est pas dans la liste cela signifie que le choix n'est pas valide, on redemande alors un numéro
        choix = input("Choix incorrect, veuillez réessayez : ")
    return equipe[int(choix)-1]

def enregistrer_historique(nom, nb_cle, nb_victoire):
    with open("historique.txt", "r") as f :  #Ouvre le fichier historique en lecture seul
        dico_principal = {}  #Initialise le dictionnaire qui stockera toutes les informations des joueurs
        i = 0
        f.readline()  #Saute les deux premières lignes car elles ne contiennent pas d'informations, elles servent juste à rendre les valeurs plus visibles
        f.readline()
        for ligne in f:  #On parcourt chaque ligne du fichier historique en partant de la troisième
            ligne = ligne.split()  #On utilise la fonction split pour séparer les mots
            dico_joueur = {"nom": ligne[0], "nb_cle": int(ligne[2]), "nb_victoire": int(ligne[4])}  #Initialisation du dictionnaire qui contient toutes les données d'un joueur ligne par ligne
            dico_principal[i] = dico_joueur  #On ajoute ce dictionnaire au dictionnaire principal qui contiendra toutes les informations
            i = i + 1
        for i in range(len(dico_principal)):  #On parcourt le dictionnaire principal
            if dico_principal[i]["nom"] == nom:  #On vérifie si le joueur donné comme argument de la fonction est déjà dans le dictionnaire principal
                dico_principal[i]["nb_cle"] = int(dico_principal[i]["nb_cle"]) + nb_cle  #On ajoute le nombre de clés qu'il a obtenus au nombre de clés déjà présents
                dico_principal[i]["nb_victoire"] = int(dico_principal[i]["nb_victoire"]) + nb_victoire  #Pareil pour le nombre de victoires
                break  #On sort de la boucle for pour ne pas parcourir tous les dictionnaires des joueurs une fois qu'on a trouvé le bon
        else:  #Si le nom du joueur mis comme argument dans la fonction n'est pas encore dans le dictionnaire principal, on le rajoute
            dico_principal[len(dico_principal)] = {"nom": nom, "nb_cle": nb_cle, "nb_victoire": nb_victoire}
    with open("historique.txt", "w") as f:  #On ouvre maintenant le fichier historique en écriture pour modifier les informations des joueurs
        f.write(f"{'Nom':^10} {"|"} {'Cles':^5} {"|"} {'Victoires':^5}\n")  #On réécrit la mise en page comme le fichier est compressé en ouvrture, les :^nombre servent à aligner les mots
        f.write("-------------------------------\n")
        for i in range(len(dico_principal)):  #On parcourt notre dictionnaire principal
            ligne = f"{dico_principal[i]['nom']:^10} {"|"} {dico_principal[i]['nb_cle']:^5} {"|"} {dico_principal[i]['nb_victoire']:^5}\n"  #On prépare le texte à écrire dans la ligne comme f.write() ne prend qu'un argument
            f.write(ligne)  #On écrit les informations d'un joueur à chaque ligne