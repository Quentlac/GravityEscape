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
            if self._gravity < 0 and button == 0:
                super().invertGravity(button)
            elif self._gravity > 0 and button == 1:
                super().invertGravity(button)
            else:
                self.is_stop = True
                self._gravity = 0

    def move(self, dt):
        if self.is_stop:
            self.addForce((0, -self._forceY * 0.2))

        super().move(dt)
        

