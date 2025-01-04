#epreuves_logiques.py, pyfort-BELTZUNG-SORENSEN-CROZIER-A, CROZIER Clarence. Ce fichier importe le module random.
#Il contient toutes les fonctions permettant le bon fonctionnement du jeu du tic tac toe

import random

#Cette fonction permet d'afficher la grille. Elle prend en argument la grille et l'affiche. Elle ne retourne donc aucun résultat.
def afficher_grille(grille):
    for i in range(3):
        print(grille[i][0], '|',grille[i][1],'|',grille[i][2],"\n",end="")
        if i !=2:  #Cette condition empêche l'affichage de la ligne de tirets à la fin du quadrillage.
            print('----------',"\n",end="")

#Cette fonction vérifie si toutes les cases sont remplies par des symboles, c'est-à-dire si elles sont toutes différentes du
# symbole espace. Elle prend donc en entrée la grille puis retourne True si toutes les cases du jeu sont remplies ou False s'il
# reste des cases ne contenant pas de symbole.
def grille_complete(grille):
    for i in range(3):
        for j in range(3):
            if grille[i][j] == " ":
                return False
    return True

#Cette fonction vérifie la victoire pour un symbole particulier soit 3 symboles identiques sur une ligne/colonne/diagonale.
# Elle prend en entrée la grille ainsi que le symbole à vérifier. Elle retourne True si le symbole demandé a gagné et False s'il n'a pas gagné
def verifier_victoire(grille, symbole):
    cpt = 0
    for i in range(3):  #La boucle vérifie pour la diagonale principale
        if grille[i][i] == symbole :
            cpt = cpt + 1
    if cpt == 3:
        return True
    for i in range(3):  #La boucle vérifie pour les lignes
        cpt = 0
        for j in range(3):
            if grille[i][j] == symbole :
                cpt = cpt + 1
        if cpt == 3 :
            return True
    for i in range(3):  #La boucle vérifie pour les colonnes
        cpt = 0
        for j in range(3):
            if grille[j][i] == symbole :
                cpt = cpt + 1
        if cpt == 3 :
            return True
    cpt = 0
    for i in range(2,-1,-1):  #La boucle vérifie pour l'antidiagonale
         if grille[2-i][i] == symbole :
            cpt = cpt + 1
    if cpt == 3:
        return True
    return False

#Cette fonction choisit le coup du maître du jeu d'abord pour gagner, puis pour contrer le joueur, puis un coup au hasard
# si aucun des coups auparavant n'est possible. Elle prend donc comme arguments la grille ainsi que le symbole utilisé par
# le maître et elle retourne la position du coup du maître sous la forme d'un tuple.
def coup_maitre(grille,symbole):
    for i in range(3):  #Cette boucle vérifie si deux symboles identiques sont sur une même ligne et que la troisième case est vide : dans ce cas-là il renvoie les coordonnées de la case vide pour le coup gagnant
        if (grille[i][0] == symbole and grille[i][1] == symbole and grille[i][2] == ' ') or (grille[i][1] == symbole and grille[i][2] == symbole and grille[i][0] == ' ') or (grille[i][0] == symbole and grille[i][2] == symbole and grille[i][1] == ' '):
            a = i,grille[i].index(' ')
            return a
    for i in range(3):  #Cette boucle vérifie si deux symboles identiques sont sur une même colonne et que la troisième case est vide : dans ce cas-là il renvoie les coordonnées de la case vide pour le coup gagnant
        if (grille[0][i] == symbole and grille[1][i] == symbole and grille[2][i] == ' ') or (grille[1][i] == symbole and grille[2][i] == symbole and grille[0][i] == ' ') or (grille[0][i] == symbole and grille[2][i] == symbole and grille[1][i] == ' '):
            for j in range(3):
                if grille[j][i] == ' ':
                    a = j,i
                    return a
    # Cette boucle vérifie si deux symboles identiques sont sur la diagonale principale et que la troisième case est vide : dans ce cas-là il renvoie les coordonnées de la case vide pour le coup gagnant
    if (grille[0][0] == symbole and  grille[1][1] == symbole and grille[2][2] == ' ') or (grille[0][0] == symbole and grille[2][2] == symbole and grille[1][1] == ' ') or (grille[1][1] == symbole and  grille[2][2] == symbole and grille[0][0] == ' ') :
        for i in range(3):
            if grille[i][i] == ' ':
                a = i,i
                return a
    # Cette boucle vérifie si deux symboles identiques sont sur l'antidiagonale et que la troisième case est vide : dans ce cas-là il renvoie les coordonnées de la case vide pour le coup gagnant
    if (grille[0][2] == symbole and  grille[1][1] == symbole and grille[2][0] == ' ') or (grille[0][2] == symbole and grille[2][0] == symbole and grille[1][1] == ' ') or (grille[1][1] == symbole and  grille[2][0] == symbole and grille[0][2] == ' ') :
        for i in range(2,-1,-1):
            if grille [2-i][i] == ' ':
                a = 2-i,i
                return a
    if symbole == 'O':  #Cette condition échange le symbole pour prendre le symbole du joueur at ainsi vérifier les mêmes possibilités du dessus mais pour bloquer le joueur
        symbole = 'X'
    else:
        symbole = 'O'
    for i in range(3):  #Cette boucle vérifie si deux symboles identiques sont sur une même ligne et que la troisième case est vide : dans ce cas-là il renvoie les coordonnées de la case vide pour contrer le joueur
        if (grille[i][0] == symbole and grille[i][1] == symbole and grille[i][2] == ' ') or (grille[i][1] == symbole and grille[i][2] == symbole and grille[i][0] == ' ') or (grille[i][0] == symbole and grille[i][2] == symbole and grille[i][1] == ' '):
            a = i,grille[i].index(' ')
            return a
    for i in range(3):  #Cette boucle vérifie si deux symboles identiques sont sur une même colonne et que la troisième case est vide : dans ce cas-là il renvoie les coordonnées de la case vide pour contrer le joueur
        if (grille[0][i] == symbole and grille[1][i] == symbole and grille[2][i] == ' ') or (grille[1][i] == symbole and grille[2][i] == symbole and grille[0][i] == ' ') or (grille[0][i] == symbole and grille[2][i] == symbole and grille[1][i] == ' '):
            for j in range(3):
                if grille[j][i] == ' ':
                    a = j,i
                    return a
    # Cette boucle vérifie si deux symboles identiques sont sur la diagonale et que la troisième case est vide : dans ce cas-là il renvoie les coordonnées de la case vide pour contrer le joueur
    if (grille[0][0] == symbole and  grille[1][1] == symbole and grille[2][2] == ' ') or (grille[0][0] == symbole and grille[2][2] == symbole and grille[1][1] == ' ') or (grille[1][1] == symbole and  grille[2][2] == symbole and grille[0][0] == ' ') :
        for i in range(3):
            if grille[i][i] == ' ':
                a = i,i
                return a
    # Cette boucle vérifie si deux symboles identiques sont sur l'antidiagonale et que la troisième case est vide : dans ce cas-là il renvoie les coordonnées de la case vide pour contrer le joueur
    if (grille[0][2] == symbole and  grille[1][1] == symbole and grille[2][0] == ' ') or (grille[0][2] == symbole and grille[2][0] == symbole and grille[1][1] == ' ') or (grille[1][1] == symbole and  grille[2][0] == symbole and grille[0][2] == ' ') :
        for i in range(2,-1,-1):
            if grille [2-i][i] == ' ':
                a = 2-i,i
                return a
    while 1 != 2 :  #Cette boucle infinie génère deux nombres aléatoirement : les coordonnées d'une case et vérifie qu'il n'y a aucun symbole sur cette case et renvoie alors les coordonnées de cette case
        a = random.randint(0,2)
        b = random.randint(0,2)
        if grille[a][b] == ' ':
            break
    c = a,b
    return c

#Cette fonction crée le tour du maître du jeu. Elle prend comme argument la grille et le symbole du maître du jeu. Elle
# appelle la fonction coup_maître pour connaître l'emplacement du coup à jouer puis modifie la grille pour le jouer
# et enfin affiche la grille modifiée en appelant la fonction afficher_grille
def tour_maitre(grille, symbole):
    coup = coup_maitre(grille, 'X')  #Cette variable récupère les coordonnées du coup à jouer grâce à la fonction du dessus
    grille[coup[0]][coup[1]] = symbole
    afficher_grille(grille)

#Cette fonction exécute le tour du joueur. Elle prend en argument la grille ainsi que le symbole du joueur. Elle
# ne retourne rien mais affiche juste la grille avec la fonction afficher_grille
def tour_joueur(grille, symbole):
    liste_coup = ["3", "1", "2"]  #Initialise la seule liste de coups possibles
    while True:  #Cette boucle infinie permet de vérifier que le coup du joueur est correct
        coup = input("Pour jouer, entrez les coordonnées de votre coup (1, 2 ou 3) sous forme ligne,colonne : ")
        if len(coup) == 3 and (coup[0] in liste_coup and coup[2] in liste_coup) and coup[1] == ',':  #Cette condition vérifie que le coup du joueur comporte bien deux caractères qui sont dans la liste de coups possibles
            if grille[int(coup[0])-1][int(coup[2])-1] == " ":  #Cette condition vérifie que le coup du joueur tombe sur une case vide
                break  #Si c'est le cas, nous sortons de la boucle
            else:
                print("Erreur, vous ne pouvez pas mettre de symbole dans cette case, il y en a déjà un. Veuillez recommencer : ")
        else:
            print("Erreur, veuillez entrez deux chiffres valides 1, 2 ou 3 séparés par une virgule : ")
    grille[int(coup[0])-1][int(coup[2])-1] = symbole  #Modifie la grille en ajoutant le coup du joueur
    afficher_grille(grille)

#Cette fonction vérifie si une condition de victoire ou d'égalité est réalisée. Elle prend en argument la grille
# et les symboles du maitre et du joueur. Elle appelle les fonctions verifier_victoire et grille_complete pour
# vérifier si une condition de victoire a été accomplie, si oui elle retourne True sinon False
def verifier_resultat(grille, symbole_joueur, symbole_maitre):
    if verifier_victoire(grille, symbole_joueur) or grille_complete(grille) or verifier_victoire(grille, symbole_maitre) :
        return True
    else:
        return False

#Cette fonction orchestre l'ensemble du jeu. Elle ne prend pas d'argument, return True si le joueur gagne et False
# s'il perd ou s'il y a égalité. Elle appelle toutes les fonctions précédentes pour permettre le bon fonctionnement du jeu
def jeu_tictactoe():
    grille = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]  #Initialisation de la grille vide
    print("Bienvenue au jeu du morpion. Le jeu va maintenant débuter.")
    symbole_joueur = input("Choisissez votre symbole entre O et X : ")
    while (symbole_joueur != 'O') and (symbole_joueur != 'X'): #Cette boucle permet au joueur de choisir le symbole qu'il veut utiliser et sécurise la saisie
        symbole_joueur = input("Erreur, veuillez choisir un symbole correct : ")
    if symbole_joueur == 'X':  #Cette condition permet de donner au maître du jeu le symbole restant
        print("Très bien, le symbole du maître du jeu sera donc O.")
        symbole_maitre = 'O'
    else:
        print("Très bien, le symbole du maître du jeu sera donc X.")
        symbole_maitre = 'X'
    while not(verifier_resultat(grille, symbole_joueur, symbole_maitre)):  #Cette boucle tourne tant qu'aucune condition de victoire ou d'égalité n'a été accomplie
        tour_joueur(grille,symbole_joueur)
        if verifier_resultat(grille, symbole_joueur, symbole_maitre):  #Cette condition vérifie si quelqu'un a gagné le jeu ou s'il y a eu égalité : dans ce cas-là on rentre dans la boucle pour trouver le gagnant
            if verifier_victoire(grille, symbole_joueur):
                print("Bravo vous gagnez le morpion et vous remportez la clé !")
                return True
            elif grille_complete(grille):
                print("Egalité ! Vous ne gagnez pas la clé !")
                return False
            else:
                print("Dommage vous avez perdu, vous ne gagnez pas la clé !")
                return False
        print("Voici le coup du maître du jeu : ")
        tour_maitre(grille,symbole_maitre)
        if verifier_resultat(grille, symbole_joueur, symbole_maitre):  #Cette condition à la sortie de la boucle permet de trouver le gagnant du morpion
            if verifier_victoire(grille,symbole_maitre):
                print("Dommage vous avez perdu, vous ne gagnez pas la clé !")
                return False