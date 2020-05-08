from Module.carte import Carte

#class de carte special qui permet de diferencier la carte nomal de la carte ex: changement de couleur 
class Carte_special(Carte):
        
        def __init__(self, couleur, val=None):
                super().__init__(couleur, val=val)
                self.couleur:str=couleur

        #methode pour changer la couleur 
        def set_couleur(self,couleur_demander:str):
            self.couleur=couleur_demander
       
        #methode pour demander au joueur quelle couleur il veut pour  pour la carte special 
        def get_carte(self) -> str:
            self.couleur=input("Quelle est la couleur de la carte : ")
            self.affiche_carte()
            return self.couleur
        
        #affiche la carte demander 
        def affiche_carte(self):
            print(self.couleur)