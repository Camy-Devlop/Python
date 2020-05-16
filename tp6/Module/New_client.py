from Module.Adresse import Adresse
from Module.Personne import Personne


class New_Client():

    def __init__(self):
        self.nom:str=(input("Nom du client: ")).upper()
        self.prenom:str=(input("Prénom du client: ")).upper()
        self.adr:Adresse=Adresse(input("Adresse: "),int(input("Numero: ")),int(input("Code postal: ")),input("commune: "),input("Pays: "))

    def get_personne(self)->Personne:
        if self.nom!=None and self.prenom!=None:
            return Personne(self.nom,self.prenom,self.adr.__str__())

if __name__ == __name__:
   print( New_Client().get_personne())