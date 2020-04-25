from vie import Vie
class Personne(Vie):

    def __init__(self,nom,prenom="",date_nessance="",sexe=""):
        super(Personne,self).__init__(True)
        self.nom=nom
        self.prenom=prenom
        self.date=date
        self.sexe=sexe

    def get_nom(self):
        return self.nom

    