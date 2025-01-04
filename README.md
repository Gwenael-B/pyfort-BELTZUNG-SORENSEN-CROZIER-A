**1. Présentation Générale**  
-----------------------------
**Titre du Projet :** pyfort-BELTZUNG-SORENSEN-CROZIER-A  

**Contributeurs :**
- BELTZUNG-SÖRENSEN Gwenaël : développeur
- CROZIER Clarence : développeur

**Description :** Simulation de Fort-Boyard avec différentes épreuves portant sur les mathématiques, le hasard et la logique.

**Fonctionnalités Principales :** Adaptation du jeu télévisé Fort-Boyard avec une interface en ligne de commande qui permet de constituer une équipe.
Pour l’épreuve de mathématiques, il y a une épreuve de résolution d'équation, une où il faut déterminer un nombre premier supérieur ou égale le plus proche d’un nombre donné et enfin, une roulette où il faut additionner, soustraire ou multiplier 3 nombres. Une de ces trois épreuves est choisie de manière aléatoire.
Pour l’épreuve du père Fouras, une énigme est posée et le joueur a 3 tentatives pour trouver la bonne réponse.
Pour l'épreuve finale, trois indices sont donnés et le joueur a trois essais pour trouver le mot lié aux indices, s'il ne trouve pas, un indice de plus est affiché.
Pour l'épreuve du pendu, un mot est choisi de manière aléatoire et le joueur a 9 essais pour le trouver sinon il perd.
Pour l'épreuve de hasard une épreuve est choisie au hasard entre un lancé de dés ou un jeu du bonnetau, pour le lancer de dés, le joueur et le maître du jeu lancent tous deux deux dés et le premier à faire un 6 gagne, si au bout de 3 essais aucun n'a fait de 6, le joueur perd. Pour l'épreuve de bonnetau, le joueur doit déterminer en maximum trois essais sous quel bonnetau se cache la bille s'il trouve il gagne une clé sinon il perd.
Pour l'épreuve de logique le joueur doit jouer au morpion contre le maître du jeu, s'il gagne, il remporte une clé sinon il ne remporte rien.
Pour la fonction main et fonction utile, ces fichiers permettent le bon déroulement du jeu.
Un fichier historique.txt enregistre l'historique de jeu.

**Technologies Utilisées :** Langage python avec l’utilisation des librairies random et json.

**Installation :** Ouvrez PyCharm, depuis l'écran d'accueil, cliquez sur "Get from Version Control" (ou allez dans File > Project from Version Control > Git). Dans le champ "URL", collez l'URL de votre repository GitHub que vous avez copiée, sélectionnez un dossier local où clonez le projet et cliquez sur "Clone". 
Installez un éditeur python, par exemple pycharm : https://www.jetbrains.com/fr-fr/pycharm/download/?section=windows	
	
**Utilisation :** Ouvrez votre éditeur python puis appuyer sur run pour le fichier main.py.


**2. Documentation Technique** 
-----------------------------
**Algorithme du Jeu :** 
1. execution du fichier main.py.
2. Création de l’équipe avec le nombre de joueurs, leur nom et profession ainsi que la détermination du leader.
3. Affichage des propositions des différentes épreuves et sélection du joueur.
4. Lancement de l’épreuve et déroulement de cette dernière, si le joueur réussit, l’épreuve retourne true sinon false.
5. Répétition de l’étape précédente jusqu'à ce que l’équipe ait 3 clés ou 4 tentatives sans avoir eu les 3 clés nécessaires.
6. Si 3 clés sont remportées, lancement de l’épreuve finale : la salle de trésor.
7. Si les 3 clés n'ont pas été remportées, affichage d’un message de défaite et arrêt du jeu.
8. Si l’équipe a trouvé la solution de la salle du trésor, affichage d’un message de victoire et arrêt du jeu.
9. Si l’équipe n’a pas trouvé la solution de la salle du trésor, affichage d’un message de défaite et arrêt du jeu.

**Details des fonctions implémentées :**  
*Fonctions utiles :*  
- introduction() : Cette fonction affiche juste un message d'introduction pour signaler l'arrivée dans le jeu et son déroulement.  
- menu_épreuve(liste_epreuve) : Elle prend en argument la liste des épreuves disponibles pour permettre au joueur de choisir l'épreuve qu'il souhaite puis la supprime dans la liste des épreuves disponibles. La fonction retourne ensuite l'épreuve choisie par le joueur et la nouvelle liste des épreuves disponibles.  
- composer_equipe() : Elle ne prend pas d'argument en entrée et retourne la liste des dictionnaires des joueurs.  
- choisir_joueur(equipe) : Elle prend la liste des joueurs en argument et retourne le dictionnaire contenant toutes les informations du joueur choisi.  
- enregistrer_historique(nom, profession, nb_cle, nb_victoire) : Elle prend en argument le nom, la profession, le nombre de clés et de victoires d'un joueur mais elle ne retourne rien.  

*Enigme père Fouras :*  
- charger_enigmes(dossier) : Cette fonction prend en paramètre le nom du dossier et permet de charger toutes les données du fichier enigmesPF.json dans la variable 'donnes' et la retourne.  
- enigme_pere_fouras() : Elle ne prend pas d'argument en entrée et retourne True si le joueur gagne et False si le joueur perd.  

*Epreuve finale :*  
- salle_De_Tresor() : Elle ne prend pas d'argument en entrée et retourne True si le joueur gagne et False si le joueur perd.

*Epreuve jeu du pendu :*
- chargement_enigmes() : Fonction qui charge la liste de mots pour le pendu et la retourne.  
- remplace_lettre(lettre) : Transforme la lettre prise en paramètre et la retourne sans accent et en minuscule.  
- mot_simplifie(mot) : Transforme le mot pris en paramètre et le retourne sans accent et en minuscules.  
- saisie_choix_joueur() : Ne prend pas de paramètre en entrée et retourne le choix du joueur.  
- saisie_lettre_joueur() : Fonction qui vérifie que la lettre saisie par le joueur est correcte et la convertit en minuscules puis la renvoie.  
- saisie_mot_joueur() : Fonction qui saisit et convertit le mot final du joueur en minuscules et le retourne.  
- affichage_lettre_trouvees(lettres_utilisees, mot) : Cette fonction prend en entrée un mot et des lettres et retourne une chaine de caractères où sont présentes les lettres et leur position dans le mot.  
- affichage_pendu(tentatives) : Le paramètre correspond au nombre de tentatives et retourne un espace pour plus de lisibilité.  
- jeu_pendu() : Elle ne prend pas d'argument en entrée et retourne True si le joueur gagne et False si le joueur perd.

*Epreuve logique :*  
- afficher_grille(grille) : Elle prend en argument la grille et l'affiche. Elle ne retourne donc aucun résultat.  
- grille_complete(grille) : Elle prend en entrée la grille puis retourne True si toutes les cases du jeu sont remplies ou False s'il reste des cases ne contenant pas de symbole.  
- verifier_victoire(grille, symbole) : Elle prend en entrée la grille ainsi que le symbole à vérifier. Elle retourne True si le symbole demandé a gagné et False s'il n'a pas gagné.  
- coup_maitre(grille,symbole) : Elle prend comme arguments la grille ainsi que le symbole utilisé par le maître et elle retourne la position du coup du maître sous la forme d'un tuple.  
- tour_maitre(grille, symbole) : Elle prend comme arguments la grille et le symbole du maître du jeu. Elle ne retourne rien car elle affiche juste la grille mise à jour.  
- tour_joueur(grille, symbole) : Elle prend en arguments la grille ainsi que le symbole du joueur. Elle ne retourne rien mais affiche juste la grille.  
- verifier_resultat(grille, symbole_joueur, symbole_maitre) : Elle prend en arguments la grille et les symboles du maitre et du joueur. Elle retourne True si une condition de victoire a été accomplie sinon False.  
- jeu_tictactoe() : Elle ne prend pas d'argument en entrée et retourne True si le joueur gagne et False si le joueur perd.  

*Epreuve hasard :*  
- epreuve_hasard() : Elle ne prend pas d'argument et retourne la fonction du bonneteau ou du lancer de dès en l'exécutant.  
- bonneteau() : Elle ne prend pas d'argument en entrée et retourne True si le joueur gagne et False si le joueur perd.
- jeu_lance_des() : Elle ne prend pas d'argument en entrée et retourne True si le joueur gagne et False si le joueur perd.  

*Epreuve mathématique :*
- epreuve_math() : Elle ne prend pas d'argument et retourne la fonction de la résolution d'équation, du nombre premier ou de la roulette mathématique en l'exécutant.
- resoudre_equation_lineaire() : Elle ne prend pas d'argument et retourne a, x et b tel que ax+b=0.  
- epreuve_math_equation() : Elle ne prend pas d'argument en entrée et retourne True si le joueur gagne et False si le joueur perd.  
- est_premier(n) : Cette fonction permet de définir si un entier n passé en paramètre est un nombre premier et retourne True si oui sinon elle retourne False.  
- premier_plus_proche(n) : Elle retourne le nombre premier supérieur ou égal au paramètre n le plus proche.  
- epreuve_math_premier() : Elle ne prend pas d'argument en entrée et retourne True si le joueur gagne et False si le joueur perd.  
- epreuve_roulette_mathematique() : Elle ne prend pas d'argument en entrée et retourne True si le joueur gagne et False si le joueur perd.  

*main :*
- jeu() : C'est la fonction principale qui coordine le jeu, elle ne prend donc pas d'argument et ne retourne rien.  

**Gestion des Entrées et Erreurs :** 
Les erreurs dues aux entrées sont gérées grâce à une boucle “while True” qui vérifie si la saisie est correcte et si oui : ce qui a été saisi est retourné, si la saisie n’est pas correcte, un message d’erreur est affiché et il est demandé à l’utilisateur d'entrer une valeur correcte selon les instructions données.
Nous avons également utilisé les chaînes de caractères, si la valeur saisie est différente des caractères demandés en entrée, un message d’erreur est affiché et il est demandé à l’utilisateur d'entrer une valeur correcte selon les instructions données.


**3. Journal de Bord**
-----------------------------
**Chronologie du Projet :**  
30/11/24 : Création du projet sur le github  
01/12/24 : Première version des trois épreuves de mathématiques + première version des deux jeux de hasard  
06/12/24 : Première version jeu du morpion  
07/12/24 : Première version énigme père fouras  
18/12/24 : Première version fonctions utiles sans la fonction pour enregistrer l'historique + première version salle du trésor  
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
