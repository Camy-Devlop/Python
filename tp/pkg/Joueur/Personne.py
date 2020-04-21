class Personne:

    def __init__(self,nom,prenom="",date_nessance="",sexe=None):
        self.nom=nom
        self.prenom=prenom
        self.date=date
        self.sexe=sexe

    def get_nom(self):
        return self.nom