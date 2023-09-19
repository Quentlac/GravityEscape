import json
import os

from Camera import Camera
from Player import Player
from view.Materials import Materials
from Bloc.StaticBloc import StaticBloc
from Bloc.NoHitBoxBloc import NoHitBoxBloc
from Bloc.GravityBloc import GravityBloc
import pygame as pg


class Level:
    default_size = (50, 50)
    list_gravity_bloc = []

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
                    bg = pg.image.load(
                        f"{os.path.dirname(os.path.realpath(__file__))}/view/backgrounds/{self.json_data['background']}")
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

        self.player = Player((200, 200))

        self.camera = Camera(self.grid_width, self.grid_height, self.x_center, self.y_center)

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

                        if material[1] == NoHitBoxBloc:
                            bloc = NoHitBoxBloc(pos, self.default_size, material[0])
                        elif material[1] == GravityBloc:
                            bloc = GravityBloc(pos)
                            self.list_gravity_bloc.append((bloc))
                        else:
                            bloc = None
                    if bloc:
                        self.level_elements.append(bloc)

    def update(self, dt):
        if self.background:
            x = 0
            while x < self.screen.get_size()[0]:
                self.screen.blit(self.background, (x, 0))
                x += self.background.get_size()[0]

        for b in self.list_gravity_bloc:
            b.display(self.screen)
            b.move(dt)

        for elem in self.level_elements:
            elem.display(self.screen)

        self.player.display(self.screen)
        self.player.move(dt)

        keys = pg.key.get_pressed()

        if keys[pg.K_SPACE]:
            self.player.jump()
        if keys[pg.K_d] or keys[pg.K_RIGHT]:
            self.player.goRight(dt)
        if keys[pg.K_q] or keys[pg.K_LEFT]:
            self.player.goLeft(dt)

        pg.draw.rect(self.screen, (0, 0, 0), (self.x_center, self.y_center, self.grid_width, self.grid_height), 4)
