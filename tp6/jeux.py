import pygame
pygame.init()

#enerer la fenetre de notre jeu
pygame.display.set_caption("comet fall game")
screen=pygame.display.set_mode(((1080,720)))
bg=pygame.image.load('assets/bg.jpg')
running = True


while running:

    screen.blit(bg,(0,0))
    pygame.display.flip()
    for event in pygame.event.get():

        if event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                print("c'est moi achraf")