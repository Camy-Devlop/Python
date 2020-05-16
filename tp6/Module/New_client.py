
class New_Client():

    def __init__(self):
        self.nom:str=(input("Nom du client: ")).upper()
        self.prenom:str=(input("Prénom du client: ")).upper()
        print(self.nom,"\n"+self.prenom)


if __name__ == __name__:
    New_Client()