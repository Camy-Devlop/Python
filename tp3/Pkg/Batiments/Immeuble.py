#!/usr/bin/python3
from Pkg.Batiments.Batiment import Batiment
from Pkg.Batiments.Appartement import Appartement 
class Immeuble(Batiment):
      appart=list()
      
      def __init__(self,nombre_etage=0,appart=0):
          super().__init__(nombre_etage)
          
          
          for i in range(10):
              a.clear()
              for j in range(9):
                a.append(Appartement(i,str(chr(j+97))))



          #for x in appart:
           # for xx in x:
            #  self.appart=appart

      def nombre_etage_print(self):
        print("bienvenu dans l\'immeuble il y a {}".format(self.nombre_etage))      

      def nombre_etage_print(self):
        return self.nombre_etage      
          