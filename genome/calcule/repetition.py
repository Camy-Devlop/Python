
import itertools

class Repetition():

    def __init__(self,chaine:str=""):
        self.chaine=chaine
        self.combinaison:dict=[]
        self.groupe="ACGT"
        
    def couper(self):
        a=[]
        tmp=""
        for i in range(1,len(self.chaine)):
            for ii in range(0,i):
                tmp+=self.chaine[ii]
                
            a.append(tmp)
            tmp=""
        self.combinaison=a
    
    def affichage(self):
        for i in self.combinaison:
            print(i)

    def affichage_N(self,N):
        for i in range(N):
            print(self.combinaison[i])

    def nombre_repeter(self,n):
        for i in range(0,n):
            print(i,self.combinaison[i], self.chaine.count(self.combinaison[i]))
















"""a = ["A","C","G","T","A"]
b=list()
#print (list(itertools.combinations(a,2)))
for i in range(len(a)):
   b=a[i]
   for ii in range(len(a)):
       print(b+a[ii])
"""





