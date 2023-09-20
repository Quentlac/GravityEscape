from Bloc.NoHitBoxBloc import NoHitBoxBloc
from Bloc.StaticBloc import StaticBloc
from Player import Player


class SpawnBloc(NoHitBoxBloc):

    def __init__(self, pos, material):
        super().__init__(pos, (50, 50), material)