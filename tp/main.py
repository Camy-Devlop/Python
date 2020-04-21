
#importation de la classe ListMots 

#from pkg.tplist import ListMots 
from pkg.Joueur.joueur import Joueur
from pkg.Joueur.personne import Personne
from pkg.Joueur.vie import Vie
class main:

    #l=ListMots()
    #l.demande_liste_mot()
    #print("le tableau "+str(l.melanger_mot_List()))          

    j=Joueur("Pat")

    print("nom du joueur ",j.get_nom())