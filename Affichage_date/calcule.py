from CONFIGS import *


def h(q: int, m: int, J: int, k: int):
    """
    h : methode qui va calcule le congruence de ZELLER
    elle va permettre de savoir quelle jour de la semaine avec une date donne en paramettre
    :param q : le jour
    :param m : le mois
    :param J : la moitier du coter gauche de l'anne             exemple 2021 le J = 20
    :param k : le moitier du coter droit de l'anne
               ex: 2021 k=21
    :return: retourne un int qui est le h congruence de ZELLER
    """
    return (q + (((m + 1) * 26) // 10) + k + (k // 4) + (J // 4) + 5 * J) % 7


def isLeap_year(year: int) -> bool:
    """
    : methode isLeap_year: methode qui determine
                 si l'anner donne en paramettre year est bissextile
    :param year : l'année qui va êter calculer
    :return: un boolean qui true si l'année est bissectile par True
    et si c'est pas une année bissextile par False
    """
    return year % 4 == 0  # retourne bool pour les anne bissextile


def day_in_month(month: int, year: int) -> int:
    # TODO A FAIRE
    return (
    {1: 31, 2: 29 if isLeap_year(year) == True else 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30,
     12: 31})[month]
    # retourne int le nombre de jour dans un mois


def day_of_week(day: int, month: int, year: int) -> int:
    """
    :Mehtode day_of_week : return le int entier qui le jour de la semaine
    0:Dim, 1:Lun ...
    :param day:
    :param month:
    :param year:
    :return : le jour de la semain en entier
    """
    return Mike_Keith(day, month, year)  # return int c'est les jour de la semain
    # 0:lun , 1:mar...


def Mike_Keith(day, month, year) -> int:
    """
     Mike Keith est un mathématicien américai
    """
    sigma = []

    if month < 3:
        sigma = [(23 * month) // 9, day, 4, year, (year - 1) // 4, -((year - 1) // 100), (year - 1) // 400]
        d = 0
        for i in sigma:
            d += i
        sigma = d % 7
        return sigma

    else:
        sigma = [(23 * month) // 9, day, 2, year, (year) // 4, -((year) // 100), (year) // 400]
        d = 0
        for i in sigma:
            d += i
        sigma = d % 7
        return sigma