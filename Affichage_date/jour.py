
class Jour:
    def __init__(self, nb, jour_semaine, espace:str=" ", nb_espace=3):
        self.__nb = nb
        self.espace=espace*nb_espace
        self.__jour_semaine=jour_semaine

    def __str__(self):
        return self.__affichage()

    def __affichage(self)->str:
        if self.__nb<10:return f"0{self.__nb}{self.espace}"
        else: return f"{self.__nb}{self.espace}"

    @property
    def jour_semain(self):
        return self.__jour_semaine

    @property
    def value_int(self):
        return self.__nb