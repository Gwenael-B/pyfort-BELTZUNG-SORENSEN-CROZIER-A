#main.py, pyfort-BELTZUNG-SORENSEN-CROZIER-A, BELTZUNG-SÖRENSEN Gwenaël. Ce fichier coordonne et exécute le jeu dans sa généralité,
# il appelle tout d'abord l'ensemble des fonctions épreuves. Il choisit ensuite une épreuve de manière aléatoire
# puis l'exécute si elle retourne true alors la variable résultats vos true et le joueur gagne une clé sinon il ne gagne pas de clé.
# Enfin, si l'équipe a au moins trois clés, elle peut accéder à la salle du trésor si salle_De_tresor vaut true alors,
# le jeu est gagné et un message de victoire est affiché sinon un message de défaite est affiché.
# Cette fonction ne retourne rien car elle n'est pas utilisé par une autre fonction ensuite.


#Importation de toutes les fonctions qui sont des épreuves.
from fonctions_utiles import introduction, composer_equipe, choisir_joueur, menu_epreuves, enregistrer_historique
from  epreuves_mathematiques import epreuve_math
from epreuves_logiques import jeu_tictactoe
from epreuves_hasard import  epreuve_hasard
from epreuve_pendu import jeu_pendu
from enigme_pere_fouras import enigme_pere_fouras
from epreuve_finale import salle_De_Tresor

#C'est le programme principal.
def jeu():
    introduction()
    equipe = composer_equipe()
    clef = 0
    compteur_epreuve = 4
    liste_epreuve = ["Epreuve de Mathématiques", "Epreuve de Logique", "Epreuve du hasard", "Epreuve du pendu", "Enigme du Père Fourras"]
    #Condition qui permet de vérifier si le joueur a trois clés ou s'il n'a plus d'éssais réstants.
    while clef != 3 and compteur_epreuve > 0:
        num_epreuve, liste_epreuve = menu_epreuves(liste_epreuve)
        joueur_choisi = choisir_joueur(equipe)
        #Initialisation de la variable booléenne à False puis lancement de l'épreuve en fonction du choix du joueur.
        #S'il réussi, resultat vaut True.
        resultat = False
        match num_epreuve:
            case 'Epreuve de Mathématiques':
                resultat = epreuve_math()
            case 'Epreuve de Logique':
                resultat = jeu_tictactoe()
            case 'Epreuve du hasard':
                resultat = epreuve_hasard()
            case 'Epreuve du pendu':
                resultat = jeu_pendu()
            case 'Enigme du Père Fourras':
                resultat = enigme_pere_fouras()
        #Si resultat vaut True, en l'enregistre dans l'historique et affiche le nombre de clé(s) gagnée.
        if resultat:
            enregistrer_historique(joueur_choisi["nom"], joueur_choisi["profession"], 1, 0)
            clef += 1
        if clef == 1:
            print("Vous avez maintenant", clef, "clé.\n")
        else:
            print("Vous avez maintenant", clef, "clés.\n")
        #Décrémentation du nombre de jeu que le joueur peu faire pour obtenir les 3 clés.
        compteur_epreuve -= 1
    #Si le joueur a obtenu au moins 3 clés, il accède à la "salle du trésor" et s'il réussi un message de victoire est affiché.
    #L'historique est également mis à jour.
    if clef >= 3:
        if salle_De_Tresor():
            print("Encore bravo, vous gagnez le jeu.")
            for i in range(len(equipe)):
                enregistrer_historique(equipe[i]["nom"], equipe[i]["profession"], 0, 1)
        else:
            print("Désolé, vous perdez malheureusement le jeu.")
    else:
        print("\nDésolé, vous ne pouvez pas accéder à la salle du trésor car vous n'avez pas trois clés.\nVous perdez malheureusement le jeu.")

if __name__ == '__main__':
    jeu()