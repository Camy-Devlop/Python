from random import shuffle as molo

class Carte:
    def __init__(self, couleur,val):
        self.couleur=couleur
        self.val=val
        
    def get_couleur(self):
        return self.couleur
        
    def get_val(self):
        return self.val
        
    def __str__(self):
        return self.get_couleur()+" "+str(self.get_val())
        
class Un_paquet_cartes:
    
    list_color=["bleu","rouge","vert","jaune"]
    paquet=[]
    #les carte special le 2x , § changement sens
    # @ stop et le * depot de carte de meme couleur
    list_spetial_couleur=["2￼x","§","@","*"]
    
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
        pass
    
    def cree_carte_special(self):
        pass
    
class Joueur:
    
    def __init__(self,nom="TomBot",carte=0):
        self.bot=nom
        self.cartes=carte
        print("je suis pres a jouer")


class main:
    
    print("hello bienvenue au jeux")
    m=Un_paquet_cartes()
    j=Joueur()
    print("ok")
    
    m.get_carte(0)
    m.get_nombre_carte()