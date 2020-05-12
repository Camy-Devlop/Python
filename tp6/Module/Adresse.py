class Adresse(object):

    def __init__(self,nom_adresse:str,numero:int,code_postal:int,commune:str,pays:str,boite:str=None):
        """   :param nom_adresse: le nom de l'adressse
            :param numero: le numero de la porte ou du batiment
            :param code_postal: un entier pour le code postal de la ville
            :param commune: string nom de la commune de la ville
            :param pays: string le nom du payer ou la personne reside
            :param boite: string le numero de boite s'il y a une optionel
        """


        self.nom_adresse:str=nom_adresse
        self.numero:int=numero
        self.boite:str=boite
        self.code_postal:int=code_postal
        self.commune:str=commune
        self.pays:str=pays


    def __str__(self)->str:
        """
            :return: une chaine de caractaire avec l'adresse complete
        """
        if self.boite !=None:
            return "{} {}/{}\n{} {}".format(self.nom_adresse,self.numero,self.boite,self.code_postal,self.pays)
        else:
            return "{} {}\n{} {}".format(self.nom_adresse,self.numero,self.code_postal,self.pays)