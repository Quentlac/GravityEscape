from Bloc.StaticBloc import StaticBloc
from Player import Player


class EndBloc(StaticBloc):

    def __init__(self, pos, endcallback, material):
        super().__init__(pos, (50, 50), material)
        self.endcallback = endcallback

    def testCollisionWithOtherItem(self, o, dx=0, dy=0):
        if isinstance(o, Player) and super().testCollisionWithOtherItem(o, dx, dy):
            self.endcallback()
            return False
        else:
            return super().testCollisionWithOtherItem(o, dx, dy)