import os
import json
import pygame as pg
import pygame.mouse

from Bloc.StaticBloc import StaticBloc
from Camera import Camera
from view.Materials import Materials


class Level:
    bloc_size = 50

    def __init__(self, screen: pg.Surface, editor):
        self.editor = editor
        # Loading level file
        self.screen = screen
        with open(os.path.dirname(os.path.realpath(__file__)) + "/../Levels/" + self.editor.level_name,
                  "r") as f:
            self.json_data = json.load(f)

        self.size = self.json_data["size"]
        # Grid setup
        self.grid = self.json_data["grid"]
        # If grid stored is lower than requested size, create bigger grid.
        # If the grid is bigger, do nothing
        if len(self.grid) < self.size[0]:
            for x in range(self.size[0]):
                self.grid.extend(
                    [[] for _ in range((self.size[0] - len(self.grid)))])  # Extend grid with current_size - target_size
        for column in self.grid:
            if len(column) < self.size[0]:
                column.extend([0] * (self.size[1] - len(column)))

        # Get center of the screen
        self.grid_width = self.size[1] * self.bloc_size
        self.grid_height = self.size[0] * self.bloc_size
        self.x_center = (screen.get_size()[0] - self.grid_width) // 2
        self.y_center = (screen.get_size()[1] - self.grid_height) // 2

        self.half_bloc_size = self.bloc_size / 2

        self.camera_pos = pg.Vector2()

        # Needed for render block but useless here, attribute change make it invisible in calcul
        self.camera = Camera(None, (0,0))
        self.camera.camera_width = 0
        self.camera.camera_height = 0

    def draw_grid(self, events, dt):
        # Retreive click event if one
        click_event = None

        for event in events:
            if event.type == pg.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                if y > 40:
                    click_event = event
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_k:
                    self.save()

        keys = pg.key.get_pressed()
        if keys[pg.K_d]:
            self.camera_pos.x -= 1 * dt
        if keys[pg.K_q]:
            self.camera_pos.x += 1 * dt
        if keys[pg.K_s]:
            self.camera_pos.y -= 1 * dt
        if keys[pg.K_z]:
            self.camera_pos.y += 1 * dt

        # Draw grid
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                rect = pg.Rect((self.camera_pos.x + self.x_center + y * self.bloc_size) - self.half_bloc_size,
                               (self.camera_pos.y + self.y_center + x * self.bloc_size) - self.half_bloc_size, self.bloc_size,
                               self.bloc_size)
                if self.grid[x][y] != 0:
                    material = Materials.get_material(self.grid[x][y])
                    if type(material) == tuple:
                        material = material[0]
                    bloc = StaticBloc((self.camera_pos.x + self.x_center + y * self.bloc_size,
                                       self.camera_pos.y + self.y_center + x * self.bloc_size),
                                      (self.bloc_size, self.bloc_size), material)
                    bloc.display(self.screen, self.camera)

                if click_event and rect.collidepoint(click_event.pos):
                    if click_event.button == 3:
                        self.grid[x][y] = 0
                    else:
                        self.grid[x][y] = self.editor.current_material

        rect = pg.Rect(self.camera_pos.x + self.x_center - self.half_bloc_size,
                       self.camera_pos.y + self.y_center - self.half_bloc_size, self.grid_width,
                       self.grid_height)
        pg.draw.rect(self.screen, (200, 200, 200), rect, 1)

    def save(self):
        with open(os.path.dirname(os.path.realpath(__file__)) + "/../Levels/" + self.editor.level_name,
                  "w") as f:
            print("save")
            f.write(json.dumps(self.json_data))
