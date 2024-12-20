import json
import random

#Cette fonction permet de charger toutes les données du fichier enigmesPF.json dans la variable 'donnes' et la retourne.
def charger_enigmes(dossier):
    with open(dossier + "/enigmesPF.json", "r", encoding='utf8') as enigmesPF:
        donnees = json.load(enigmesPF)
        return donnees

#Cette fonction permet de choisir au hasard une énigme, converti la réponse en minuscule puis affiche la question.
#La réponse du candidat est ensuite converti en minuscule et comparée à la réponse attendue, si la réponse est la même,
# la fonction retourne True et un message de victoire est affiché sinon le nombre d'essais est décrémenté de un.
#Si au bout de trois essais le candidat n'a pas trouvé la réponse, un message affiche la défaite et la bonne réponse puis retourne False.
def enigme_pere_fouras():
    tentatives_restantes = 3
    liste_enigmes = charger_enigmes("./data")
    enigme = random.choice(liste_enigmes)
    reponse_machine = enigme["reponse"]
    reponse_final_machine = ""
    for i in range(len(reponse_machine)):
        if 65 <= ord(reponse_machine[i]) <= 91:
            reponse_final_machine = reponse_final_machine + chr(ord(reponse_machine[i]) + 32)
        else:
            reponse_final_machine = reponse_final_machine + reponse_machine[i]
    print("Pour gagner la clé, répondez correctement à cette énigme !")
    print(enigme["question"])
    while tentatives_restantes > 0:
        reponse_final_candidat = ""
        reponse_candidat = input("Saisissez votre réponse avec le determinant : ")
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