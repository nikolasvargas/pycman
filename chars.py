from assets.colors import COLOR
from pygame import draw, Surface, Rect
from typing import List, Tuple


def pacman(window: Surface, pos: Tuple[int]) -> None:
    circle_rect = (x, y) = [p // 2 for p in pos]
    radius: int = 50
    fill: int = 0

    def _b() -> Rect:
        x_r: Tuple[int] = (x + radius, y - radius)
        y_r: Tuple[int] = (x + radius, y)
        polygon_rects: List[int] = [circle_rect, x_r, y_r]
        return draw.polygon(window, COLOR['DARK'], polygon_rects, fill)

    def _e() -> Rect:
        e_x = (x + (radius // 3))
        e_y = (y - int(radius * 0.5))
        e_radius = radius // 10
        return draw.circle(window, COLOR['DARK'], (e_x, e_y), e_radius, fill)

    draw.circle(window, COLOR['YELLOW'], circle_rect, radius, fill)
    _b()
    _e()
