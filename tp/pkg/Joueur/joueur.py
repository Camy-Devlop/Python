#heritage de la classe personne 
from personne import Personne


#joueur 
class Joueur(Personne):

    #initisalisation de la class Joueur les attribue 
        #   nom obligatoire 
        #   attribue optionnelle prenom, date_nessance et sexe 
    def __init__(self,nom,prenom="",date_nessance="",sexe=""):
        super().__init__(nom,prenom,date_nessance,sexe)
