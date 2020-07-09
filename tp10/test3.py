from datetime import date

def naissance(fonc,anne=0,mois=0,jour=0):
      if anne!=0 and mois!=0 and jour!=0:
         d=date(2000,3,23)
         fonc.self.d=d
      return fonc

@naissance
class Humain:
   def __init__(self):
      self.__nom:str=input("entre un nom ")

   @property
   def humain(self)->str:
      return self.__nom

   @humain.setter
   def humain(self,name:str):
      self.__nom=name

   @property
   def affiche_name(self):
      print(self.__nom)

  # nom=property(get_name,set_name)


m=Humain()


print(m.humain)
print(m.d.__str__())