from outils.vivant.Sexe import Sexe


class Personne(Sexe):
    def __init__(self, nom: str, prenom: str, date_naissance: str, sex: str):
        super().__init__(sex)
        self.__nom = nom
        self.__prenom = prenom
        self.date_naissance: str = date_naissance

    def __str__(self):
        return f"{self.__nom} {self.__prenom}"


