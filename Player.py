from GravityItem import GravityItem
import pygame
class Player(GravityItem):

    def __init__(self, pos):
        super().__init__(pos, (20, 20), 0.02)
        self._isPlayer = True
        self._isJump = False

    def display(self, canva):
        pygame.draw.rect(canva, 'red', pygame.Rect(self._posX - self._width / 2, self._posY - self._height / 2, self._width, self._height))

    def jump(self):
        if(not self._isJump):
            self._isJump = True
            self.addForce((0, -0.5))

    def goRight(self, dt):
        nextX = self.getPosX() + 0.15 *dt
        nextY = self.getPosY()

        self.setPosition(nextX, nextY)

        col = False
        for b in GravityItem.getItems():
            if b.testCollisionWithOtherItem(self):
                col = True

        if col:
            self.setPosition(nextX - 0.15 * dt, nextY)

    def goLeft(self, dt):
        nextX = self.getPosX() - 0.15 * dt
        nextY = self.getPosY()

        self.setPosition(nextX, nextY)

        col = False
        for b in GravityItem.getItems():
            if b.testCollisionWithOtherItem(self):
                col = True

        if col:
            self.setPosition(nextX + 0.15*dt, nextY)


