
from random import shuffle as molo
from Module.joueur import Joueur
from Module.regle import Regle
from Module.paquet import Un_paquet_cartes
class Table_jeux:
    
    couleur_demander:str
    joueurs:Joueur=[Joueur(),Joueur("CamyBot")]
    reg=Regle()
    paquet=Un_paquet_cartes()
    paquet.cree_carte_special_couleur()
    paquet.cree_carte_special()
    def __init__(self):
        pass

    