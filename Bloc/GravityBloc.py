from Item.GravityItem import GravityItem

class GravityBloc(GravityItem):
    def __init__(self, pos, size=(50, 50), gravity=0.0003):
        super().__init__(pos, size, gravity)

    def invertGravity(self, button):
        self._gravity = -self._gravity

    def display(self, canva, camera):
        super().display(canva, camera)


    @classmethod
    def getItems(cls):
        l = []
        for i in GravityItem.getItems():
            if(isinstance(i, GravityBloc)):
                l.append(i)

        return l