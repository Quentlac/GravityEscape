from Bloc.StaticBloc import StaticBloc
from Item.GravityItem import GravityItem
from Player import Player


class NoKillBloc(GravityItem):
    def __init__(self, pos, size, material):
        super().__init__(pos, size, material)

    def testCollisionWithOtherItem(self, o, dx=0, dy=0):
        if isinstance(o, Player):
            return False
        else:
            return super().testCollisionWithOtherItem(o, o, dx)
