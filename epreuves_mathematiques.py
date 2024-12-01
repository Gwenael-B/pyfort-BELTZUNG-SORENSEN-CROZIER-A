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
#Cette fonction permet de
def resoudre_equation_lineaire():
    a = random.randint(1,10)
    b = random.randint(1,10)
    x = (-b)/a
    return a, b, x

def epreuve_math_equation():
    a, b, x = resoudre_equation_lineaire()
    print("Résoudre l'équation ", a, "x +", b, "= 0.\n")
    while True:
        try:
            reponse = float(input("Quelle est la valeur de x : "))
            break
        except ValueError:
            print("Votre réponse n'est pas valide.\n")
    if reponse == x: #Comment faire si réponse avec plus de x décimales ?
        print("Correct! Vous gagnez une clé.")
        return True
    else:
        print("Incorrect! Vous ne gagnez pas la clé, la réponse était : ", x)
        return False

def est_premier(n):
    multiple = 0
    for i in range(2, n):
        if n % i == 0:
            multiple = 1
    if multiple == 1:
        return False
    else:
        return True

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

def epreuve_math_premier():
    n = random.randint(10,20)
    reponse_machine = premier_plus_proche(n)
    print("Trouver le nombre premier le plus proche de ", n)
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

def epreuve_roulette_mathematique():
    Liste_nb_roulette = []
    for i in range(5):
        Liste_nb_roulette.append(random.randint(1,20))
    operation = random.choice(["addition", "soustraction", "multiplication"])
    if operation == "addition":
        reponse_machine = Liste_nb_roulette[0]
        for i in range(1,5):
            reponse_machine = reponse_machine + Liste_nb_roulette[i]
    elif operation == "soustraction":
        reponse_machine = Liste_nb_roulette[0]
        for i in range(1,5):
            reponse_machine = reponse_machine - Liste_nb_roulette[i]
    else:
        reponse_machine = Liste_nb_roulette[0]
        for i in range(1, 5):
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

if __name__ == '__main__':
    epreuve_math()