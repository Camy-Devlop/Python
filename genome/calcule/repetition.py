
import itertools

class Repetition():

    def __init__(self,chaine:str=""):
        self.chaine=chaine
        self.combinaison=dict()
        self.groupe="ACGT"
        for i in range(len(self.groupe)):
            self.combinaison[self.groupe[i]]=list()
        print(self.combinaison)

    def combi(self):
        t=list()
        tt=""
        cpt=0
    
        for i in self.groupe:
            pass

a=Repetition()
a.combi()


a = ["A","C","G","T"]
#print (list(itertools.combinations(a,2)))
for i in range(len(a)):
   print(list(itertools.permutations(a,i)))
 