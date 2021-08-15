import pygame
import pytmx
import pyscroll
import os
import arcade


from player import Player


class Game():

    def __init__(self):
        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption("nouveau jeux")
        tmx_data = pytmx.util_pygame.load_pygame("carte1.tmx",pixelalpha=True)
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_data.visible_object_layers
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data,self.screen.get_size())
        map_layer.zoom=2
        self.fps=60

        self.player=Player(30,40,tmx_data)
        self.walls = []
        for obj in tmx_data.objects:
            print( obj.type)
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))


        self.groupe= pyscroll.PyscrollGroup(map_layer=map_layer,default_layer=4)
        self.groupe.add(self.player)
        #self.player = pygame.image.load("player.png")

    def update(self):
        self.groupe.update()
        for sprite in self.groupe.sprites():
            if sprite.feet.collidelist(self.walls)> -1:
                self.player.move_back()

    def run(self):
        running =True
        clock = pygame.time.Clock()
        while running:

            self.player.save_location()
            self.update()
            self.groupe.center(self.player.rect)
            self.groupe.draw(self.screen)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        self.clock.tick(self.fps)
        pygame.quit()
