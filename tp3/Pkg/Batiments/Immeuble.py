#!/usr/bin/python3
from Pkg.Batiments.Batiment import Batiment

class Immeuble(Batiment):
      appart=list()
      
      def __init__(self,nombre_etage=0,appart=[]):
          super().__init__(nombre_etage)
          self.nombre_etage=nombre_etage
          
          for x in appart:
            for xx in x:
              self.appart=appart

            print("bienvenu dans l\'immeuble il y a {}".format(self.nombre_etage))
          