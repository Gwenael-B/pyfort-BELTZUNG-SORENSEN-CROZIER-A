import random

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

bonneteau()