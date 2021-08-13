from lettre import Lettre

class Compteur_lettre:


    def __calculer(self):
        for i in self.__text:
            if len(self.__liste_lettres) < 1:
                self.__liste_lettres[str(i).lower()] = Lettre(i)
            elif i not in self.__liste_lettres.keys():
                self.__liste_lettres[str(i).lower()] = Lettre(i)
            else:
                self.__liste_lettres[str(i).lower()].set_test(i)

    def __init__(self, text: str):
        self.__liste_lettres = dict()
        self.__text = text
        self.__calculer()

    def affiche(self):
        for i, j in self.__liste_lettres.items():
            print("{0} {1}".format(i, j.get_cpt))

    def get_repeter_lettre_string(self, l: chr) -> int:
        if str(l).lower() in self.__liste_lettres.keys():
            return self.__liste_lettres[str(l).lower()].get_cpt
        else:
            return 0
