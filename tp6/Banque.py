

import Module.Adresse
from Module.Compte import Compte
from Module.String_int import String_int
from Module.Verifier import verifie_ischiffre as verif

a=Module.Adresse.Adresse("avenue de l'expo. univer.",50,1083,"chichi","bruxelles")
#print(a)

#===================================================================================
print(a)

#===================================================================================

comp=Compte(String_int("BE",3),2934,9991,21E00)

print(comp)
print("=================================")

