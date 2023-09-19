from Item.Item2D import *
import pygame

class BulletItem(Item2D):

    def __init__(self, pos, visee):
        super().__init__(pos, (5, 5))
        self._directionX = visee[0]
        self._directionY = visee[1]
        self._speed = 0.5

    def display(self, canva):
        pygame.draw.circle(canva, 'green', (self._posX, self._posY), self.getWidth())

    def move(self, dt):
        dx = self._directionX * self._speed * dt
        dy = self._directionY * self._speed * dt

        self.setPosition(self.getPosX() + dx, self.getPosY() + dy)