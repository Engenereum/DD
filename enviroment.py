import random

import pygame
from pygame import Surface, Rect

level1_map = [
    "11111111111111111111",
    "11111111111111111111",
    "11111111111111111111",
    "11111111111111111111",
    "11111111222221111111",
    "11111111222221111111",
    "11111111222221111111",
    "11111111111111111111",
    "11111111111111111111",
    "11111111111111111111",
    "11111111111111111111",
]
def generate_map(textures: list, rows_count, columns_count):
    map = []
    for i in range(rows_count):
        row = []
        for j in range(columns_count):
            row.append(random.choice(textures))
        map.append(str(row).replace('[', '').replace(']', '').replace(' ', '').replace(',', '').replace("'", ''))
    return map


class Environment:
    def __init__(self, screen : Surface):
        self.grid = []
        w, h = screen.get_size()
        self.rows_count = 11
        self.column_count = 20
        self.cell_w = w // self.column_count
        self.cell_h = h // self.rows_count
        self.textures = {
            "_": pygame.Surface((self.cell_w, self.cell_h)),
            "1": pygame.transform.scale(pygame.image.load("2/1/grid/brick.jpg").convert(), (self.cell_w, self.cell_h)),
            "2": pygame.transform.scale(pygame.image.load("2/1/grid/grass.jpg").convert(), (self.cell_w, self.cell_h)),
            "3": pygame.transform.scale(pygame.image.load("2/1/grid/grass.jpg").convert(), (self.cell_w, self.cell_h)),
            "4": pygame.transform.scale(pygame.image.load("2/1/grid/grass.jpg").convert(), (self.cell_w, self.cell_h)),
        }
        self.map = level1_map #generate_map(list(self.textures.keys()), self.rows_count, self.column_count)
        for i in range(self.rows_count):
            self.grid.append([])
            for j in range(self.column_count):
                index = self.map[i][j]
                self.grid[i].append({
                    "rect": Rect(j * self.cell_w, i * self.cell_h, self.cell_w, self.cell_h),
                    'texture': self.textures[index],
                })


    def draw(self, screen):
        for i in range(self.rows_count):
            for j in range(self.column_count):
                screen.blit(self.grid[i][j]["texture"], self.grid[i][j]['rect'])