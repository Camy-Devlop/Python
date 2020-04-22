
class Voyelle:
    # attribue voyalle c'est un string qui contient toute les voyelle
    # attribue liste_voyelle_trouver permet de stoker le voyelle trouver en tableau a deux dimention 
    voyelle="aeiouy"
    liste_voyelle_trouver=[]
    
    #initialisation du construteur et des attribue 
    def __init__(self):
        print("pres ok")
        self.mot=None
        self.liste_voyelle_trouver.clear()
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
       for l in range(len(self.voyelle)):
                if 0==self.liste_voyelle_trouver[self.voyelle.index(list(self.voyelle)[l])][1]:
                    print("voici la voyelle {} trouver {}".format(list(self.voyelle)[l],self.liste_voyelle_trouver[self.voyelle.index(list(self.voyelle)[l])][1]))
             

    # fonction qui va afficher tout les voyelle trouver
    def affiche_voyelle_trouver(self):
         
         for l in range(len(self.voyelle)):
                if 0<self.liste_voyelle_trouver[self.voyelle.index(list(self.voyelle)[l])][1]:
                    print("voici la voyelle {} trouver {}".format(list(self.voyelle)[l],self.liste_voyelle_trouver[self.voyelle.index(list(self.voyelle)[l])][1]))
             
    # fonction recherche voyelle et met a jour dans le tableau a deux dimantion
    def recher_voyelle(self,lettre):
        
        for xx in list(self.mot):
            if xx==lettre:
                self.liste_voyelle_trouver[self.voyelle.index(lettre)][1]+=1
                
    def total_voyelle(self):
        tmp=0
        for l in range(len(self.voyelle)):
            tmp +=self.liste_voyelle_trouver[self.voyelle.index(list(self.voyelle)[l])][1]
        return tmp
#v.get_numbers_voyelle("patrik")sh

ll=Voyelle()
ll.get_numbers_voyelle("patriko vi t y e mddd")
print(ll.liste_voyelle_trouver) 
ll.affiche_voyelle_trouver()
print("========================================================")
ll.affiche_voyelle_yapas()
print("========================================================")
print("voici le nombre total de voyelle {}".format(ll.total_voyelle()))