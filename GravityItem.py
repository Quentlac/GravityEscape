from Item2D import Item2D
class GravityItem(Item2D):

    items = []
    def __init__(self, pos, size, gravity):
        super().__init__(pos, size)

        self._forceX = 0
        self._forceY = 0
        self._gravity = gravity
        GravityItem.newItem(self)

    def invertGravity(self):
        self._gravity = -self._gravity
    def setForce(self, force):
        self._forceX = force[0]
        self._forceY = force[1]
    def addForce(self, force):
        self._forceX += force[0]
        self._forceY += force[1]

    def testCollisionWithOtherItem(self, o : 'Item2D'):
        if(self == o):
            return False

        return abs(self._posX + self._forceX - o.getPosX()) < ((self._width + o.getWidth()) / 2) and abs(self._posY + self._forceY - o.getPosY()) < ((self._height + o.getHeight()) / 2)


    def move(self):

        self.addForce((0, self._gravity))

        # On calcule toute les collisions et on applique les forces nécessaires
        for i in GravityItem.getItems():
            # Collision avec un élément (autre bloc par exemple)
            if self.testCollisionWithOtherItem(i):
                self.addForce((-self._forceX, -self._forceY))


        nextX = self._posX + self._forceX
        nextY = self._posY + self._forceY

        self.setPosition(nextX, nextY)

    def display(self, canva):
        if(self._gravity > 0):
            super().display(canva, 'orange')
        elif(self._gravity < 0):
            super().display(canva, 'cyan')
        else:
            super().display(canva, 'white')

    @classmethod
    def getItems(cls):
        return cls.items

    @classmethod
    def newItem(cls, item : 'GravityItem'):
        cls.items.append(item)


