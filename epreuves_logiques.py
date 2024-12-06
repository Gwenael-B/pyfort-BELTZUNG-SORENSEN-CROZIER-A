import random

def afficher_grille(grille):
    for i in range(3):
        print(grille[i][0], '|',grille[i][1],'|',grille[i][2],"\n",end="")
        if i !=2:
            print('----------',"\n",end="")

def grille_complete(grille):
    for i in range(3):
        for j in range(3):
            if grille[i][j] == " ":
                return False
    return True

def verifier_victoire(grille, symbole):
    cpt = 0
    for i in range(3):
        if grille[i][i] == symbole :
            cpt = cpt + 1
    if cpt == 3:
        return True
    for i in range(3):
        cpt = 0
        for j in range(3):
            if grille[i][j] == symbole :
                cpt = cpt + 1
        if cpt == 3 :
            return True
    for i in range(3):
        cpt = 0
        for j in range(3):
            if grille[j][i] == symbole :
                cpt = cpt + 1
        if cpt == 3 :
            return True
    cpt = 0
    for i in range(2,-1,-1):
         if grille[2-i][i] == symbole :
            cpt = cpt + 1
    if cpt == 3:
        return True
    return False

def coup_maitre(grille,symbole):
    for i in range(3):
        if (grille[i][0] == symbole and grille[i][1] == symbole and grille[i][2] == ' ') or (grille[i][1] == symbole and grille[i][2] == symbole and grille[i][0] == ' ') or (grille[i][0] == symbole and grille[i][2] == symbole and grille[i][1] == ' '):
            a = i,grille[i].index(' ')
            return a
    for i in range(3):
        if (grille[0][i] == symbole and grille[1][i] == symbole and grille[2][i] == ' ') or (grille[1][i] == symbole and grille[2][i] == symbole and grille[0][i] == ' ') or (grille[0][i] == symbole and grille[2][i] == symbole and grille[1][i] == ' '):
            for j in range(3):
                if grille[j][i] == ' ':
                    a = j,i
                    return a
    if (grille[0][0] == symbole and  grille[1][1] == symbole and grille[2][2] == ' ') or (grille[0][0] == symbole and grille[2][2] == symbole and grille[1][1] == ' ') or (grille[1][1] == symbole and  grille[2][2] == symbole and grille[0][0] == ' ') :
        for i in range(3):
            if grille[i][i] == ' ':
                a = i,i
                return a
    if (grille[0][2] == symbole and  grille[1][1] == symbole and grille[2][0] == ' ') or (grille[0][2] == symbole and grille[2][0] == symbole and grille[1][1] == ' ') or (grille[1][1] == symbole and  grille[2][0] == symbole and grille[0][2] == ' ') :
        for i in range(2,-1,-1):
            if grille [2-i][i] == ' ':
                a = 2-i,i
                return a
    if symbole == 'O':
        symbole == 'X'
    for i in range(3):
        if (grille[i][0] == symbole and grille[i][1] == symbole and grille[i][2] == ' ') or (grille[i][1] == symbole and grille[i][2] == symbole and grille[i][0] == ' ') or (grille[i][0] == symbole and grille[i][2] == symbole and grille[i][1] == ' '):
            a = i,grille[i].index(' ')
            return a
    for i in range(3):
        if (grille[0][i] == symbole and grille[1][i] == symbole and grille[2][i] == ' ') or (grille[1][i] == symbole and grille[2][i] == symbole and grille[0][i] == ' ') or (grille[0][i] == symbole and grille[2][i] == symbole and grille[1][i] == ' '):
            for j in range(3):
                if grille[j][i] == ' ':
                    a = j,i
                    return a
    if (grille[0][0] == symbole and  grille[1][1] == symbole and grille[2][2] == ' ') or (grille[0][0] == symbole and grille[2][2] == symbole and grille[1][1] == ' ') or (grille[1][1] == symbole and  grille[2][2] == symbole and grille[0][0] == ' ') :
        for i in range(3):
            if grille[i][i] == ' ':
                a = i,i
                return a
    if (grille[0][2] == symbole and  grille[1][1] == symbole and grille[2][0] == ' ') or (grille[0][2] == symbole and grille[2][0] == symbole and grille[1][1] == ' ') or (grille[1][1] == symbole and  grille[2][0] == symbole and grille[0][2] == ' ') :
        for i in range(2,-1,-1):
            if grille [2-i][i] == ' ':
                a = 2-i,i
                return a
    while 1 != 2 :
        a = random.randint(0,2)
        b = random.randint(0,2)
        if grille[a][b] == ' ':
            break
    c = a,b
    return c

def tour_maitre(grille, symbole):
    coup = coup_maitre(grille, 'X')
    grille[coup[0]][coup[1]] = symbole
    afficher_grille(grille)

def tour_joueur(grille,symbole):
    coup = int(input("Pour jouer, entrez les coordonnées de votre coup sous forme : ligne, colonne : "))




grille = [[' ','X',' '],[' ','X',' '],[' ',' ',' ']]
tour_joueur(grille,'X')