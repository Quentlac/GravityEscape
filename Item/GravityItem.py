from Item.Item2D import Item2D


class GravityItem(Item2D):
    items = []

    def __init__(self, pos, size, gravity=0, weight=1, is_solid=True):
        super().__init__(pos, size)

        self._forceX = 0
        self._forceY = 0
        self._gravity = gravity
        self._isPlayer = False
        self._weight = weight
        if is_solid:
            GravityItem.newItem(self)

    def setForce(self, force):
        self._forceX = force[0]
        self._forceY = force[1]

    def addForce(self, force):
        self._forceX += force[0]
        self._forceY += force[1]

    def move(self, dt):

        self.addForce((0, self._gravity * dt))

        dx = self._forceX * dt
        dy = self._forceY * dt

        t = False

        # On calcule toute les collisions et on applique les forces nécessaires
        for i in GravityItem.getItems():

            # Collision avec un élément (autre bloc par exemple)
            if self.testCollisionWithOtherItem(i, dx, dy):
                if self._isPlayer:
                    if(self._forceY > 0):
                        self._isJump = False

                    if(t == False):
                        self.addForce((-self._forceX + i._forceX, -self._forceY + i._forceY))
                        t = True
                    else:
                        self.addForce((i._forceX, i._forceY))


                elif (not i._isPlayer):
                    self.addForce((-self._forceX + i._forceX * 0.5, -self._forceY + i._forceY * 0.5))

        dx = self._forceX * dt
        dy = self._forceY * dt

        nextX = self._posX + dx
        nextY = self._posY + dy

        self.setPosition(nextX, nextY)

    @classmethod
    def getItems(cls):
        return cls.items

    @classmethod
    def newItem(cls, item: 'GravityItem'):
        cls.items.append(item)

    def display(self, canva, camera):
        if (self._gravity > 0):
            super().display(canva, camera, 'orange')
        elif (self._gravity < 0):
            super().display(canva, camera, 'darkcyan')
        else:
            super().display(canva, camera, 'white')
