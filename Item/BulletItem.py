from Item.Item2D import *
import pygame

class BulletItem(Item2D):

    def __init__(self, pos, visee):
        super().__init__(pos, (3, 3))
        self._directionX = visee[0]
        self._directionY = visee[1]
        self._speed = 0.5

    def display(self, canva):
        pygame.draw.circle(canva, 'green', (self._posX, self._posY), 10)

    def move(self, dt):
        self.setPosition(self.getPosX() + self._directionX * self._speed * dt, self.getPosY() + self._directionY * self._speed * dt)