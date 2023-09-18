import pygame as pg


class Bloc:
    size = 20

    def __init__(self, x, y, material):
        self.pos = pg.Vector2(x, y)
        self.element = pg.transform.scale(material, (self.size, self.size))

    def update(self, screen: pg.Surface):
        screen.blit(self.element, self.pos)
