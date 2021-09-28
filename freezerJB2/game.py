import pygame
import pytmx
import pyscroll

import charge_world
from player import Player
from charge_world import Charge_world as swap

class Game:

    def __init__(self):

        self.map ='house'
        self.charge_world=swap
        # creation de la fenêtre
        #self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption("Pygamon - Aventure")

        # charger la carte

        tmxData = pytmx.util_pygame.load_pygame('carte.tmx')
        mapData = pyscroll.data.TiledMapData(tmxData)
        mapLayer = pyscroll.orthographic.BufferedRenderer(mapData, self.screen.get_size())
        mapLayer.zoom = 3.5

        # generer un joueur
        playerPosition = tmxData.get_object_by_name('player')
        self.player = Player(playerPosition.x, playerPosition.y)

        # definir une liste qui va stocker les rectangles de collisions
        self.walls = []

        for obj in tmxData.objects:
            if obj.type == 'collision':
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # dessiner le groupe de calque
        self.group = pyscroll.PyscrollGroup(map_layer=mapLayer, default_layer=5)
        self.group.add(self.player)

        # definir le rectangle de collision pour entrer dans la maison
        enter_house = tmxData.get_object_by_name('enter_house_blue')
        self.enter_house_rect = pygame.Rect(enter_house.x, enter_house.y, enter_house.width, enter_house.height)

        enter_world = tmxData.get_object_by_name('switch_world_ouest_top')
        self.enter_world_rect = pygame.Rect(enter_world.x, enter_world.y, enter_world.width, enter_world.height)


    def handleInput(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_z]:
            self.player.move_up()
            self.player.change_animation('up')
        elif pressed[pygame.K_s]:
            self.player.move_down()
            self.player.change_animation('down')
        elif pressed[pygame.K_d]:
            self.player.move_right()
            self.player.change_animation('right')
        elif pressed[pygame.K_q]:
            self.player.move_left()
            self.player.change_animation('left')



    def update(self):
        self.group.update()

        # verifier l'entrer dans la maison
        if self.map =='house' and self.player.feet.colliderect(self.enter_house_rect):
            self.charge_world.swap_world(self,'house_blue.tmx', 4,self.player,'exit_house','spawn_house', 'world')

        # verifier la sortie dans la maison
        if self.map == 'world' and  self.player.feet.colliderect(self.enter_house_rect):
            
            self.charge_world.swap_world(self,'carte.tmx', 3.5,self.player, 'enter_house_blue', 'enter_house_exit', 'house')

        if self.map == "carte_Ouest" and self.player.feet.colliderect(self.enter_house_rect):
            self.charge_world('carte_Ouest.tmx', 3.5,self.player, 'switch_world_middle_top', 'spawn_world_ouest_top', 'world')
            print('Changez monde')


        # verification de la collision
        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.walls) > -1:
                sprite.move_back()

    def run(self):

        clock = pygame.time.Clock()

        # boucle du jeu
        running = True

        while running:

            self.player.save_location()
            self.handleInput()
            self.update()
            self.group.center(self.player.rect)
            self.group.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(60)

        pygame.quit()