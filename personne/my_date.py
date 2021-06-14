from datetime import datetime
"""
    TytoPy voici un petit tuto qui permet d'avoir une date de naissence qui peremt de connaire l'age de la personne 
    et de connaire combien il reste de jour pour jour d'annivaire 
"""

class My_date():
    """
    __date_anniversaire: datetime variable qui va stoker la date de naissence 
        
    """
    __date_anniversaire: datetime
    
    
    #TODO verifier un date qui n'est pas encore arriver 
    def __init__(self, jour: int, mois: int, annee: int):
        if (jour > 0) and (mois > 0) and (annee > 0):
            self.__date_anniversaire = datetime(annee, mois, jour)

    @property
    def age(self):
        """
            age: mehtode getter qui va calcule l'age de la personne avec la date aujourd'hui et la date naissence 
        """
        j_date = (datetime.now()-self.__date_anniversaire ).days//365
        return j_date

    @property
    def jour_reste_aniversaire(self):
        """
            jour_reste_aniversaire: methode getter qui va calculer le nombre de jour qui rest de la date anniversaire 
        """
        
        if datetime.now()>datetime(datetime.now().year,self.__date_anniversaire.month,self.__date_anniversaire.day):
            return (datetime(datetime.now().year+1,self.__date_anniversaire.month,self.__date_anniversaire.day)-datetime.now()).days+1
        else:
            return (datetime(datetime.now().year , self.__date_anniversaire.month,
                             self.__date_anniversaire.day) - datetime.now()).days+1
