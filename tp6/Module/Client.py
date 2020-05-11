from Module.Compte import Compte
from Module.Adresse import Adresse
from Module.Personne import Personne


class Client(Personne):

    def __init__(self,compte:Compte):
        super().__init__("Adbaibi","prenom",Adresse("rue du chien",10,1000,"Bruxelles","belgique"))
        self.compte:Compte=compte


    def __str__(self):
        pass