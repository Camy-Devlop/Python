from random import shuffle as molo


        
#! /usr/bin/python3

from joueur import Joueur
from paquet import Un_paquet_cartes
class main:
    
    print("hello bienvenue au jeux")
    m=Un_paquet_cartes()
    j=Joueur()
    print("ok")
    
    m.get_carte(0)
    m.get_nombre_carte()