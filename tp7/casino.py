import pygame 
from Module.emplacement import Emplacement
pygame.init()

import numpy as np

print("Bienvenue sur le la machine à sous")

fruits=["ananas","cerise","orange","pasteque","pomme_dore"]

fruit_hasard=[]
proba_fruit=[0.2,0.25,0.4,0.1,0.05]
jeton=0
fruit_dic={
    "orange":5,
    "cerise":15,
    "ananas":50,
    "pasteque":150,
    "pomme_dore":10000
}

hasard=np.random.choice(fruits, 3, replace=True, p=proba_fruit)
print(hasard[0])

if hasard[0] == hasard[1] == hasard[2]:
    jeton+=fruit_dic[hasard[0]]
    print(f"une ligne de {hasard[0]} a été completé ! +{fruit_dic[hasard[0]]} Jetons")

#les mesure de la fenetre 
largeur=800
hauteur=400
#l'image de la fenetre la machine
font_ecran=pygame.image.load("assets/images/slot.png")

#la declaration de la fenetre 
ecran = pygame.display.set_mode((largeur,hauteur))
pygame.display.set_caption("nouvelle fenetre ")

#couleur du font ecran
blanc=[255,255,255]
fruit_dic={
    "ananas":pygame.image.load("assets/images/ananas.png"),
    "cerise":pygame.image.load("assets/images/cerise.png"),
    "orange":pygame.image.load("assets/images/orange.png"),
    "pasteque":pygame.image.load("assets/images/pasteque.png"),
    "pomme_dore":pygame.image.load("assets/images/pomme_dore.png"),
    }
hauteur_emplacement=hauteur/2+57
emplacement_x_milieu=(largeur/2)-73
ecart_emplacement=100
emplacements=pygame.sprite.Group()
def lancement():
    emplacement_gauche=Emplacement(fruit_dic[hasard[0]],emplacement_x_milieu-ecart_emplacement,hauteur_emplacement)
    emplacement_milieu=Emplacement(fruit_dic[hasard[1]],emplacement_x_milieu,hauteur_emplacement)
    emplacement_droite=Emplacement(fruit_dic[hasard[2]],emplacement_x_milieu+ecart_emplacement,hauteur_emplacement)
    emplacements.add(emplacement_gauche)
    emplacements.add(emplacement_milieu)
    emplacements.add(emplacement_droite)

running=True
while running:
    ecran.fill(blanc)
    ecran.blit(font_ecran,(0,0))
    emplacements.draw(ecran)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
            quit()
        #cree un nouveau evenemt
        if event.type == pygame.KEYDOWN:
            # si la touche est la touche ESPACE
            if event.key == pygame.K_SPACE:
                lancement()
    
    
    print("rejouer !!!!!!")
    
    hasard=np.random.choice(fruits, 3, replace=True, p=proba_fruit)
    