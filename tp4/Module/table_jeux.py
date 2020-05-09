

from Module.joueur import Joueur
from Module.regle import Regle
from Module.paquet import Un_paquet_cartes
class Table_jeux:
    
    couleur_demander:str
    
    reg=Regle()
    paquet=Un_paquet_cartes()
    paquet.cree_carte_special_couleur()
    paquet.cree_carte_special()
    def __init__(self):
        self.joueurs:Joueur=[Joueur(),Joueur("CamyBot")]
        self.paquet.melanger_du_paquert()
        
    def get_carte1(self)-> Carte:
        """ 
            methode qui va donne une carte qui au dessus du paquet  
        """
        c=self.paquet.get_carte(1)
        return c