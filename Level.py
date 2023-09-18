import json
import os

from Materials import Materials
from Bloc import Bloc


class Level:

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

        except json.JSONDecodeError:
            print("Error decoding level json file")
        except KeyError as e:
            print("Missing key in level file: ", e)

        # Get center of the screen
        self.grid_width = self.size[1] * Bloc.size
        self.grid_height = self.size[0] * Bloc.size
        self.x_center = (screen.get_size()[0] - self.grid_width) // 2
        self.y_center = (screen.get_size()[1] - self.grid_height) // 2

        self.load_grid()

    def load_grid(self):
        # Draw grid
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                if self.grid[x][y] != 0:
                    material = Materials.get_material(self.grid[x][y])
                    bloc = Bloc(self.x_center + y * Bloc.size, self.y_center + x * Bloc.size, material)
                    self.level_elements.append(bloc)

    def update(self):
        for elem in self.level_elements:
            elem.update(self.screen)
