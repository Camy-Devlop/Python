from Module.Adresse import Adresse
from datetime import date

class Personne():

    def __init__(self,nom:str,prenom:str,adresse:Adresse,date_naissance:date,lieux_naissance:str):
        """
            va cree une base pour une personne avec son nom, nom prenom, son adresse, la date de naissance
            et le lieux de naissance
        :param nom: le nom de la personne string
        :param prenom: le prenom de la personne en string
        :param adresse:  class Adresse permet de stocker l'adresse de la personne
        :param date_naissance: type Date permet de stoker la date de naissance
        :param lieux_naissance: lieu de naissance type string
        """
        self.nom:str=nom
        self.prenom:str=prenom
        self.adresse:Adresse=adresse
        self.date_nee:date=date_naissance
        self.lieux_nee:str=lieux_naissance
        self.format_date:str="%d/%m/%Y"

    def __str__(self):
        """
            fonction general qui retourne un string
        :return: retourne le nom et le prenom de la personne
        """
        return self.nom+" "+self.prenom

    def get_adress(self)->str:
        """
        permet de retourner l'adresse de la personne
        :return: retourne l'adresse de la personne.
        """
        return self.adresse.__str__()


    def get_date_nee(self)->str:
        return self.date_nee.strftime(self.format_date)


    def get_lieux_nee(self)->str:
        return self.lieux_nee