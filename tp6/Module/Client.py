from Module.Compte import Compte
from Module.Adresse import Adresse
from Module.Personne import Personne


class Client(Personne):

    def __init__(self,compte:Compte,adres:Adresse):
        super().__init__("Adbaibi","prenom",adres)
        self.compte:Compte=compte


    def __str__(self):
        pass