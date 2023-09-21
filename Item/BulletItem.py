import random

from Bloc.NoKillBloc import NoKillBloc
from Item.Item2D import *
from Item.GravityItem import *
from Bloc.GravityBloc import *
import pygame

class BulletItem(Item2D):
    sound = None
    cat_sound = None
    def __init__(self, pos, visee, button):
        super().__init__(pos, (5, 5))
        self._directionX = visee[0]
        self._directionY = visee[1]
        self._speed = 0.5
        self.active = True
        self._nbBounce = 0
        self.button = 1 if button == 1 else 0
        rnd = random.Random();
        n = rnd.random()
        if not BulletItem.sound:
            BulletItem.sound = pygame.mixer.Sound("ressources/sound-laser.mp3")
            BulletItem.cat_sound = pygame.mixer.Sound("ressources/sound-cat.mp3")
        if n < 0.98:
            BulletItem.sound.play()
        else:
            BulletItem.cat_sound.play()

    def display(self, canva, camera):
        offset_x, offset_y = camera.getOffset()
        if self.active:
            color = "blue" if self.button == 1 else "orange"
            pygame.draw.circle(canva, color, (offset_x + self._posX, offset_y + self._posY), self.getWidth())

    def bounce(self, b : 'Item2D'):
        if(self._nbBounce < 10):
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
                if(not isinstance(b, NoKillBloc) and not b._isPlayer and self.active and self.testCollisionWithOtherItem(b, dx, dy)):
                    if(isinstance(b, GravityBloc)):
                        b.invertGravity(self.button)
                        self.active = False

                    elif not col:
                        self.bounce(b)

                    col = True


            if(not col):
                self.setPosition(self.getPosX() + dx, self.getPosY() + dy)