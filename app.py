import pygame
from enemy import spawn
from enviroment import Environment
import interface
from player import Player

def create_cursor():
    surface = pygame.image.load("2/City_locator_20.svg.png")
    hotspot = (25, 25)
    surface = pygame.transform.scale(surface, (50,50))
    cursor = pygame.cursors.Cursor(hotspot, surface)
    return cursor

class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((1550, 900))
        self.clock = pygame.time.Clock()
        self.player = Player(self.screen)
        self.map = Environment(self.screen)
        self.enemies = spawn(5, self.screen)
        pygame.mouse.set_cursor(create_cursor())
        self.interface = interface.Interface()

    def run(self):
        running = True
        while running:
            events =pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    running = False
            keys = pygame.key.get_pressed()
            self.player.update(events, keys)
            self.enemies.update(self.player, self.enemies)
            self.screen.fill((255,255,255))
            self.map.draw(self.screen)
            self.player.draw(self.screen)
            self.enemies.draw(self.screen)
            self.interface.draw(self.screen, 5)
            pygame.display.flip()
            self.clock.tick(30)


if __name__ == "__main__":
    pygame.init()
    app = App()
    app.run()