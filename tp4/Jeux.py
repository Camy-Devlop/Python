   
#! /usr/bin/python3

from random import shuffle as molo
from Module.joueur import Joueur
from Module.paquet import Un_paquet_cartes

# c'est un vieux jeux UNO que je voudrais realiser 
#petit defi perso

class main:
    
    print("hello bienvenue au jeux")
    m=Un_paquet_cartes()
    j=Joueur()
    print("ok")
    
    m.get_carte(0)
    
    m.cree_carte_special_couleur()
    m.get_nombre_carte()
    m.cree_carte_special()
    m.get_nombre_carte()
    m.get_carte(102)