from pygame import display, event, font, Surface
from pygame.locals import *
import pygame
from sys import exit

class Game:
    def __init__(self):
        #self.screen = pygame.display.set_mode([426, 240])
        self.screen = pygame.display.set_mode([426, 240], pygame.FULLSCREEN)
        pygame.display.set_caption('Pong Reloaded Ultra Gamer Edition 2: Electric Boogaloo')
        self.scene = SceneMenu(self)
        self.main_loop()
    def draw(self):
        self.screen.fill((0, 0, 0))
        self.scene.surface.fill((0, 0, 0))
        self.scene.draw()
        self.screen.blit(self.scene.surface, (0, 0))
        pygame.display.flip()
    def handle_events(self, events):
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                exit()
            else:
                self.scene.handle_event(event)
    def step(self):
        self.scene.step()
    def main_loop(self):
        while True:
            self.handle_events(event.get())
            self.step()
            self.draw()

class Scene:
    def __init__(self, game):
        self.game = game
        self.surface = Surface([426, 240])
        self.font = font.SysFont('Comic Sans MS', 16)
        self.font_bold = font.SysFont('Comic Sans MS', 18, bold=True)
    def draw(self):
        pass
    def handle_event(self, event):
        pass
    def step(self):
        pass

class SceneMenu(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.options = ["New game", "Options", "Quit"]
        self.current_option = 0
    def draw(self):
        for index, option in enumerate(self.options):
            text = self.font.render(option, False, (100, 100, 100))
            self.surface.blit(text, (60, 100 + 20*index))

        text = self.font.render('>', False, (100, 255, 255))
        self.surface.blit(text, (50, 100 + 20*self.current_option))
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.current_option = (self.current_option - 1) % len(self.options)
            if event.key == pygame.K_DOWN:
                    self.current_option = (self.current_option + 1) % len(self.options)