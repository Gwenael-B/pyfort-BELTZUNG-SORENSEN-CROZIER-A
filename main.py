from fonctions_utiles import introduction, composer_equipe, choisir_joueur, menu_epreuves, enregistrer_historique
from  epreuves_mathematiques import epreuve_math
from epreuves_logiques import jeu_tictactoe
from epreuves_hasard import  epreuve_hasard
from epreuve_pendu import jeu_pendu
from enigme_pere_fouras import enigme_pere_fouras
from epreuve_finale import salle_De_Tresor

def jeu():
    introduction()
    equipe = composer_equipe()
    clef = 0
    compteur_epreuve = 4
    liste_epreuve = ["Epreuve de Mathématiques", "Epreuve de Logique", "Epreuve du hasard", "Epreuve du pendu", "Enigme du Père Fourras"]
    while clef != 3 and compteur_epreuve > 0:
        num_epreuve, liste_epreuve = menu_epreuves(liste_epreuve)
        joueur_choisi = choisir_joueur(equipe)
        resultat = False
        match num_epreuve:
            case '1':
                resultat = epreuve_math()
            case '2':
                resultat = jeu_tictactoe()
            case '3':
                resultat = epreuve_hasard()
            case '4':
                resultat = jeu_pendu()
            case '5':
                resultat = enigme_pere_fouras()
        if resultat:
            enregistrer_historique(joueur_choisi["nom"], 1, 0)
            clef += 1
            if clef == 1:
                print("Vous avez maintenant", clef, "clé\n")
            else:
                print("Vous avez maintenant", clef, "clés\n")
        compteur_epreuve -= 1
    if clef >= 3:
        if salle_De_Tresor():
            print("Encore bravo, vous gagnez le jeu.")
            for i in range(len(equipe)):
                enregistrer_historique(equipe[i]["nom"], 0, 1)
            return None
        else:
            print("Désolé, vous perdez malheureusement le jeu.")
    else:
        print("\nDésolé, vous ne pouvez pas accéder à la salle du trésor car vous n'avez pas trois clés.\nVous perdez malheureusement le jeu.")
        return None

if __name__ == '__main__':
    jeu()