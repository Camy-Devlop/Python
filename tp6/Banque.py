

from Module.Adresse import Adresse
from Module.Client import Client
from Module.Compte import Compte
from Module.String_int import String_int
from datetime import date
#adr=Adresse("avenue de l'expo. univer.",50,1083,"chichi","bruxelles")
#comp=Compte(String_int("BE",3),2934,9991,2100)

#===================================================================================

#===================================================================================
print("============== Client ==============")

#client=Client("Adbaibi","Ismail",comp,adr)

#print(client)
#print(client.get_adress())

print("============== Date ==============")
d=date(2020,1,3)

print(d.strftime("%d/%m/%Y"))