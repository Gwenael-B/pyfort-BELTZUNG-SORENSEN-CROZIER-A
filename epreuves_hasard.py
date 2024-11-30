import random

def bonneteau():
    L = ['A','B','C']
    print("Bienvenue à l'épreuve des bonneteaux. Voici le but du jeu : devant vous se trouvent trois bonneteaux, la clé se trouve sous l'un d'eux. \nVous aurez deux essais pour tenter de trouver la clé. A chaque essai la clé est placée aléatoirement sous l'un des bonneteaux. Bonne chance !")
    print("Vous pouvez choisir un bonneteau parmi les trois : tapez A pour le premier, B pour le second et C pour le troisième.")
    choix_joueur = 'Z'
    position_cle = 'Z'
    nmb_tentatives = 0
    while nmb_tentatives != 2:
        position_cle = random.choice(L)
        choix_joueur = input("Choisissez un bonneteau parmi les trois : ")
        while (choix_joueur != 'A') or (choix_joueur != 'B') or (choix_joueur != 'C') :
            choix_joueur = str(input("Choix incorrect. Veuillez indiquer un choix correct : "))
        if choix_joueur == position_cle :
            print("Bravo ! Vous avez trouvé la clé")
            return True
        else :
            nmb_tentatives = nmb_tentatives + 1
            print("Dommage, la clé n'était pas sous ce bonneteau. Elle était sous le bonneteau", position_cle, "Il vous reste", 2 - nmb_tentatives - 1, "tentatives.")
    print("Dommage, vous n'avez pas réussi à avoir la clé. Vous avez perdu l'épreuve.")
    return False


bonneteau()