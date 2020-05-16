from Module.Adresse import Adresse
from datetime import date

class Personne():
    def __init__(self,nom:str,prenom:str,adresse:Adresse,date_naissance:date,lieux_naissance:str):
        self.nom:str=nom
        self.prenom:str=prenom
        self.adresse:Adresse=adresse


    def __str__(self):
        return self.nom+" "+self.prenom

    def get_adress(self)->str:
        return self.adresse.__str__()