from Module.Adresse import Adresse


class Personne():
    def __init__(self,nom:str,prenom:str,adresse:Adresse):
        self.nom:str=nom
        self.prenom:str=prenom
        self.adresse:Adresse=adresse

    def __str__(self):
        return self.nom+" "+self.prenom

    def get_adress(self)->str:
        return self.adresse.__str__()