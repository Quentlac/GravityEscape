import json
import os

from view.Materials import Materials
from Bloc.StaticBloc import StaticBloc
from Bloc.NoHitBoxBloc import NoHitBoxBloc
import pygame as pg


class Level:
    default_size = (50, 50)
    def __init__(self, name, screen):
        self.level_elements = []
        self.level_name = name
        self.screen = screen
        try:
            # Loading level file
            with open(os.path.dirname(os.path.realpath(__file__)) + "/Levels/" + name + ".json", "r") as f:
                self.json_data = json.load(f)

            self.size = self.json_data["size"]
            self.grid = self.json_data["grid"]

            self.background = None
            if self.json_data["background"]:
                try:
                    bg = pg.image.load(f"{os.path.dirname(os.path.realpath(__file__))}/view/backgrounds/{self.json_data['background']}")
                    new_width = (bg.get_size()[0] * screen.get_size()[1]) // bg.get_size()[0]
                    bg = pg.transform.scale(bg, (new_width, screen.get_size()[1]))

                    self.background = bg
                except FileNotFoundError as e:
                    print("Background not found")
                    self.background = None

        except json.JSONDecodeError:
            print("Error decoding level json file")
        except KeyError as e:
            print("Missing key in level file: ", e)

        # Get center of the screen
        self.grid_width = self.size[1] * self.default_size[0]
        self.grid_height = self.size[0] * self.default_size[1]
        self.x_center = (screen.get_size()[0] - self.grid_width) // 2
        self.y_center = (screen.get_size()[1] - self.grid_height) // 2

        self.load_grid()

    def load_grid(self):
        # Draw grid
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                if self.grid[x][y] != 0:
                    material = Materials.get_material(self.grid[x][y])
                    pos = (self.x_center + y * self.default_size[0], self.y_center + x * self.default_size[1])
                    if type(material) != tuple:
                        bloc = StaticBloc(pos, self.default_size, material)
                        self.level_elements.append(bloc)
                    else:
                        if type(material[1]) == type(NoHitBoxBloc):
                            bloc = NoHitBoxBloc(pos, self.default_size, material[0])
                        else:
                            bloc = None
                    if bloc:
                        self.level_elements.append(bloc)


    def update(self):
        if self.background:
            x = 0
            while x < self.screen.get_size()[0]:
                self.screen.blit(self.background, (x, 0))
                x += self.background.get_size()[0]

        for elem in self.level_elements:
            elem.display(self.screen)

        pg.draw.rect(self.screen, (0, 0, 0), (self.x_center, self.y_center, self.grid_width, self.grid_height), 4)