from compteur_lettre import Compteur_lettre


class Mot(Compteur_lettre):
    __mot: str
    __cpt: int

    def __init__(self, mot: str):
        super().__init__(mot)
        self.__mot = mot
        self.__cpt = 1

    @property
    def mot(self):
        return self.__mot

    @mot.setter
    def mot(self, m: str):
        if self.__mot.lower() == m.lower():
            self.__cpt += 1

    @property
    def nombre(self):
        return self.__cpt

    def __str__(self):
        return self.__mot
