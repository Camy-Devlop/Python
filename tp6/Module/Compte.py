from Module import Numero_compte
from Module.String_int import String_int


class Compte():

    def __init__(self,parti1:String_int,parti2:int,parti3:int,parti4:int):
        liste=[str(parti2),str(parti3),str(parti4)]
        cpt:int=0
        for t in range(0,len(liste)-1):
            cpt=len(liste[t])
            if cpt > 4:
                print(len(liste[0]))
                print("longueur du str {} et la valeur entre {}".format(len(liste[t]),liste[t]))
                liste[t]=input("la valeur entre pour crée un compte a plus de 4 chiffre \nveiller enrte 4 chiffres MAX :")
            
        self.compte:Numero_compte=[parti1,liste[0].zfill(4),liste[1].zfill(4),liste[2].zfill(4)]

    def __str__(self):
        return ''.join(str(e) for e in self.compte)