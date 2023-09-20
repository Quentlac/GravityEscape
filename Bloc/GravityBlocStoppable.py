from Bloc.GravityBloc import GravityBloc


class GravityBlocStoppable(GravityBloc):
    def __init__(self, pos, size=(50, 50), gravity=0.0003):
        super().__init__(pos, size, 0)
        self.last_gravity = -gravity
        self.is_stop = True

    def invertGravity(self):
        if self.is_stop:
            self._gravity = -self.last_gravity
            self.is_stop = False
        else:
            self.is_stop = True
            self.last_gravity = self._gravity
            self.setForce((0,0))
            self._gravity = 0

    def move(self, dt):
        if not self.is_stop:
            super().move(dt)
