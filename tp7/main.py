import random
import numpy as np

print("Bienvenue sur le la machine à sous")

fruits=["ananas","cerise","orange","paseteque","pomme_dore"]
print(fruits)
fruit_hasard=random.choices(fruits,k=3)
proba_fruit=[0.2,0.25,0.4,0.1,0.05]
jeton=0
fruit_dic={
    "orange":5,
    "cerise":15,
    "ananas":50,
    "pasteque":150,
    "pomme_dore":10000
}
print("{} - {} - {}".format(fruit_hasard[0],fruit_hasard[1],fruit_hasard[2]))

hasard=np.random.choice(fruits, 3, replace=True, p=proba_fruit)
print("affiche {}".format(hasard))

if hasard[0] == hasard[1] == hasard[2]:
    jeton+=fruit_dic[hasard[0]]
    print(f"une ligne de {hasard[0]} a été completé ! +{fruit_dic[hasard[0]]} Jetons")