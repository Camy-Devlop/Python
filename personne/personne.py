#j'ai cree un fichier personne et on va cree une class personne avec un nom, prenom
#une date de nessance et les mettre en priver pour pas etre modifier et seulment consultable
# des getter et on va fais une mise en forme pour la date simple perso c'est partie

from my_date import My_Date
class Personne(My_Date):
    __nom: str
    __prenom: str

    # TODO: faire une verification de la date naissance inverieur a aujourd'hui
    def __init__(self,nom: str, prenom: str, jour: int, mois: int, anne: int):
        super().__init__(jour, mois, anne)
        self.__nom = nom
        self.__prenom = prenom

    @property
    def nom(self)-> str:
        return self.__nom

    @property
    def prenom(self)-> str:
        return self.__prenom


    # on va remoder la methode __str__ comme ca elle va afficher le nom et le prenom direcctement

    def __str__(self):
        return self.__nom + " " + self.__prenom