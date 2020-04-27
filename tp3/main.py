
#! /usr.bin/python3


from Pkg.Batiments.Immeuble import Immeuble
from Pkg.Batiments.Appartement import Appartement 

class main:
  
    print("bienvenu dans ma ville")
     
    app=list()
    a=list()
      
    for i in range(10):
        a.clear()
        for j in range(9):
            a.append(Appartement(i,str(chr(j+97))))
              
        app.append(a)
      
    print(app[1][2].get_