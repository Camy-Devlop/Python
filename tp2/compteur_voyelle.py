
class Voyelle:
    # attribue voyalle c'est un string qui contient toute les voyelle
    # attribue liste_voyelle_trouver permet de stoker le voyelle trouver en tableau a deux dimention 
    voyelle="aeiouy"
    liste_voyelle_trouver=[]
    
    #initialisation du construteur et des attribue 
    def __init__(self):
        print("pres ok")
        self.mot=None
        self.liste_voyelle_trouver=[]
        # place les voyelle dans le tableau da deux diemention avec le nombre a 0 voyelle 
        #
        #       liste_voyelle_trouver[0]-> ["a",0]
        #       liste_voyelle_trouver[1]-> ["e",0]
        #       liste_voyelle_trouver[2]-> ["i",0]
        #       liste_voyelle_trouver[3]-> ["o",0]
        #       etc
        #
        for i in range(0,len(self.voyelle)):
           self.liste_voyelle_trouver.append([(list(self.voyelle))[i],0]) 

       # fonction get_number_voyelle va recherche le nombre de voyelle 
       # elle resoit en parametre mot c'est dans cette vaiable quelle va faire les recherche de voyele 
    def get_numbers_voyelle(self,mot):
        self.mot=mot
        for x in list(self.voyelle):
            self.recher_voyelle(x)

    # fonction qui va cherche quelle sont les voyelle qu'y a pas dans le mot demander 
    def affiche_voyelle_yapas(self):
        pass

    # fonction qui va afficher tout les voyelle trouver
    def affiche_voyelle_trouver(self):
        for l in self.voyelle:
            if l>0:
                print("Voici les voyelle trouvée ",l)

    # fonction recherche voyelle 
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
 