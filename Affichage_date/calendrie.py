from jour import Jour
from CONFIGS import *
from calcule import Mike_Keith
class Calandrie:
    def __init__(self,nb_jour:int=31,premier_semain:str="Dim"):
        self.premier_semain=premier_semain
        self.__nb_jour=nb_jour
        self.__jours:list=[]
        self.__liste()
    def __iter__(self):
        return iter(self.__jours)
    def __next__(self):
        return next(self.__jours)

    def __liste(self):

        cpt= jour_semaine2[self.premier_semain]
        print("test",cpt,jour_semaine3[cpt])
        for i in range(self.__nb_jour):
            self.__jours.append(Jour(i + 1, f"{jour_semaine3[cpt]}"))
            if cpt<8:
                cpt+=1
            else:cpt=1



    def EEE(self):
        for i in self.__jours:
            if i.value % 7 != 0:
                print(i, end="")
            else:
                print(i)
    def jour_semain_str(self,num):
        print(self.__jours[num],self.__jours[num].jour_semain)