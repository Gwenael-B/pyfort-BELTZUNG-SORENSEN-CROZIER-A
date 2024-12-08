import json
import random


def charger_enigmes(dossier):
    with open(dossier + "/enigmesPF.json", "r", encoding='utf8') as enigmesPF:
        donnees = json.load(enigmesPF)
        return donnees

def enigme_pere_fouras():
    tentatives_restantes = 3
    reponse_final_machine = ""
    liste_enigmes = charger_enigmes("./data")
    enigme = random.choice(liste_enigmes)
    reponse_machine = enigme["reponse"]
    print("Pour gagner la clé, répondez correctement à cette énigme !")
    print(enigme["question"])
    for i in range(len(reponse_machine)):
        if 65 <= ord(reponse_machine[i]) <= 91:
            reponse_final_machine = reponse_final_machine + chr(ord(reponse_machine[i]) + 32)
        else:
            reponse_final_machine = reponse_final_machine + reponse_machine[i]
    while tentatives_restantes > 0:
        reponse_final_candidat = ""
        reponse_candidat = input("Saisissez votre réponse : ")
        for i in range(len(reponse_candidat)):
            if 65 <= ord(reponse_candidat[i]) <= 91:
                reponse_final_candidat = reponse_final_candidat + chr(ord(reponse_candidat[i])+32)
            else:
                reponse_final_candidat = reponse_final_candidat + reponse_candidat[i]
        if reponse_final_candidat == reponse_final_machine:
            print("Bravo, vous gagner la clé.")
            return True
        else:
            tentatives_restantes = tentatives_restantes - 1
            if tentatives_restantes != 1:
                print("Votre réponse est incorrecte, il vous reste", tentatives_restantes, "tentatives.")
            else:
                print("Votre réponse est incorrecte, il vous reste", tentatives_restantes, "tentative.")

    print("Dommage, vous avez perdu, la réponse était :", reponse_final_machine)
    return False

enigme_pere_fouras()