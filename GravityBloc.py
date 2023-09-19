from GravityItem import GravityItem

class GravityBloc(GravityItem):
    def __init__(self, pos):
        super().__init__(pos, (50, 50), 0.003)

    def invertGravity(self):
        self._gravity = -self._gravity

    def display(self, canva):
        super().display(canva)