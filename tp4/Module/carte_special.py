from Module.carte import Carte

class Carte_special(Carte):
        
        def __init__(self, couleur, val=None):
                super().__init__(couleur, val=val)
                self.couleur:str=couleur

        def set_couleur(self,couleur_demander:str):
            self.couleur=couleur_demander
       

        def get_carte(self) -> str:
            self.couleur=input("Quelle est la couleur de la carte : ")
            self.affiche_carte()
            return self.couleur

        def affiche_carte(self):
            print(self.couleur)