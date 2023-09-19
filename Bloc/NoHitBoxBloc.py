from Bloc.StaticBloc import StaticBloc
from Item.Item2D import Item2D


class NoHitBoxBloc(StaticBloc):
    def __init__(self, pos, size, material):
        super().__init__(pos, size, material, False)


