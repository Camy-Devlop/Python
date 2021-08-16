import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super(Player, self).__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.image = pygame.image.load('assets/player/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 450
        self.rect.y = 500

    def move_right(self):
        self.rect.x += self.velocity
        print(self.rect.x)

    def move_left(self):
        self.rect.x -= self.velocity


