from Module.Compte import Compte
from Module.Adresse import Adresse
from Module.Personne import Personne


class Client(Personne):

    def __init__(self,nom:str,prenom:str,compte:Compte,adres:Adresse):
        super().__init__(nom,prenom,adres)
        self.compte:Compte=compte


    def __str__(self):
        return "Nom:"+self.nom+" Prenom:"+self.prenom+"\n"+"Numero de compte: "+self.compte.__str__()