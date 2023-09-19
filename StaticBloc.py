from GravityItem import GravityItem

class StaticBloc(GravityItem):

    def __init__(self, pos):
        super().__init__(pos, (50, 50), 0)