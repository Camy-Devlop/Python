def switch_world_ouest_top(self):
    # charger la carte
    tmxData = pytmx.util_pygame.load_pygame('carte_Ouest.tmx')
    mapData = pyscroll.data.TiledMapData(tmxData)
    mapLayer = pyscroll.orthographic.BufferedRenderer(mapData, self.screen.get_size())
    mapLayer.zoom = 4

    # definir une liste qui va stocker les rectangles de collisions
    self.walls = []

    for obj in tmxData.objects:
        if obj.type == 'collision':
            self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

    # definir le rectangle de collision pour entrer dans la maison
    enter_world = tmxData.get_object_by_name('switch_world_middle_top')
    self.enter_world_rect = pygame.Rect(enter_world.x, enter_world.y, enter_world.width, enter_world.height)

    # définir le point de spawn devant la maison
    spawn_world_point = tmxData.get_object_by_name('spawn_world_ouest_top')
    self.player.position[0] = spawn_world_point.x
    self.player.position[1] = spawn_world_point.y

    # dessiner le groupe de calque
    self.group = pyscroll.PyscrollGroup(map_layer=mapLayer, default_layer=5)
    self.group.add(self.player)


def switch_world_middle_ouest_top(self):
    # charger la carte
    tmxData = pytmx.util_pygame.load_pygame('carte.tmx')
    mapData = pyscroll.data.TiledMapData(tmxData)
    mapLayer = pyscroll.orthographic.BufferedRenderer(mapData, self.screen.get_size())
    mapLayer.zoom = 4

    # definir une liste qui va stocker les rectangles de collisions
    self.walls = []

    for obj in tmxData.objects:
        if obj.type == 'collision':
            self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

    # definir le rectangle de collision pour entrer dans la maison
    enter_world = tmxData.get_object_by_name('switch_world_ouest_top')
    self.enter_world_rect = pygame.Rect(enter_world.x, enter_world.y, enter_world.width, enter_world.height)

    # définir le point de spawn devant la maison
    spawn_world_point = tmxData.get_object_by_name('spawn_world_middle_ouest_top')
    self.player.position[0] = spawn_world_point.x
    self.player.position[1] = spawn_world_point.y + 20

    # dessiner le groupe de calque
    self.group = pyscroll.PyscrollGroup(map_layer=mapLayer, default_layer=5)
    self.group.add(self.player)

    def switch_world(self):

        # charger la carte
        tmxData = pytmx.util_pygame.load_pygame('carte.tmx')
        mapData = pyscroll.data.TiledMapData(tmxData)
        mapLayer = pyscroll.orthographic.BufferedRenderer(mapData, self.screen.get_size())
        mapLayer.zoom = 4

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

        # définir le point de spawn devant la maison
        spawn_house_point = tmxData.get_object_by_name('enter_house_exit')
        self.player.position[0] = spawn_house_point.x
        self.player.position[1] = spawn_house_point.y + 20

        self.map = 'house'