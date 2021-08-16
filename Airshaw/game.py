from player import Player
import pygame

class Game:

    def __init__(self):
        self.player = Player()
        self.pressed = { }
        self.titre=pygame.display.set_caption("comet fall game")
        self.background = pygame.image.load('assets/fonts/bg.jpg')
        self.screen = pygame.display.set_mode((1080, 720))

    def run(self):
        running = True
        clock = pygame.time.Clock()
        while running:

            self.screen.blit(self.background, (0, -200))
            # print(game.pressed)
            self.screen.blit(self.player.image, self.player.rect)
            # print(player.rect)

            if self.pressed.get(pygame.K_d) and self.player.rect.x+self.player.rect.width<self.screen.get_width() :
                self.player.move_right()
            elif self.pressed.get(pygame.K_q) and self.player.rect.x>0:
                self.player.move_left()

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    print('fermeture')

                elif event.type == pygame.KEYDOWN:
                    self.pressed[event.key] = True
                elif event.type == pygame.KEYUP:
                    self.pressed[event.key] = False
            clock.tick(60) #dsfdfs
