import pygame as pg

from Bloc.StaticBloc import StaticBloc
from view.Materials import Materials


class BlocSelector:
    cell_size = 30

    def __init__(self, screen, editor):
        self.editor = editor
        self.rect = None
        self.screen = screen
        self.half_cell_size = self.cell_size / 2
        # Get X coordonates to center the blocs
        self.x_center = (screen.get_size()[0] - len(Materials.materials) * self.cell_size) // 2

    def update(self, events):
        # Check if a clicked event is registered
        click_event = None
        for event in events:
            if event.type == pg.MOUSEBUTTONUP:
                click_event = event

        i = 0
        for x, material in Materials.as_list():
            # Change y position if the bloc is the selected one
            pos_y = 8 if x == self.editor.current_material else 0
            pos_y += self.cell_size / 2
            # Get rectangle
            rect = pg.Rect(self.x_center + i * self.cell_size, pos_y, self.cell_size, self.cell_size)

            if type(material) == tuple:
                material = material[0]
            bloc = StaticBloc((self.x_center + i * self.cell_size + self.half_cell_size, pos_y),
                              (self.cell_size, self.cell_size), material)
            bloc.display(self.screen, self.editor.level.camera)
            # If the click is one of the element, update selected element
            if click_event and rect.collidepoint(click_event.pos):
                self.editor.current_material = x
                events.remove(click_event)
                # Height pos will be updated in next frame
            i += 1
