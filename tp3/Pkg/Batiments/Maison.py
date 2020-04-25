
from Pkg.Batiments.Batiment import Batiment
class Maison(Batiment):
      
      def __init__(self,nombre_etage=0):
          super().__init__(nombre_etage)
          print("Bienvenu a la maison")