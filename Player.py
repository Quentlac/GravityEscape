from GravityItem import GravityItem
import pygame
class Player(GravityItem):

    def __init__(self, pos):
        super().__init__(pos, (20, 20), 0.0002)
        self._isPlayer = True
        self._isJump = False

    def display(self, canva):
        pygame.draw.rect(canva, 'red', pygame.Rect(self._posX - self._width / 2, self._posY - self._height / 2, self._width, self._height))

    def jump(self):
        if(not self._isJump):
            self._isJump = True
            self.addForce((0, -0.2))

    def goRight(self):
        nextX = self.getPosX() + 0.1
        nextY = self.getPosY()

        self.setPosition(nextX, nextY)

        col = False
        for b in GravityItem.getItems():
            if b.testCollisionWithOtherItem(self):
                col = True

        if col:
            self.setPosition(nextX - 0.1, nextY)

    def goLeft(self):
        nextX = self.getPosX() - 0.1
        nextY = self.getPosY()

        self.setPosition(nextX, nextY)

        col = False
        for b in GravityItem.getItems():
            if b.testCollisionWithOtherItem(self):
                col = True

        if col:
            self.setPosition(nextX + 0.1, nextY)

    def move(self):
        self.addForce((0, self._gravity))

        # On calcule toute les collisions et on applique les forces nécessaires
        for i in GravityItem.getItems():
            # Collision avec un élément (autre bloc par exemple)
            if self.testCollisionWithOtherItem(i):
                self.setForce((i._forceX, i._forceY))
                self._isJump = False

        nextX = self._posX + self._forceX
        nextY = self._posY + self._forceY

        self.setPosition(nextX, nextY)
