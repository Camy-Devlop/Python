import pygame
from game import Game
from player import Player

pygame.init()

pygame.display.set_caption("comet fall game")
screen = pygame.display.set_mode((1080, 720))

background = pygame.image.load('bg.jpg')

game = Game()

player = Player()

running = True

while running:
#pfsd
    screen.blit(background, (0, -200))

    screen.blit(player.image, player.rect)

    if game.pressed.get(pygame.K_d):
        game.player.move_right()
    elif game.pressed.get(pygame.K_q):
        game.player.move_left()

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print('fermeture')

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
