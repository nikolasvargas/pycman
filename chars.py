from assets.colors import COLOR
from pygame import draw, Surface, Rect
from typing import List, Tuple


class Pacman:
    def __init__(self, window: Surface, pos: Tuple[int]) -> None:
        self.circle_rect = (self.x, self.y) = [p // 2 for p in pos]
        self.radius: int = 50
        self.fill: int = 0
        self.window: Surface = window
        self.draw_pacman()

    def _lips(self) -> Rect:
        x_r: Tuple[int] = (self.x + self.radius, self.y - self.radius)
        y_r: Tuple[int] = (self.x + self.radius, self.y)
        polygon_rects: List[int] = [self.circle_rect, x_r, y_r]
        return draw.polygon(self.window, COLOR['DARK'], polygon_rects, self.fill)

    def _eyes(self) -> Rect:
        e_x = (self.x + (self.radius // 3))
        e_y = (self.y - int(self.radius * 0.5))
        e_radius = self.radius // 10
        return draw.circle(self.window, COLOR['DARK'], (e_x, e_y), e_radius, self.fill)

    def draw_pacman(self) -> None:
        draw.circle(self.window, COLOR['YELLOW'], self.circle_rect, self.radius, self.fill)
        self._lips()
        self._eyes()
