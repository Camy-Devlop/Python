   
#! /usr/bin/python3

from random import shuffle as molo
from Module.joueur import Joueur
from Module.paquet import Un_paquet_cartes


class main:
    
    print("hello bienvenue au jeux")
    m=Un_paquet_cartes()
    j=Joueur()
    print("ok")
    
    m.get_carte(0)
    m.get_nombre_carte()