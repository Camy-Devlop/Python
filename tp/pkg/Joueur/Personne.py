from vie import Vie
class Personne:

    def __init__(self,nom,prenom="",date_nessance="",sexe=None):
        super().__init__(True)
        self.nom=nom
        self.prenom=prenom
        self.date=date
        self.sexe=sexe

    def get_nom(self):
        return self.nom

    