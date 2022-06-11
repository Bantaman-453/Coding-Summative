import pygame
import sys
from settings import *
from level import Level
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
)


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Jared's Zelda Game")
        self.clock = pygame.time.Clock()

        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            self.screen.fill('black')
            self.level.run()
            self.clock.tick(FPS)
            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()
