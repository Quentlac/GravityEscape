from Bloc.StaticBloc import StaticBloc
from Player import Player


class NoKillBloc(StaticBloc):
    def __init__(self, pos, size, material):
        super().__init__(pos, size, material)

    def testCollisionWithOtherItem(self, o, dx=0, dy=0):
        if isinstance(o, Player):
            return False
        else:
            return super().testCollisionWithOtherItem(o, dx, dy)
