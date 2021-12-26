# un import de date qui nous permetera de fait un petit tuto sur les date
#on va aussi determiner le nombre de jour qui reste avant l'anniversaire
#et nous allons determiner l'age de la personne
from datetime import datetime

class My_Date():
    __date_naissance:datetime# la variable qui va permettre de stoker la date de naissance

    def __init__(self,jour:int,mois:int,annee:int):#voici le constructeur qui resoit 3 parametre
        self.__date_naissance=datetime(day=jour,month=mois,year=annee) # stocke la date dans la variable

        # une verification que la diference pour etre sur que le nombre de jour soit positife


    def num2chr(self,a: int)->str:
        if len(str(a))<2:
            return "0{0}".format(str(a))
        else:
            return str(a)

    @property
    def date_naissance(self) -> str:
        return "{0}/{1}/{2}".format(self.num2chr(self.__date_naissance.day),
                                    self.num2chr(self.__date_naissance.month), self.__date_naissance.year)

    #passons a la presantion puis que c'est des variable prive
    #on va utiliser property qui va nous permettre d'avoir des getter
    @property
    def age(self)->str:

        if (datetime.now()-self.__date_naissance).days>0:
            return ((datetime.now()-self.__date_naissance)//365).days
        else:
            return 0 #si 'est egale a 0 il est pas née mdr


    @property
    def combien_Jour_reste(self)->int:
        """
             jour_reste_aniversaire: methode getter qui va calculer le nombre de jour qui rest de la date anniversaire
         """
        if datetime.now().month > self.__date_naissance.month:

            return (datetime(datetime.now().year+1,
                             self.__date_naissance.month,
                             self.__date_naissance.day)-datetime.now()).days+1
        else:
            return (datetime(datetime.now().year,
                             self.__date_naissance.month,
                                    self.__date_naissance.day) - datetime.now()).days +1