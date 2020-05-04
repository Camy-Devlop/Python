from Module.carte import Carte
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
                    
    #affiche la carte qui stoker dans la liste paquet de carte appelle paquet
    def get_carte(self,n):
        print(self.paquet[n])
    
    def get_carte1(self,n:int):
        print(self.paquet[n])
    
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
    