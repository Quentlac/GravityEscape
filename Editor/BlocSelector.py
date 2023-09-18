import os
import json
import pygame as pg

from Bloc import Bloc
from Materials import Materials


class BlocSelector:
    cell_size = 100

    def __init__(self, screen, editor):
        self.editor = editor
        self.rect = None
        self.screen = screen
        # Get X coordonates to center the blocs
        self.x_center = (screen.get_size()[0] - len(Materials.materials) * self.cell_size) // 2

    def update(self, events):
        # Check if a clicked event is registered
        click_event = None
        for event in events:
            if event.type == pg.MOUSEBUTTONUP:
                click_event = event

        for x, material in enumerate(Materials.as_list()):

            # Change y position if the bloc is the selected one
            pos_y = 8 if x == self.editor.current_material else 0
            # Get rectangle
            rect = pg.Rect(self.x_center + x * self.cell_size, pos_y, self.cell_size, self.cell_size)

            bloc = Bloc(self.x_center + x * self.cell_size, pos_y, material[1])
            bloc.update(self.screen)
            # If the click is one of the element, update selected element
            if click_event and rect.collidepoint(click_event.pos):
                self.editor.current_material = x + 1
                print("change material")
                # Height pos will be updated in next frame
