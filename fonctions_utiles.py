#fonctions_utiles.py, pyfort-BELTZUNG-SORENSEN-CROZIER-A, CROZIER Clarence. Ce fichier comporte des
# fonctions utiles au bon déroulement du jeu et qui seront ensuite utilisé dans le main

#Cette fonction affiche juste un message d'introduction pour signaler l'arrivée dans le jeu et son déroulement
def introduction():
    print("Bonjour et bienvenue dans FORT BOYARD SIMULATOR.\nVous allez faire face à 4 défis. Pour chaque défi remporté, vous gagnerez une clé.\nIl vous faut obtenir au minimum 3 clés pour espérer accéder à la salle du trésor.")
    print("Vous aurez une épreuve de mathématiques, une épreuve de hasard, une épreuve de logique et enfin l'énigme de père Fouras.\n")

#Cette fonction permet au joueur de choisir une épreuve. Elle prend en argument la liste des épreuves disponibles pour permettre
# au joueur de choisir l'épreuve qu'il souhaite puis la supprime dans la liste des épreuves disponibles. La fonction
# retourne ensuite l'épreuve choisie par le joueur et la nouvelle liste des épreuves disponibles
def menu_epreuves(liste_epreuve):
    L = liste_epreuve
    C = []  #Initialise une liste qui contiendra les choix possibles
    print("Choisissez une épreuve parmi les épreuves suivantes : \n")
    for i in range(len(L)):
        print(i+1, ".", L[i])
    for i in range(len(L)):  #Remplis le tableau des choix possibles avec des caractères
        C.append(str(i+1))
    choix = input("Choix : ")
    while choix not in C:
        choix = input("Erreur veuillez entrer un nombre correct : ")
    epreuve = L[int(choix)-1]
    del L[int(choix)-1]  #Supprime l'épreuve qui a été choisi de la liste épreuve
    return epreuve, L

#Cette fonction permet de composer les équipes. Elle ne prend pas d'arguments en entrée et retourne la liste des dictionnaires des joueurs
def composer_equipe():
    nb_joueurs = input("Combien de joueurs souhaitez-vous inscrire dans l'équipe (nombre maximum de trois joueurs) : ")
    while nb_joueurs not in ["1","2","3"]:  #Vérifie que le nombre de joueurs est bien entre 1 et 3
        nb_joueurs = input("Choix invalide. Veuillez réessayez : ")
    verif_leader = False  #Création de la variable pour vérifier si l'un des joueurs est déjà leader
    equipe = []  #Initialisation de la liste équipe qui contiendra les infos des joueurs
    for i in range(int(nb_joueurs)):
        pipe = False
        nom = input("Entrez le nom du joueur {} sans caractère '|' : ".format(i+1))
        while not(pipe):
            for j in range(len(nom)):
                if nom[j] == '|':
                    nom = input("Veuillez réessayer sans caractère '|' : ")
                    break
            else:
                pipe = True
        profession = input("Entrez la profession du joueur {} sans caractère '|': ".format(i+1))
        pipe = False
        while not(pipe):
            for j in range(len(profession)):
                if profession[j] == '|':
                    profession = input("Veuillez réessayer sans caractère '|' : ")
                    break
            else:
                pipe = True
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

#Cette fonction permet de choisir le joueur qui participera à une épreuve. Elle prend la liste des joueurs en arguments et retourne
# le dictionnaire contenant toutes les informations du joueur choisi
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
        choix = input("Choix incorrect, veuillez réessayer : ")
    return equipe[int(choix)-1]

#Cette fonction permet d'enregistrer l'historique. Elle prend en argument le nom, la profession, le nombre de clés et de victoire d'un
# joueur mais elle ne retourne rien. Elle ouvre le fichier historique.txt d'abord en lecture seule pour récupérer les informations
# déjà présentes puis elle l'ouvre ensuite en écriture pour réécrire toutes les informations
def enregistrer_historique(nom, profession, nb_cle, nb_victoire):
    with open("data/historique.txt", "r", encoding='utf8') as f :  #Ouvre le fichier historique en lecture seul
        dico_principal = {}  #Initialise le dictionnaire qui stockera toutes les informations des joueurs
        i = 0
        f.readline()  #Saute les deux premières lignes car elles ne contiennent pas d'informations, elles servent juste à rendre les valeurs plus visibles
        f.readline()
        for ligne in f:  #On parcourt chaque ligne du fichier historique en partant de la troisième
            ligne = ligne.split('|')  #On utilise la fonction split pour séparer les mots
            dico_joueur = {"nom": ligne[0].strip(), "profession" : ligne[1].strip(), "nb_cle": int(ligne[2]), "nb_victoire": int(ligne[3])}  #Initialisation du dictionnaire qui contient toutes les données d'un joueur ligne par ligne
            dico_principal[i] = dico_joueur  #On ajoute ce dictionnaire au dictionnaire principal qui contiendra toutes les informations
            i = i + 1
        joueur_trouve = False
        for i in range(len(dico_principal)):  #On parcourt le dictionnaire principal
            if dico_principal[i]["nom"] == nom:  #On vérifie si le joueur donné comme argument de la fonction est déjà dans le dictionnaire principal
                dico_principal[i]["nb_cle"] = int(dico_principal[i]["nb_cle"]) + nb_cle  #On ajoute le nombre de clés qu'il a obtenus au nombre de clés déjà présents
                dico_principal[i]["nb_victoire"] = int(dico_principal[i]["nb_victoire"]) + nb_victoire  #Pareil pour le nombre de victoires
                joueur_trouve = True
                break  #On sort de la boucle for pour ne pas parcourir tous les dictionnaires des joueurs une fois qu'on a trouvé le bon
        if not(joueur_trouve):  #Si le nom du joueur mis comme argument dans la fonction n'est pas encore dans le dictionnaire principal, on le rajoute
            dico_principal[len(dico_principal)] = {"nom": nom, "profession": profession, "nb_cle": nb_cle, "nb_victoire": nb_victoire}
    with open("data/historique.txt", "w", encoding='utf8') as f:  #On ouvre maintenant le fichier historique en écriture pour modifier les informations des joueurs
        f.write(f"{'Nom':^11} {"|"} {'Profession':^12} {"|"} {'Cles':^6} {"|"} {'Victoires':^5}\n")  #On réécrit la mise en page comme le fichier est compressé en ouvrture, les :^nombre servent à aligner les mots
        f.write("------------------------------------------------\n")
        for i in range(len(dico_principal)):  #On parcourt notre dictionnaire principal
            ligne = f"{dico_principal[i]['nom']:^11} {"|"} {dico_principal[i]['profession']:^12} {"|"} {dico_principal[i]['nb_cle']:^6} {"|"} {dico_principal[i]['nb_victoire']:^7}\n"  #On prépare le texte à écrire dans la ligne comme f.write() ne prend qu'un argument
            f.write(ligne)  #On écrit les informations d'un joueur à chaque ligne