from pygame import display
import pygame
from classes import Game

def init():
    global GAME
    pygame.init()
    GAME = Game()

if __name__ == '__main__':
    init()