import pygame
import pytmx
import pyscroll
import os
from game import Game
import arcade

if __name__ == '__main__':
    pygame.init()
    games = Game()
    games.run()
