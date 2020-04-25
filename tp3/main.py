
from Pkg.Batiments.Immeuble import Immeuble
from Pkg.Batiments.Appartement import Appartement 

class main:
  
      print("bienvenu dans ma ville")
     
      app=list()
      a=list()
      b=list()
     # for i in range(10):
      #    for j in range(9):
       #       a.append(Appartement(i,str(chr(j+97))))
        
       # app.append(a)
      
      a.append([2,3,4,5,6])

      #b.append(["a","b","c","d"])
      b.append("a")
      b.append("b")
      b.append("c")
      b.append("d")

      app.append(a[0])
      app.append(b)  
      print(app)