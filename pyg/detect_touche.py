import pygame


class Detect_touche:
    def __init__(self):
        pass

    def handl_imput(self,position:list):

        pressed= pygame.key.get_pressed()

        if pressed[pygame.K_UP]:
            position[1]-=1

        if pressed[pygame.K_DOWN]:
            position[1]+=1

        if pressed[pygame.K_LEFT]:
            position[0]-=1

        if pressed[pygame.K_RIGHT]:
            position[0]+=1
        return position