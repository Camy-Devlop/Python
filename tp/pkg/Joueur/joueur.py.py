from personne import Personne

class Joueur(Personne):

    def __init__(self,nom,prenom="",date_nessance="",sexe=""):
        super().__init__(nom,prenom,date_nessance,sexe)