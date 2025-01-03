**1. Présentation Générale**  
-----------------------------
**Titre du Projet :** pyfort-BELTZUNG-SORENSEN-CROZIER-A  

**Contributeurs :**
- BELTZUNG-SÖRENSEN Gwenaël : développeur
- CROZIER Clarence : développeur

**Description :** Simulation de Fort-Boyard avec différentes épreuves portant sur les mathématiques, le hasard et la logique.

**Fonctionnalités Principales :** Adaptation du jeu télévisé Fort-Boyard avec une interface en ligne de commande qui permet de constituer une équipe.
Pour l’épreuve de mathématiques, il y a une épreuve où nous devons résoudre une équation, une où il faut déterminer un nombre premier supérieur le plus proche d’un nombre et enfin, une roulette où il faut additionner, soustraire ou multiplier 3 nombres. Une de ces trois épreuves est choisie de manière aléatoire.
Pour l’épreuve du père Fouras, une énigme est posée et le joueur a 3 tentatives pour trouver la bonne réponse.
Pour 

**Technologies Utilisées :** Langage python avec l’utilisation des librairies random et json.

**Installation :** Ouvrez PyCharm, depuis l'écran d'accueil, cliquez sur "Get from Version Control" (ou allez dans File > Project from Version Control > Git). Dans le champ "URL", collez l'URL de votre repository GitHub que vous avez copiée, sélectionnez un dossier local où cloner le projet et cliquez sur "Clone". 
Installer un éditeur python, par exemple pycharm : https://www.jetbrains.com/fr-fr/pycharm/download/?section=windows	
	
**Utilisation :** Double clique sur le fichier main.py


**2. Documentation Technique** 
-----------------------------
**Algorithme du Jeu :** 
1. execution du fichier main.py.
2. Création de l’équipe avec le nombre de joueurs, leur nom et profession ainsi que la détermination du leader.
3. Affichage des propositions des différentes épreuves et sélection du joueur.
4. Lancement de l’épreuve et déroulement de cette dernière, si le joueur réussi, l’épreuve return true sinon false.
5. Répétition de l’étape précédente jusqu'à ce que l’équipe aie 3 clefs ou 4 tentatives sans avoir eu les 3 clefs nécessaires.
6. Si 3 clefs sont remportées, lancement de l’épreuve finale : la salle de trésor.
7. Si les 3 clefs n'ont pas été remportées, affichage d’un message de défaite et arrêt du jeu.
8. Si l’équipe a trouvé la solution de la salle du trésor, affichage d’un message de victoire et arrêt du jeu.
9. Si l’équipe n’a pas trouvé la solution de la salle du trésor, affichage d’un message de défaite et arrêt du jeu.

**Details des fonctions implémentées :** 

**Gestion des Entrées et Erreurs :** 
Les erreurs dues aux entrées sont gérées grâce à une boucle “while True” qui vérifie si la saisie est correcte et si oui : ce qui a été saisie est retourné, si la saisie n’est pas correcte, un message d’erreurs est afficher et il est demandé à l’utilisateur d'entrer une valeur correcte selon les instructions données.
Nous avons également utilisé les chaînes de caractères, si la valeur saisie est différente des caractères demandés en entrée, un message d’erreurs est affiché et il est demandé à l’utilisateur d'entrer une valeur correcte selon les instructions données.


**3. Journal de Bord**
-----------------------------
**Chronologie du Projet :**  
30/11/24 : Création du projet sur le github  
01/12/24 : Première version des trois épreuves de mathématiques + première version des deux jeux de hasard  
06/12/24 : Première version jeu du morpion  
07/12/24 : Première version énigme père fouras  
18/12/24 : Première version fonctions utiles sans la fonction pour enregistrer l'historique + première version salle de trésor  
26/12/24 : Première version fonction pour enregistrer l'historique  
27/12/24 : Première version du jeu du pendu + correction d'erreurs pour choisir l'épreuve  
03/01/25 : Correction de bugs majeurs pour enregistrer l'historique  


**Répartition des Tâches :**  
BELTZUNG-SÖRENSEN Gwenaël : 
- épreuve mathématiques
- épreuve du père Fouras
- épreuve du pendu
- épreuve finale
- main

CROZIER Clarence :  
- épreuve logique
- épreuve hasard
- fonctions utiles

**4. Test et Validation**  
-----------------------------
**Stratégies de Test :** Tests avec des nombres négatifs, très grands, flottants, 0, des chaînes de caractères, des caractères spéciaux.
