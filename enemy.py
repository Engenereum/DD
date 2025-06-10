import os
import random

import pygame
from pygame import Surface
from pygame.examples.aliens import Player
from pygame.sprite import Sprite, Group

from collisions import check_out, is_collide_enemies

enemies_paths = ["2/enemies/enemy1/"]

def spawn(count, screen):
    enemies = Group()
    current_count = 0
    while current_count < count:
        x1 = random.randint(100, 400)
        x2 = random.randint(600, 1800)
        x = random.choice([x1, x2])
        y1 = random.randint(100, 200)
        y2 = random.randint(400, 1000)
        y = random.choice([y1, y2])
        path = random.choice(enemies_paths)
        enemy = Enemy(path,x ,y, screen)
        if is_collide_enemies(enemy.rect, enemies):
            continue
        else:
            enemies.add(enemy)
            current_count += 1
    print("----------------")
    return enemies


class Enemy(Sprite):
    def __init__(self, path, x, y, screen):
        self.screen = screen
        super().__init__()
        self.anims = {
            "down": Animation(path+"down/"),
            "left": Animation(path+"left/"),
            "right": Animation(path+"right/"),
            "up": Animation(path+"up/"),
        }
        self.anim = self.anims["down"]
        self.image = self.anim.image
        self.rect = self.image.get_rect(center=(x,y))


    def update(self, player: Player, enemies=None):
        x, y = self.rect.center
        x1, y1 = player.rect.center
        dx, dy = x - x1, y - y1
        if x < x1:
            direct_x = "right"
        else:
            direct_x = "left"
        if y1 < y:
            direct_y = "up"
        else:
            direct_y = "down"
        if dx < dy:
            direct = direct_x
        else:
            direct = direct_y
        self.anim = self.anims[direct]
        self.anim.update()
        self.image = self.anim.image
        dx, dy = 0,0
        if x < x1:
            dx += 5
        else:
            dx -= 5
        if y < y1:
            dy += 5
        else:
            dy -= 5
        rect = self.rect.move(dx, 0)
        if not check_out(rect, self.screen) and is_collide_enemies(rect, enemies):
            self.rect = rect
        rect = self.rect.move(0, dy)
        if not check_out(rect, self.screen) and is_collide_enemies(rect, enemies):
            self.rect = rect

    def draw(self, screen : Surface):
        ...

class Animation:
    def __init__(self, path):
        self.path = path
        files = os.listdir(path)
        self.images = []
        for file in files:
            image = pygame.image.load(f"{self.path}{file}").convert_alpha()
            image = pygame.transform.scale(image, (150, 150))
            # image.set_colorkey(pygame.color.Color('white'))
            self.images.append(image)
        self.index = 0
        self.image = self.images[self.index]
        self.playing = True

    def update(self):
        if self.playing:
            self.index += 1
            self.index %= len(self.images)
            self.image = self.images[self.index]
        else:
            self.image = self.images[0]

    def draw(self, screen: Surface):
        screen.blit(self.image, (0, 0))
