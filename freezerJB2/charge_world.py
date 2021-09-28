import pygame
import pyscroll
import pytmx



class Charge_world():

    def swap_world(self, nameCarte, zoom, player, positionEntry, positionExit, map):
        # charger la carte

        tmxData = pytmx.util_pygame.load_pygame(nameCarte)

        mapData = pyscroll.data.TiledMapData(tmxData)
        mapLayer = pyscroll.orthographic.BufferedRenderer(mapData, self.screen.get_size())
        mapLayer.zoom = zoom

        # definir une liste qui va stocker les rectangles de collisions
        self.walls = []

        for obj in tmxData.objects:
            if obj.type == 'collision':
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # definir le rectangle de collision pour entrer dans la maison
        enter_house = tmxData.get_object_by_name(positionEntry)
        self.enter_house_rect = pygame.Rect(enter_house.x, enter_house.y, enter_house.width, enter_house.height)

        # définir le point de spawn devant la maison
        spawn_point = tmxData.get_object_by_name(positionExit)
        self.player.position[0] = spawn_point.x
        self.player.position[1] = spawn_point.y - 20

        print('Position modifié')
        # bababsas

        # dessiner le groupe de calque
        self.group = pyscroll.PyscrollGroup(map_layer=mapLayer, default_layer=5)
        self.group.add(player)

        self.map = map

