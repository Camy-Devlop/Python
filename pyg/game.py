import pygame
import pytmx
import pyscroll
import io

from p import P


class Game():

    def __init__(self):
        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption("nouveau jeux")
        tmx_data = pytmx.util_pygame.load_pygame("carte.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data,self.screen.get_size())
        map_layer.zoom=2

        self.player=P()


        self.groupe= pyscroll.PyscrollGroup(map_layer=map_layer,default_layer=3)
        self.groupe.add(self.player)
        #self.player = pygame.image.load("player.png")

    def run(self):
        running =True

        while running:

            self.groupe.update()
            self.groupe.center(self.player.rect)
            self.groupe.draw(self.screen)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()