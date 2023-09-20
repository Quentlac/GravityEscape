from Bloc.GravityBloc import GravityBloc


class InvertGravityBloc(GravityBloc):
    def __init__(self, pos, size=(50, 50), gravity=-0.0003):
        super().__init__(pos, size, gravity)
