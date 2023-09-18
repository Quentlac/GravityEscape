from Level import Level
from BlocSelector import BlocSelector


class Editor:

    def __init__(self, screen):
        self.level_name = input("Nom du niveau ?")
        self.level = Level(screen, self)
        self.bloc_selector = BlocSelector(screen, self)
        self.current_material = 1

    def update(self, events, dt):
        self.level.draw_grid(events, dt)
        self.bloc_selector.update(events)
