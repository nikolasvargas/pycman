from assets.colors import COLOR
from chars import Pacman
from pygame import Surface
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT
from typing import Tuple
import configparser
import pygame as _PYG


_PYG.init()

_CFG = configparser.ConfigParser()
_CFG.read('game_config.ini')

SCREEN_WIDTH = int(_CFG['SCREEN']['WIDTH'])
SCREEN_HEIGHT = int(_CFG['SCREEN']['HEIGHT'])

WINDOW_SIZE: Tuple[int] = (SCREEN_WIDTH, SCREEN_HEIGHT)
WINDOW: Surface = _PYG.display.set_mode(WINDOW_SIZE)

FPS = int(_CFG['SCREEN']['FRAMES'])


def run() -> None:
    running: bool = True

    while running:
        WINDOW.fill(COLOR['DARK'])

        Pacman(WINDOW, (SCREEN_WIDTH, SCREEN_HEIGHT))

        _PYG.display.update()

        for event in _PYG.event.get():
            escape: bool = event.type == KEYDOWN and event.key == K_ESCAPE
            exit_key: bool = event.type == QUIT or escape

            if exit_key:
                running = False

    _PYG.quit()


if __name__ == '__main__':
    run()
