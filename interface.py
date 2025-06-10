import pygame.font
from pygame import Surface


class Interface:
    def __init__(self):
        self.surf = Surface((100, 50))
        self.font = pygame.font.Font('GNF.ttf', 50)
        self.level_font = pygame.font.Font('GNF.ttf', 250)
        self.text = self.font.render("==Количество жизней==", 1, (0, 0, 0))
        self.level_text = self.level_font.render("Уровень 1", 1, (0, 0, 0))
        self.heart = pygame.image.load("heart.png").convert_alpha()
        self.heart = pygame.transform.scale(self.heart, (50, 50))
        self.clock_delay = 3
        self.border = pygame.image.load("hurt.png").convert_alpha()
        self.counter = 255

    def draw(self, screen: Surface, count):
        screen.blit(self.text, (0, 0))
        rect = self.text.get_rect()
        for i in range(count):
            screen.blit(self.heart, (i * self.heart.get_width(), rect.h))
        if pygame.time.get_ticks() <= 3 * 1000:
            w, h = screen.get_size()
            rect = self.level_text.get_rect(center=(w // 2, h // 2))
            screen.blit(self.level_text, rect)
        if pygame.time.get_ticks() > 4 * 1000 and self.counter != 0:
            self.draw_damaged(screen)

    def draw_damaged(self, screen):
        size = screen.get_size()
        surface = pygame.surface.Surface(size)
        surface.set_alpha(self.counter)
        border = pygame.transform.scale(self.border, size)
        surface.blit(border, (0, 0))
        screen.blit(surface, (0, 0))
        self.counter = (self.counter - 5) % 255

    # def draw(self, screen: Surface, count):
    #    screen.blit(self.text, (0, 0))
    #    rect = self.text.get_rect()
    #    screen.blit(self.heart, (0 * self.heart.get_width(), rect.h))
    #    w = 10
    #    h = 50
    #    shift = 10
    #    for i in range(count):
    #        pygame.draw.rect(screen, (255, 0, 0), (shift + i * w * 1.1, rect.h, w, h))
