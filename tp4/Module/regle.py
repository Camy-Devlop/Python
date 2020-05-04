
#class va permetre appliquer des regle de jeux 
from random import randint
from Module.carte import Carte
class Regle:
    
    def verifie_deposer(self,carte_sur_table:Carte, carte_deposer:Carte) -> bool:

            if carte_sur_table.get_couleur()==carte_deposer.get_couleur() or carte_sur_table.get_val()==carte_deposer.get_val():
                return True
                #{"4c":4,"4c4x":1,"4c2x":4}
            elif carte_deposer.get_couleur()=="4c" or carte_deposer.get_couleur()=="4c4x" or carte_deposer.get_couleur()=="4c2x" :
                return True
            else:
                return False

   