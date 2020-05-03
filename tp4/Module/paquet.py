from Module.carte import Carte
class Un_paquet_cartes:
    
    list_color=["bleu","rouge","vert","jaune"]
    paquet=[]
    #les carte special le 2x , § changement sens
    # @ stop et le * depot de carte de meme couleur
    dico_spetial_couleur={"2￼x":2,"§":1,"@":2,"*":2}
    dico_special={"4c":4,"4c4x":1,"4c2x":4}

    def __init__(self,nombre=9):
        self.nombre=nombre
        self.cree_paquet()
   
    def cree_paquet(self):
        
        for ii in range(2):
            for c in self.list_color:
                for i in range(1,self.nombre+1):
                    self.paquet.append(Carte(c,i))
                    
    def get_carte(self,n):
        print(self.paquet[n])
    
    def get_nombre_carte(self):
        print(len(self.paquet))
        
    def cree_carte_special_couleur(self):
        for c in self.list_color:
            for key , val in self.dico_spetial_couleur.items():
                for v in range(val):
                    self.paquet.append(Carte(c,key))

    def cree_carte_special(self):
            for key , val in self.dico_special.items():
                for v in range(val):
                    self.paquet.append(Carte(key))
    