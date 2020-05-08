
#class va permetre appliquer des regle de jeux 
from random import randint
from Module.carte import Carte
from Module.carte_special import Carte_special
class Regle:
    
    def verifie_deposer(self,carte_sur_table:Carte, carte_deposer:Carte or Carte_Special) -> bool:
        self.carte_sur_table=carte_sur_table
        self.carte_deposer=carte_deposer
        methode_nom="method_"+carte_deposer.get_couleur()
        method = getattr(self, methode_nom, lambda: "carte non autoriser")
        # Call the method as we return it
        return method()

    def method_4c(self):
        
        print("carte 4c "+str(isinstance(self.carte_deposer,Carte_special)))
        self.carte_deposer.get_carte()
       
        return True
    
    def method_4c4x(self):
        return True
    
    def method_4c2x(self):
        return True
    
    def method_bloc(self):
        return True
    
    def method_sens(self):
        return True
    
    def method_meme_carte(self):
        return True
    
    def method_jaune(self):
        return True
    
    def method_vert(self):
        return True

    def method_bleu(self):
        return True
    
    def method_rouge(self):
        return True
    
    def method_val(self,cartetable:Carte,cartedeposer:Carte):
        if self.cartetable.get_val==cartedeposer.get_val:
            return True
        else:
            return False
        
       
 

    # if carte_sur_table.get_couleur()==carte_deposer.get_couleur() or carte_sur_table.get_val()==carte_deposer.get_val():
    #             return True
    #             #{"4c":4,"4c4x":1,"4c2x":4}
    #         elif carte_deposer.get_couleur()=="4c" or carte_deposer.get_couleur()=="4c4x" or carte_deposer.get_couleur()=="4c2x" :
                
    #             return True
            
    #         elif 
    #         else:
    #             return False