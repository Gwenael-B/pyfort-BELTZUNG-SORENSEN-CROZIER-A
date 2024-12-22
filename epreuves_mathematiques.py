import random

#Cette fonction permet de sélectionner au hasard une des trois épreuves de maths.
def epreuve_math():
    epreuves = ["equation_lineaire", "nombre_premier", "roulette_mathematique"]
    epreuve = random.choice(epreuves)
    if epreuve == "equation_lineaire":
        epreuve_math_equation()
    elif epreuve == "nombre_premier":
        epreuve_math_premier()
    else:
        epreuve_roulette_mathematique()

#Première épreuve de math : résolution d'équation linéaire.
#Cette fonction permet de générer aléatoirement deux entiers a et b compris ente 1 et 10 inclus grâce à la fonction
# random.randint() et de déterminer la valeur de x telle que ax+b = 0, elle renvoie ensuite a, b et x.
def resoudre_equation_lineaire():
    a = random.randint(1,10)
    b = random.randint(1,10)
    x = (-b)/a
    #Pour qu'il n'y ait que 2 chiffres après la virgule.
    x = x * 100
    x = (int(x))/100
    return a, b, x

#Cette fonction appelle la fonction resoudre_equation_lineaire() pour obtenir a, b et x,
# elle s'assure ensuite que la saisie de l'utilisateur est correcte puis compare ce résultat à celui
# trouvé par l'algorithme. Si le résultat est le même, la fonction retourne True sinon False.
def epreuve_math_equation():
    a, b, x = resoudre_equation_lineaire()
    print("Résoudre l'équation ", a, "x +", b, "= 0.\n")
    while True:
        try:
            reponse = float(input("Quelle est la valeur de x à deux chiffres après la virgule sans arrondi: "))
            break
        except ValueError:
            print("Votre réponse n'est pas valide.\n")
    if reponse == x:
        print("Correct! Vous gagnez une clé.")
        return True
    else:
        print("Incorrect! Vous ne gagnez pas la clé, la réponse était : ", x)
        return False

#Deuxième épreuve de math : détermination du nombre premier (supérieur ou égale) le plus proche d'un entier n.

#Cette fonction permet de définir si un entier n passé en paramètre est un nombre premier.
def est_premier(n):
    multiple = 0
    for i in range(2, n):
        if n % i == 0:
            multiple = 1
    if multiple == 1:
        return False
    else:
        return True

#Cette fonction appelle la fonction est_premier(n) et permet de retourner le nombre premier supérieur ou égal à n
# le plus proche.
def premier_plus_proche(n):
    if est_premier(n):
        return n
    elif n>= 20:
        return 23
    elif n>= 18:
        return 19
    elif n>= 14:
        return 17
    elif n>= 12:
        return 13
    else:
        return 11

#Cette fonction permet de générer un entier n compris entre 10 et 20 inclus grâce à la fonction random.randint(),
# elle s'assure ensuite que la saisie de l'utilisateur est correcte puis compare ce résultat à celui
# trouvé par l'algorithme. Si le résultat est le même, la fonction retourne True sinon False.
def epreuve_math_premier():
    n = random.randint(10,20)
    reponse_machine = premier_plus_proche(n)
    print("Trouver le nombre premier supérieur ou égale le plus proche de ", n)
    while True:
        try:
            reponse_candidat = int(input("Votre réponse : "))
            break
        except ValueError:
            print("Votre réponse n'est pas valide.\n")
    if reponse_candidat == reponse_machine:
        print("Correct! Vous gagnez une clé.")
        return True
    else:
        print("Incorrect! Vous ne gagnez pas la clé, la réponse était : ", reponse_machine)
        return False

#Troisième épreuve de math : roulette mathematique, calculs entre 5 entiers (addition, soustraction ou multiplication).

#Cette fonction permet de créer une liste de 5 entiers compris entre 1 et 20 inclus grâce à la fonction random.randint(),
# elle permet ensuite de choisir aléatoirement entre l'addition, la soustraction ou la multiplication grâce à la
# fonction random.choice(), elle calcule ensuite les opérations demandées puis elle s'assure que la saisie
# de l'utilisateur est correcte et compare ce résultat à celui trouvé par l'algorithme,
# si le résultat est le même, la fonction retourne True sinon False.
def epreuve_roulette_mathematique():
    Liste_nb_roulette = []
    for i in range(5):
        Liste_nb_roulette.append(random.randint(1,20))
    operation = random.choice(["addition", "soustraction", "multiplication"])
    #Initialisation variable reponse_machine.
    reponse_machine = Liste_nb_roulette[0]
    #Calcule réponse machine en fonction de l'opération.
    for i in range(1,5):
        if operation == "addition":
            reponse_machine = reponse_machine + Liste_nb_roulette[i]
        elif operation == "soustraction":
            reponse_machine = reponse_machine - Liste_nb_roulette[i]
        else:
            reponse_machine = reponse_machine * Liste_nb_roulette[i]
    print("Nombres sur la roulette : ", Liste_nb_roulette[:], "\nCalculer le résultat en combinant ces nombres avec une ", operation)
    while True:
        try:
            reponse_candidat = int(input("Votre réponse : "))
            break
        except ValueError:
            print("Votre réponse n'est pas valide.\n")
    if reponse_candidat == reponse_machine:
        print("Correct! Vous gagnez une clé.")
        return True
    else:
        print("Incorrect! Vous ne gagnez pas la clé, la réponse était : ", reponse_machine)
        return False