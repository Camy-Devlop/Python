from my_date import My_date


class Personne:
    __nom: str
    __prenom: str
    __date: My_date

    def __init__(self, nom: str, prenom: str, jour: int, mois: int, anne: int):
        self.__nom = nom
        self.__prenom = prenom
        self.__date = My_date(jour, mois, anne)

    @property
    def nom(self):
        return self.__nom

    @property
    def prenom(self):
        return self.__prenom

    @property
    def date_anniversaire(self):
        return self.__date.date
