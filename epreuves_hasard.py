import random

def epreuve_hasard():
    nom_epreuve=random.choice(["bonneteau", "jeu_lance_des"])
    if nom_epreuve == "bonneteau":
        bonneteau()
    else:
        jeu_lance_des()

def bonneteau():
    L = ['A','B','C']
    print("Bienvenue à l'épreuve des bonneteaux. Voici le but du jeu : devant vous se trouvent trois bonneteaux, la clé se trouve sous l'un d'eux. \nVous aurez deux essais pour tenter de trouver la clé. A chaque essai la clé est placée aléatoirement sous l'un des bonneteaux. Bonne chance !")
    print("Vous pouvez choisir un bonneteau parmi les trois : tapez A pour le premier, B pour le second et C pour le troisième.")
    nmb_tentatives = 0
    while nmb_tentatives != 2:
        position_cle = random.choice(L)
        choix_joueur = input("Choisissez un bonneteau parmi les trois : ")
        while (choix_joueur != "A") and (choix_joueur != "B") and (choix_joueur != "C"):
            choix_joueur = input("Choix incorrect. Veuillez indiquer un choix correct : ")
        if choix_joueur == position_cle :
            print("Bravo ! Vous avez trouvé la clé")
            return True
        else :
            nmb_tentatives = nmb_tentatives + 1
            print("Dommage, la clé n'était pas sous ce bonneteau. Il vous reste", 2 - nmb_tentatives, "tentatives.")
            L.remove(choix_joueur)
            if nmb_tentatives != 2 :
                print("Choisissez maintenant entre le bonneteau", L[0], "et le bonneteau", L[1], ": ", end="")
                choix_joueur = input("")
                while (choix_joueur != L[0]) and (choix_joueur != L[1]) :
                    choix_joueur = input("Choix incorrect. Veuillez indiquer un choix correct : ")
                if choix_joueur == position_cle:
                    print("Bravo ! Vous avez trouvé la clé")
                    return True
                else :
                    print("Dommage, vous n'avez pas réussi à avoir la clé. Elle se trouvait sous le bonneteau", position_cle, ". Vous avez perdu l'épreuve car vous n'avez pas réussi à trouver la clé en deux essais.")
                    return False


def jeu_lance_des() :
    print("Bienvenue à l'épreuve du lancer de dés. Vous allez jouer contre le maître du jeu. A chaque tour vous devrez lancer deux dés, le premier à obtenir un 6 remporte la partie. \nVous aurez un maximum de trois essais et c'est vous qui commencerez. Bonne chance !")
    nmb_essais = 0
    while nmb_essais != 3 :
        print("Il vous reste", 3 - nmb_essais, "essais.")
        a = input("Appuyez sur la touche entrée pour lancer les dés : ")
        tuple_joueur = random.randint(1,6), random.randint(1,6)
        print("Voici les différentes valeurs obtenues :", tuple_joueur[0], "et", tuple_joueur[1])
        if tuple_joueur[0] == 6 or tuple_joueur[1] == 6 :
            print("Bravo vous avez obtenu un 6. Vous gagnez donc le jeu et vous obtenez la clé.")
            return True
        else :
            tuple_maitre = random.randint(1,6), random.randint(1,6)
            print("Voici les dés obtenues par le maître du jeu :", tuple_maitre[0], "et", tuple_maitre[1])
            if tuple_maitre[0] == 6 or tuple_maitre[1] == 6 :
                print("Le maître du jeu a obtenu un 6. Vous perdez donc l'épreuve et n'obtenez pas la clé.")
                return False
        nmb_essais = nmb_essais + 1
        print("Aucun 6 n'a été obtenu. On passe donc au tour suivant.")
    print("Aucun joueur n'a obtenu de 6 après trois essais. Il y a donc match nul et vous ne remportez pas la clé.")
    return False

epreuve_hasard()
