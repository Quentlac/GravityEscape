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
        self._nbBounce = 0

    def display(self, canva):
        if self.active:
            pygame.draw.circle(canva, 'green', (self._posX, self._posY), self.getWidth())

    def bounce(self, b : 'Item2D'):
        if(self._nbBounce < 3):
            if (abs(self.getPosX() - b.getPosX()) > (self.getWidth() + b.getWidth()) / 2):
                self._directionX = -self._directionX
            else:
                self._directionY = -self._directionY

            self._nbBounce += 1
        else:
            self.active = False

    def move(self, dt):
        if self.active:
            dx = self._directionX * self._speed * dt
            dy = self._directionY * self._speed * dt

            col = False

            for b in GravityItem.getItems():
                if(not b._isPlayer and self.testCollisionWithOtherItem(b, dx, dy)):
                    col = True
                    if(isinstance(b, GravityBloc)):
                        b.invertGravity()
                        self.active = False

                    else:
                        self.bounce(b)

            if(not col):
                self.setPosition(self.getPosX() + dx, self.getPosY() + dy)