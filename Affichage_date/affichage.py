from CONFIGS import *
from calcule import *


class Affichage:

    def __init__(self):
        self.jour = 0

    def affichage(self, mois=4, anne=2021):
        nb_jour = day_in_month(mois, anne)

        h_j_semaine = Mike_Keith(1, mois, (int(anne)))
        self.jour = jour_semaine2[Mike_Keith_semaine[
            h_j_semaine]]  # determine le nombre de jour pour le decalage pour commencera affichier le jour 01
        print(ligne_separation)  # une ligne de separation
        print("{0} {1}".format(mois_anne[mois], anne))  # affiche le le mois et l'année
        print(ligne_separation)  # une ligne de separation
        print(d := "  ".join(__ for _, __ in jour_semaine.items()))
        for i in self.__tab_nb_1_to_mois_str(nb_jour):
            print(i)
        print(ligne_separation)

    def __tab_nb_1_to_mois_str(self, nb):
        tab = []
        tab2 = []
        for i in range(1, self.jour):
            tab.append(" " * 5)

        for i in range(1, nb + 1):
            tab.append(get_day_str(i) + "   ")

        for i in range(0, nb + self.jour, 7):
            tab2.append("".join(tab[i:i + 7]))
        return tab2


def print_calendar(month: int, year: int):
    self.affichage()


def print_day(day: int):
    if day < 10:
        print(f"0{day}")
    else:
        print(day)


def get_day_str(day: int):
    if day < 10:
        return f"0{day}"
    else:
        return str(day)