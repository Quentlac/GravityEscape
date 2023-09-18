import os
import json
import pygame as pg


class BlocSelector:
    # Retreive blocs json from file
    with open(os.path.dirname(os.path.realpath(__file__)) + "/blocs.json", "r") as f:
        blocs = json.load(f)

    cell_size = 100

    def __init__(self, screen, editor):
        self.editor = editor
        self.rect = None
        self.screen = screen
        # Get X coordonates to center the blocs
        self.x_center = (screen.get_size()[0] - len(self.blocs) * self.cell_size) // 2

    def update(self, events):
        # Check if a clicked event is registered
        click_event = None
        for event in events:
            if event.type == pg.MOUSEBUTTONUP:
                click_event = event

        for x, bloc in enumerate(self.blocs):

            # Change y position if the bloc is the selected one
            pos_y = 8 if x == self.editor.current_material else 0
            # Get rectangle
            rect = pg.Rect(self.x_center + x * self.cell_size, pos_y, self.cell_size, self.cell_size)

            # Draw rectangle and border
            pg.draw.rect(self.screen, tuple(bloc["color"]), rect, 0)
            pg.draw.rect(self.screen, (200, 200, 200), rect, 1)

            # If the click is one of the element, update selected element
            if click_event and rect.collidepoint(click_event.pos):
                self.editor.current_material = x
                # Height pos will be updated in next frame

    def get_color(self, index) -> tuple[int, int, int]:
        return tuple(self.blocs[index]["color"]) or (200, 200, 200)
