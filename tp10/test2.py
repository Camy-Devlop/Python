from random import randint

position = str


def alea_2_4():
    """
    la fonction alea sert a choisir un nombre entre 2,4 aleatoirement avec une probavilité de 1/50 pour 4 et 49/50 2
    :return:
    il return nb soit le nombre choisis entre 2 et 4 afin
    """
    al = randint(0, 20)
    if al == 1:
        nb = 4
    else:
        nb = 2
    return nb


def board():
    """
    la fonction board crée un "plateau" remplis de 0
    les variable i1 et i2 servent a choisir une ligne et une colonone aleatoirement afin de pourvoir afficher 2 nombre nb
    le while sert a verifier si les colignes des deux points sont bien differentes
    :return:
    il retourne un tableau 4*4 avec 2 valeurs du tableau qui sont soit a 2 ou 4 (valeur de nb) aleatoirement a chaque lancement de parti"
    """
    p = False
    grille = []
    for i in range(4):
        grille.append([0] * 4)
    ligne = randint(0, 3)
    colonne = randint(0, 3)
    grille[ligne][colonne] = alea_2_4()
    while p == False:
        ligne2 = randint(0, 3)
        colonne2 = randint(0, 3)
        if grille[ligne2][colonne2] == 0:
            grille[ligne2][colonne2] = alea_2_4()
            p = True

    return grille, colonne, ligne, colonne2, ligne2


def affichageboard(grille):
    for i in range(len(grille)):
        for a in range(len(grille[0])):
            print(grille[i][a], end="\t")
        print()


def deplacement(grille, position, c1, l1, c2, l2):
    colonnedroite = 3
    colonnegauche = 0
    ligne_haut = 0
    ligne_bas = 3
    if position == "droite":
        if grille[l1][c1] == grille[l2][c2] and l1==l2:
            grille[l1][c1],grille[l2][colonnedroite]= 0,grille[l2][c2]+1
            grille[l2][c2]=0

        elif grille[l1][colonnedroite]==0 and grille[l2][colonnedroite]==0 :
            grille[l1][colonnedroite], grille[l2][colonnedroite] = grille[l1][c1], grille[l2][c2]
            grille[l1][c1], grille[l2][c2] = 0, 0

        elif (grille[l1][colonnedroite]!=0 or grille[l2][colonnedroite]!=0) and (c1==colonnedroite or c2==colonnedroite):
            print("un des deux a droite ")

            if c1==colonnedroite:
                print(" 1ime solution ")
                grille[l1][c1], grille[l2][colonnedroite] = grille[l1][c1], grille[l2][c2]
                grille[l2][c2]=0
            else:
                print("deuxime solution ")
                grille[l1][colonnedroite], grille[l2][c2] = 0 , grille[l2][c2]


        c1 = colonnedroite
        c2 = colonnedroite

    if position == "gauche" :
        if grille[l1][c1] == grille[l2][c2] and l1==l2:
            grille[l1][c1], grille[l2][c2] = grille[l2][colonnegauche]+1, 0

        elif grille[l1][colonnegauche] == 0 and grille[l2][colonnegauche] == 0:
            grille[l1][colonnegauche], grille[l2][colonnegauche] = grille[l1][c1], grille[l2][c2]
            grille[l1][c1], grille[l2][c2] = 0, 0

        elif (grille[l1][colonnegauche]!=0 or grille[l2][colonnegauche]!=0) and (c1==colonnegauche or c2==colonnegauche):
            print("un des deux a gauche ")

            if c1==colonnegauche:
                print(" 1ime solution ")
                grille[l1][c1], grille[l2][colonnegauche] = grille[l1][c1], grille[l2][c2]
                grille[l2][c2]=0
            else:
                print("deuxime solution ")
                grille[l1][colonnegauche], grille[l2][c2] = grille[l1][c1] , grille[l2][c2]
                grille[l1][c1]=0



        c1 = colonnegauche
        c2 = colonnegauche

    if position == "haut":
        if grille[l1][c1] == grille[l2][c2] and c1==c2:
            print("valeur haut ",grille[l2][ligne_haut])
            grille[l1][c1], grille[ligne_haut][c2] =0, grille[l2][c2] + 1
            grille[l2][c2]=0

        elif grille[ligne_haut][c1] == 0 and grille[ligne_haut][c2] == 0:
            grille[ligne_haut][c1], grille[ligne_haut][c2] = grille[l1][c1], grille[l2][c2]
            grille[l1][c1], grille[l2][c2] = 0, 0

        l1 = ligne_haut
        l2 = ligne_haut

    if position == "bas":
        if grille[l1][c1] == grille[l2][c2] and c1==c2:
            grille[l1][c1], grille[ligne_bas][c2] = 0, grille[l2][c2] + 1
            grille[l2][c2] = 0

        l1 = ligne_bas
        l2 = ligne_bas
    print ("nouvelle coordonne",l1,c1,l2,c2 )
    return l1, c1, l2, c2 # ,colonnedroite, colonnegauche

def test(grille)->int :
    """
    fonction qui va voir combien de valeur il a y dans  la grille different de 0

    :param grille:
    :return: retourne le nombre de valeur de la grille different de 0
    """
    cptt=0
    for l in range(len(grille[0])):
        for ll in range(len(grille[0])):
           if grille[l][ll]>0:
               cptt+=1

    return cptt

def Nombre_max()->int:

    return None

def injecter_nombre() -> int :

    return None

def principal():
    game = True
    cpt:int =2 #compteur pour voir quelle est le nombre le plus grand dans la grille
    nouvelle_valeur:int=None
    grille, c1, l1, c2, l2 = board()

    print("ligne ", l1, " colone ", c1)
    print("ligne2 ", l2, " colone2 ", c2)
    affichageboard(grille)
    while game:
        position = str(input("entre position = "))

        l1,c1,l2,c2=deplacement(grille, position, c1, l1, c2, l2, )
        print("ligne ", l1, " colone ", c1)
        print("ligne2 ", l2, " colone2 ", c2)
        affichageboard(grille)

        if test(grille)<2:
            print("il ya plus qu'une valeur dans le tableau ")
            game=False



principal()

