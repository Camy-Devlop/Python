#class c'est la carte standar
class Carte:
    #constructeur qui resoit en parametre couleur et sa valeur qui situer entre 1 et 9 
    def __init__(self, couleur,val=None):
        self.couleur=couleur
        self.val=val
        
    #fonction qui donne la couleur 
    def get_couleur(self):
        return self.couleur
    
    def get_val(self):
        return self.val
        
    def __str__(self):
        if self.get_val()!=None:
            return self.get_couleur()+" "+str(self.get_val())
        else:
            return self.get_couleur()
