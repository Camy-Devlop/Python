from random import shuffle

class ListMots:

    list_mot=[]
    def __init__(self):
        self.list_mot
        self.list_mot.clear()
        

    def demande_liste_mot(self):  
        self.list_mot= input("viellez entre des mot et chause mot separer par un / ").split("/")
        print(self.list_mot)
    
    def melanger_mot_List(self):
        print("liste dans la classe "+str(self.list_mot))
        shuffle(self.list_mot)
        return  self.list_mot



       
    
    