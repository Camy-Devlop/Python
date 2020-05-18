import pygame 
pygame.init()


ecran = pygame.display.set_mode((800,400))
pygame.display.set_caption("nouvelle fenetre ")

running=True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False