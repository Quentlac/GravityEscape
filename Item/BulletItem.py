from Item.Item2D import *
from Item.GravityItem import *
from Bloc.GravityBloc import *
import pygame

class BulletItem(Item2D):

    def __init__(self, pos, visee):
        super().__init__(pos, (5, 5))
        self._directionX = visee[0]
        self._directionY = visee[1]
        self._speed = 0.5
        self.active = True

    def display(self, canva):
        if self.active:
            pygame.draw.circle(canva, 'green', (self._posX, self._posY), self.getWidth())

    def move(self, dt):
        if self.active:
            dx = self._directionX * self._speed * dt
            dy = self._directionY * self._speed * dt

            col = False

            for b in GravityItem.getItems():
                if(not b._isPlayer and self.testCollisionWithOtherItem(b, dx, dy)):
                    col = True
                    self.active = False
                    if(isinstance(b, GravityBloc)):
                        b.invertGravity()

            if(not col):
                self.setPosition(self.getPosX() + dx, self.getPosY() + dy)