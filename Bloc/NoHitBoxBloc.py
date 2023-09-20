from Bloc.StaticBloc import StaticBloc
from Item.BulletItem import BulletItem
from Item.Item2D import Item2D
from Player import Player


class NoHitBoxBloc(StaticBloc):
    def __init__(self, pos, size, material):
        super().__init__(pos, size, material, False)

    def testCollisionWithOtherItem(self, o: 'Item2D', dx=0, dy=0):
        if isinstance(o, Player):
            return False
        else:
            super().testCollisionWithOtherItem(o, dx, dy)

