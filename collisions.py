import copy
from operator import truediv

from pygame import Surface, Rect


def check_out(obj : Rect, screen : Surface) -> bool:
    w, h = screen.get_size()
    if obj.left <= 0:
        return True
    elif obj.right >= w:
        return True
    elif obj.top <= 0:
        return True
    elif obj.bottom >= h:
        return True
    else:
        return False

def is_collide_enemies(enemy : Rect, enemies) -> bool:
    enemy_rects = []
    for en in enemies:
        enemy_rects.append(en.rect)
    res = enemy.collidelist(enemy_rects)
    print(res)
    if res > -1:
        return True
    else:
        return False