import pygame

from Editor.Level import Level
from Editor.BlocSelector import BlocSelector


class Editor:

    def __init__(self, screen, name, callback):
        self.level_name = name
        self.level = Level(screen, self)
        self.bloc_selector = BlocSelector(screen, self)
        self.current_material = 1
        self.callback = callback

    def update(self, events, dt):
        self.level.draw_grid(events, dt)
        self.bloc_selector.update(events)
        for event in events:
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_j:
                    self.level.save()
                    self.callback()
