def introduction():
    print("Bonjour et bienvenue dans FORT BOYARD SIMULATOR.\nVous allez faire face à 4 défis. Pour chaque défi remporté, vous gagnerez une clé.\nIl vous faut obtenir au minimum 3 clés pour espérer accéder à la salle du trésor.")
    print("Vous aurez une épreuve de mathématiques, une épreuve de hasard, une épreuve de logique et enfin l'énigme de père Fouras\n")

def menu_epreuves():
    print("Choisissez une épreuve parmi les quatre suivantes.\n")
    print("1. Epreuve de Mathématiques\n2. Epreuve de Logique\n3. Epreuve du hasard\n4. Enigme du Père Fourras")
    choix = input("Choix : ")
    while choix not in ["1","2","3","4"]:  #Vérifie que le choix saisi correspond à une épreuve
        choix = input("Choix invalide. Veuillez réessayez : ")
    return choix

def composer_equipe():
    nb_joueurs = input("Combien de joueurs souhaitez-vous inscrire dans l'équipe (nombre maximum de trois joueurs) : ")
    while nb_joueurs not in ["1","2","3"]:  #Vérifie que le nombre de joueurs est bien entre 0 et 3
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