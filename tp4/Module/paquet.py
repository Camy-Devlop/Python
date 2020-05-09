from Module.carte import Carte
from random import shuffle as molo
class Un_paquet_cartes:
    
    # attibut qui va donnec les couleur des carte 
    list_color=["bleu","rouge","vert","jaune"]
    #liste de paquet de carte 
    paquet=[]
    #les carte special le 2x , § changement sens
    # @ stop et le * depot de carte de meme couleur
    dico_spetial_couleur={"2￼x":2,"§":1,"@":2,"*":2}
    dico_special={"4c":4,"4c4x":1,"4c2x":4}

    #constructeur va cree un paquet de carte 
    # le parametre nomnre va determiner nombre de carte entre 1 à 9 par defaut
    def __init__(self,nombre=9):
        self.nombre=nombre
        self.cree_paquet()
   
   #fonction qui va cree le paquer de carte
    def cree_paquet(self):
        for ii in range(2):
            for c in self.list_color:
                for i in range(1,self.nombre+1):
                    self.paquet.append(Carte(c,i))
                    
    
    def get_carte(self,n:int) -> Carte:
        """   Methode qui va distribuer le nombre de carte demander  
            au joueur et au cas ou le joueur ne sais pas deposer de carte
            elle va etre utilise comme une poche 
        """
        mini_paquet_n:Carte=[]
        for i in range(0,n):
            
            mini_paquet_n.append(self.paquet[n])
            self.paquet.pop(n)
        
        return mini_paquet_n
    
    #returne nombre de carte total 
    def get_nombre_carte(self):
        print(len(self.paquet))

    #fonction qui va cree les carte special avec des couleur  
    def cree_carte_special_couleur(self):
        for c in self.list_color:
            for key , val in self.dico_spetial_couleur.items():
                for v in range(val):
                    self.paquet.append(Carte(c,key))

    # fonction qui va cree ds carte special comme  a carte changement de couleur le carte changement de couleur Fois 4
    def cree_carte_special(self):
            for key , val in self.dico_special.items():
                for v in range(val):
                    self.paquet.append(Carte(key))
    
    def melanger_du_paquert(self):
        """ 
            methode qui va melanger le paquet de carte 
        """
        molo(self.paquet)
    
    def paquet_recupe(self,carte:Carte):
        