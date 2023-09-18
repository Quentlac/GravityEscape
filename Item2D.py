import pygame.draw


class Item2D:
    def __init__(self, pos, size):
        self._posX = pos[0]
        self._posY = pos[1]
        self._width = size[0]
        self._height = size[1]

    def setPosition(self, posX, posY):
        self._posX = posX
        self._posY = posY

    def getPosX(self):
        return self._posX

    def getPosY(self):
        return self._posY

    def getWidth(self):
        return self._width

    def getHeight(self):
        return self._height

    def testCollision(self, posX, posY):
        return abs(self._posX - posX) < self._width / 2 and abs(self._posY - posY) < self._height / 2

    def display(self, canva, color):
        pygame.draw.rect(canva, 'black', pygame.Rect(self._posX - self._width/2, self._posY - self._height / 2, self._width, self._height))
        pygame.draw.rect(canva, color, pygame.Rect(self._posX - (self._width-5)/2, self._posY - (self._height-5)/2, self._width-5, self._height-5))


    def move(self, dX, dY):
        self._posX += dX
        self._posY += dY