#aN-1=y
from random import randint as rnd


y = rnd(1,40)
a = rnd(1,40)
N=0
trouver=False
valeur=""

def N_positif(N)->int:
    print("positif")
    N+=1
    return N

def N_negatif(N)->int:
    print("positif")
    N-=1
    return N


if a<=y:
    valeur=N_positif
else:
    valeur=N_negatif

print("Dabut")

while trouver==False:
    print("{}x{}-1={}".format(a,N,y))

    if a*N-1==y:
        trouver=True
    else:
        N=valeur(N)

print("on a trouver N = {}".format(N))