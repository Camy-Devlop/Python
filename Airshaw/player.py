import pygame
from projectile import Projectile

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super(Player, self).__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.all_projectile= pygame.sprite.Group()
        self.image = pygame.image.load('assets/player/player1.png')
        self.rect = self.image.get_rect()
        self.rect.x = 450
        self.rect.y = 500

    def launch_projectile(self):

        self.all_projectile.add(Projectile())

    def move_right(self):
        
        self.rect.x += self.velocity


    def move_left(self):
        self.rect.x -= self.velocity


