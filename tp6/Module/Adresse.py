class Adresse(object):

    def __init__(self,nom_adresse:str,numero:int,code_postal:int,commune:str,pays:str,boite:str=None):
        self.nom_adresse=nom_adresse
        self.numero=numero
        self.boite=boite
        self.code_postal=code_postal
        self.commune=commune
        self.pays=pays


    def __str__(self):
        return self.nom_adresse+" "+self.numero+" "+self.boite+" \n"+self.code_postal+" "+self.commune+" \n"+self.pays