import pygame

from detect_touche import Detect_touche


class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,tmx_data):
        super().__init__()
        self.tmx_data=tmx_data
        self.sprite_sheet = pygame.image.load('player.png')
        self.image=self.get_image(0,0)
        #self.image.set_colorkey([0,0,0])
        self.rect = self.image.get_rect()
        self.feet=pygame.Rect(0,0,self.rect.width*0.5,12)

        self.images = {
            'down': self.get_image(0, 0),
            'left': self.get_image(0, 32),
            'right': self.get_image(0, 64),
            'up': self.get_image(0, 96)
        }

        self.speed = 1


        self.position=[x,y]
        self.old_position = self.position.copy()
        self.touche = Detect_touche()
    def save_location(self): self.old_position = self.position.copy()

    def update(self):

        position,image=self.touche.handl_imput(self.position)
        self.change_animation(image)
        self.rect.topleft = position
        self.feet.midbottom=self.rect.midbottom

    def move_back(self):
        self.position = self.old_position
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom



    def get_image(self,x,y):
        image=pygame.Surface([32,32])
        image.blit(self.sprite_sheet,(0,0),(x,y,32,32))
        return image

    def change_animation(self, name): self.image = self.images[name]
