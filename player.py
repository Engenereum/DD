import os

import pygame
import pygame.display
from pygame import Surface
from pygame.sprite import Sprite

from collisions import check_out


class Player(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.anims = {
            "down": Animation("2/1/down/"),
            "right": Animation("2/1/right/"),
            "up": Animation("2/1/up/"),
            "left": Animation("2/1/left/"),
            "top_left": Animation("2/1/top_left/"),
            "top_right": Animation("2/1/top_right/"),
            "bottom_left": Animation("2/1/bottom_left/"),
            "bottom_right": Animation("2/1/bottom_right/"),
            "idle": Animation("2/1/idle/")
        }
        self.image = self.anims["down"].image
        w, h = screen.get_size()
        self.rect = self.image.get_rect(center=(w//2, h //2))
        self.current_anim = "down"
        self.anim = self.anims[self.current_anim]

    def update(self, events, keys):
        self.anims[self.current_anim].playing = True
        if keys[pygame.K_w] and keys[pygame.K_a]:
            self.current_anim = "top_left"
        elif keys[pygame.K_w] and keys[pygame.K_d]:
            self.current_anim = "top_right"
        elif keys[pygame.K_s] and keys[pygame.K_a]:
            self.current_anim = "bottom_left"
        elif keys[pygame.K_s] and keys[pygame.K_d]:
            self.current_anim = "bottom_right"
        elif keys[pygame.K_s]:
            self.current_anim = "down"
        elif keys[pygame.K_d]:
            self.current_anim = "right"
        elif keys[pygame.K_w]:
            self.current_anim = "up"
        elif keys[pygame.K_a]:
            self.current_anim = "left"
        else:
            #self.current_anim = "idle"
            self.anims[self.current_anim].playing = False


        self.anim = self.anims[self.current_anim]
        self.anim.update()
        self.image = self.anim.image
        x, y = 0,0
        if keys[pygame.K_s]:
            y += 10
        if keys[pygame.K_w]:
            y -= 10
        if keys[pygame.K_a]:
            x -= 10
        if keys[pygame.K_d]:
            x += 10

        rect = self.rect.move(x, 0)
        if not check_out(rect, self.screen):
            self.rect = rect
        rect = self.rect.move(0, y)
        if not check_out(rect, self.screen):
            self.rect = rect

    def draw(self, screen: Surface):
        screen.blit(self.image, self.rect)

class Animation:
    def __init__(self, path):
        self.path = path
        files = os.listdir(path)
        self.images = []
        for file in files:
            image = pygame.image.load(f"{self.path}{file}").convert_alpha()
            image = pygame.transform.scale(image, (100, 100))
            #image.set_colorkey(pygame.color.Color('white'))
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

