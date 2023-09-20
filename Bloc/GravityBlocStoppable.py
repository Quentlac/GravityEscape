from Bloc.GravityBloc import GravityBloc


class GravityBlocStoppable(GravityBloc):
    def __init__(self, pos, size=(50, 50), gravity=0.0003):
        super().__init__(pos, size, 0)
        self.initial_gravity = -gravity
        self.is_stop = True

    def invertGravity(self, button):
        if self.is_stop:
            if button == 1:
                self._gravity = self.initial_gravity
            else:
                self._gravity = -self.initial_gravity
            self.is_stop = False
        else:
            self.is_stop = True
            self.setForce((0, 0))
            self._gravity = 0

    def move(self, dt):
        if not self.is_stop:
            super().move(dt)
