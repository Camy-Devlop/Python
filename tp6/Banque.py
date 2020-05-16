

from Module.Adresse import Adresse
from Module.Client import Client
from Module.Compte import Compte
from Module.String_int import String_int
from Module.Verifier import verifie_ischiffre as verif

adr=Adresse("avenue de l'expo. univer.",50,1083,"chichi","bruxelles")
comp=Compte(String_int("BE",3),2934,9991,2100)

#===================================================================================
print(adr,"\n",comp)

#===================================================================================
print("============== Client ==============")

client=Client("Adbaibi","Ismail",comp,adr)

print(client)
print(client.get_adress())