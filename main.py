from assets.colors import COLOR
from chars import pacman
from pygame import Surface
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT
from typing import Tuple
import configparser
import pygame


_CFG = configparser.ConfigParser()
_CFG.read('game_config.ini')

SCREEN_WIDTH = int(_CFG['SCREEN']['WIDTH'])
SCREEN_HEIGHT = int(_CFG['SCREEN']['HEIGHT'])
WINDOW_SIZE: Tuple[int] = (SCREEN_WIDTH, SCREEN_HEIGHT)

pygame.init()

WINDOW: Surface = pygame.display.set_mode(WINDOW_SIZE)


def run():
    running: bool = True

    while running:
        WINDOW.fill(COLOR['DARK'])

        pacman(WINDOW, (SCREEN_WIDTH, SCREEN_HEIGHT))

        pygame.display.update()

        for event in pygame.event.get():
            escape: bool = event.type == KEYDOWN and event.key == K_ESCAPE
            exit_key: bool = event.type == QUIT or escape

            if exit_key:
                running = False

    pygame.quit()


if __name__ == '__main__':
    run()
