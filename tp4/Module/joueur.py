from Module.carte import Carte
class Joueur:
    
    couleur_depart:str=None
    
    #Constructeur un bot robot qui va jouer
    def __init__(self,nom="TomBot"):
        self.bot=nom
        self.paquet:Carte=[]
        print("je suis pres a jouer je suis {}".format(self.bot))

    def depose_carte(self,carte_sur_table:Carte):
        pass

    def set_couleur_demander(self,couleur:str):
        self.couleur_depart=couleur

    def set_recoit_carte(self,carte:Carte=[]):
        for c in carte:
            self.paquet_recut.append(c)

    def set_recevoir_carte(self,carte:Carte=[]):
        """
        methode qui va recevoir des nouvelles cartes pour les ajouter au joueur  
        """
        self.paquet=self.paquet+carte