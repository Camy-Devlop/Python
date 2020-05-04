   
#! /usr/bin/python3

from random import shuffle as molo
from Module.joueur import Joueur
from Module.paquet import Un_paquet_cartes
from Module.regle import Regle
from Module.carte import Carte
# c'est un vieux jeux UNO que je voudrais realiser 
#petit defi perso

class main:
    
    print("hello bienvenue au jeux")
    m=Un_paquet_cartes()
    j=Joueur()
    print("ok")
    
    m.cree_carte_special_couleur()
    m.cree_carte_special()

    reg=Regle()
    carte1=Carte("bleu",3)
    carte2=Carte("jaune",9)
    print(reg.verifie_deposer(carte1,carte2))
