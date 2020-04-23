from random import shuffle
#la classe test cree une liste mot quelle va demander a l'utilisateur d'introduire
# en separant les mot avec un '/' 
#  
class ListMots():

    #création de l'attribue 
    list_mot=[]

    #inisialisation des variable 
    def __init__(self):
        self.list_mot
        self.list_mot.clear()
        
    #fonction pour demander a l'utilisateur de d'introduire les mot pour remplire la liste et
    # et le separateur est un '/'
    def demande_liste_mot(self):  
        self.list_mot= input("viellez entre des mot et chause mot separer par un / ").split("/")
        print(self.list_mot)
    
    #fonction pour melanger le tabeau de mot et le retourne le tableau melanger 
    def melanger_mot_List(self):

        shuffle(self.list_mot)
        return  self.list_mot



       
    
    
