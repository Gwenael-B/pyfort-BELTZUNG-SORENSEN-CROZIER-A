import random

def epreuve_math():
    nom_epreuve=random.choice(["equation_lineaire", "nombre_premier", "roulette_mathematique"])
    if nom_epreuve == "equation_lineaire":
        epreuve_math_equation()
    elif nom_epreuve == "nombre_premier":
        epreuve_math_equation()
    else:
        epreuve_math_equation()

def resoudre_equation_lineaire():
    a = random.randint(1,10)
    b = random.randint(1,10)
    x = (-b)/a
    return(a, b, x)

def epreuve_math_equation():
    a, b, x=resoudre_equation_lineaire()
    print("Résoudre l'équation ", a, "x +", b,
          "= 0.\nQuelle est la valeur de x :", end=" ")
    reponse = float(input())
    if reponse == x: #Comment faire si réponse avec plus de x décimales ?
        print("Correct! Vous gagnez la clé.")
        return True
    else:
        print("Incorrect! Vous ne gagnez pas la clé, la réponse était : ", x)
        return False

epreuve_math()