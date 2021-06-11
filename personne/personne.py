#j'ai cree un fichier personne et on va cree une class personne avec un nom, prenom
#une date de nessance et les mettre en priver pour pas etre modifier et seulment consultable
# des getter et on va fais une mise en forme pour la date simple perso c'est partie


class Personne:
    __nom: str
    __prenom: str
    __jour: int
    __mois: int
    __annee: int

    def __init__(self,nom: str, prenom: str, jour: int, mois: int, anne: int):
        self.__nom=nom
        self.__prenom=prenom
        self.__jour=jour
        self.__mois=mois
        self.__annee=anne

    def num2chr(self,a: int)->str:
        if len(str(a))<2:
            return "0{0}".format(str(a))
        else:
            return str(a)
    @property
    def nom(self)->str:
        return self.__nom

    @property
    def prenom(self)->str:
        return self.__prenom

    @property
    def date_nessance(self)->str:
        return "{0}/{1}/{2}".format(self.num2chr(self.__jour), self.num2chr(self.__mois), self.__annee)

    # on va remoder la methode __str__ comme ca elle va afficher le nom et le prenom direcctement

    def __str__(self):
        return self.__nom+" "+self.__prenom