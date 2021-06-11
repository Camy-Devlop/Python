from  personne import Personne
p=Personne("Adbaibi","Camy",2,1,1980)
print(p.nom)
print(p.prenom)
print(p.date_anniversaire)
p.__nom="bo"
print(p.nom)