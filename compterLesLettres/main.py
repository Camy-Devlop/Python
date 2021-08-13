from lettre import Lettre
from compteur_lettre import Compteur_lettre
from compte_mot import Compte_mot
from mot import Mot
m="Bonjour tout le monde tout3 bonjour !"
text=Compte_mot(m)
text.affichage_des_mot()
mo=text.retourne_mot("tout")
mo.affiche()
#print(text.get_nombre_repet("tout"))

