from Item2D import Item2D
class GravityItem(Item2D):

    items = []
    def __init__(self, pos, size, gravity, weight = 1):
        super().__init__(pos, size)

        self._forceX = 0
        self._forceY = 0
        self._gravity = gravity
        self._isPlayer = False
        self._weight = weight
        GravityItem.newItem(self)

    def invertGravity(self):
        self._gravity = -self._gravity
    def setForce(self, force):
        self._forceX = force[0]
        self._forceY = force[1]
    def addForce(self, force):
        self._forceX += force[0]
        self._forceY += force[1]

    def testCollisionWithOtherItem(self, o : 'Item2D', dx = 0, dy = 0):
        if(self == o):
            return False

        return abs(self._posX + dx - o.getPosX()) < ((self._width + o.getWidth()) / 2) and abs(self._posY + dy - o.getPosY()) < ((self._height + o.getHeight()) / 2)


    def move(self, dt):

        self.addForce((0, self._gravity))

        dx = self._forceX * dt
        dy = self._forceY * dt

        # On calcule toute les collisions et on applique les forces nécessaires
        for i in GravityItem.getItems():

            # Collision avec un élément (autre bloc par exemple)
            if self.testCollisionWithOtherItem(i, dx, dy):
                if self._isPlayer:
                    self._isJump = False
                    self.addForce((-self._forceX + i._forceX, -self._forceY + i._forceY))

                elif(not i._isPlayer):
                    self.addForce((-self._forceX + i._forceX * 0.5, -self._forceY + i._forceY * 0.5))

        dx = self._forceX * dt
        dy = self._forceY * dt

        nextX = self._posX + dx
        nextY = self._posY + dy

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


