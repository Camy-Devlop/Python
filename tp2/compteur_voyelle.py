
class Voyelle:
    # attribue voyalle c'est un string qui contient toute les 
    # voyelle 
    voyelle="aeiouy"
    liste_voyelle_trouver=[]
    def __init__(self):
        print("pres ok")
        self.mot=None
        self.liste_voyelle_trouver=[]
        for i in range(0,len(self.voyelle)):
           self.liste_voyelle_trouver.append([(list(self.voyelle))[i],0]) 

    #def __str__(self):
     #   return self.voyelle

    def get_numbers_voyelle(self,mot):
        self.mot=mot
        for x in list(self.voyelle):
            self.recher_voyelle(x)

    def affiche_voyelle_yapas(self):
        pass

    def affiche_voyelle_trouver(self):
        for l in self.voyelle:
            if l>0:
                print("Voici les voyelle trouvée ",l)

    def recher_voyelle(self,lettre):
        cpt=0
        for xx in list(self.mot):
            if xx==lettre:
                self.liste_voyelle_trouver[self.voyelle.index(lettre)][1]+=1
                pass
            cpt+=1

    def get_t(self):
        return self.liste_voyelle_trouver
#v=Voyelle()

#v.get_numbers_voyelle("patrik")sh

ll=Voyelle()
ll.get_numbers_voyelle("patrikmddd")
print() 
 