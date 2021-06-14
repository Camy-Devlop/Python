from datetime import datetime


class My_date():
    __date_anniversaire: datetime
    __jours_avant_annivversaire: int

    def __init__(self, jour: int, mois: int, annee: int):
        if (jour > 0) and (mois > 0) and (annee > 0):
            self.__date_anniversaire = datetime(annee, mois, jour)

    @property
    def age(self):
        j_date = (datetime.now()-self.__date_anniversaire ).days//365
        return j_date

    @property
    def jour_reste_aniversaire(self):
        if datetime.now()>datetime(datetime.now().year,self.__date_anniversaire.month,self.__date_anniversaire.day):
            return (datetime(datetime.now().year+1,self.__date_anniversaire.month,self.__date_anniversaire.day)-datetime.now()).days+1
        else:
            return (datetime(datetime.now().year , self.__date_anniversaire.month,
                             self.__date_anniversaire.day) - datetime.now()).days+1
