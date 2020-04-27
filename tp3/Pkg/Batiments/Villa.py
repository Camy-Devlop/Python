

#! /usr.bin/python3

from Pkg.Batiments.Maison import Maison
class Villa(Maison):
  
       def __init__(self,nombre_etage=0):
            super().__init__(nombre_etage)
            print("Villa")