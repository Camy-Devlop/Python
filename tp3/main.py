
#! /usr.bin/python3
from tkinter import *

from Pkg.Batiments.Immeuble import Immeuble
from Pkg.Batiments.Appartement import Appartement 

class main(object):
  
    print("bienvenu dans ma ville")
    window =Tk()
    
    app=list()
    a=list()
      
    for i in range(10):
        a.clear()
        for j in range(9):
            a.append(Appartement(i,str(chr(j+97))))
              
        app.append(a)
      
    