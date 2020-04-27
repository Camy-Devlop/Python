#! /usr.bin/python3


class Appartement():
       
      numero_de_letage=0
      numero_appart=""
       
      def __init__(self,numero_de_letage,numero_appart=""):
          self.numero_de_letage=numero_de_letage
          self.numero_appart=numero_appart
         
      
      def __str__(self):
          return str(self.numero_de_letage)+self.numero_appart

      def get_appart(self):
          return self.numero_appart

      def get_types(self):

          return ("Appartement")