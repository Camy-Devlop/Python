class Carte:
    def __init__(self, couleur,val=None):
        self.couleur=couleur
        self.val=val
        
    def get_couleur(self):
        return self.couleur
        
    def get_val(self):
        return self.val
        
    def __str__(self):
        if self.get_val()!=None:
            return self.get_couleur()+" "+str(self.get_val())
        else:
            return self.get_couleur()
