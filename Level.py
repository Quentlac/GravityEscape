import json
import os

from Bloc.NoKillBloc import NoKillBloc
from Camera import Camera
from Item.BulletItem import BulletItem
from Item.GravityItem import GravityItem
from Player import Player
from view.Materials import Materials
from Bloc.StaticBloc import StaticBloc
from Bloc.NoHitBoxBloc import NoHitBoxBloc
from Bloc.GravityBloc import GravityBloc
from Camera import *
import pygame as pg


class Level:
    default_size = (50, 50)
    list_gravity_bloc = []
    bullets = []

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
        # Add border to level
        top = GravityItem(((self.grid_width / 2) - self.default_size[0] / 2, -200), (self.grid_width, 50))
        right = GravityItem((self.grid_width, (self.grid_height/2) - 200), (50, self.grid_height + 50))
        bottom = GravityItem(((self.grid_width / 2) - self.default_size[0] / 2, self.grid_height - 200), (self.grid_width, 50))
        left = GravityItem((-50, (self.grid_height/2) - 200), (50, self.grid_height + 50))
        #self.level_elements.extend([top, bottom, left, right])

        self.player = Player((0, 0))
        self.camera = Camera(self.player, screen.get_size())
        self.respawn()

    def load_grid(self):
        # Draw grid
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                if self.grid[x][y] != 0:
                    material = Materials.get_material(self.grid[x][y])
                    pos = (self.x_center + y * self.default_size[0], self.y_center + x * self.default_size[1])
                    if type(material) != tuple:
                        bloc = StaticBloc(pos, self.default_size, material)
                    else:

                        if material[1] == NoHitBoxBloc:
                            bloc = NoHitBoxBloc(pos, self.default_size, material[0])
                        elif material[1] == NoKillBloc:
                            bloc = NoKillBloc(pos, self.default_size, material[0])
                        elif material[1] == GravityBloc:
                            bloc = GravityBloc(pos)
                            self.list_gravity_bloc.append(bloc)
                        else:
                            bloc = None
                    if bloc:
                        self.level_elements.append(bloc)

    def shoot(self, x, y):
        dx = x - self.player.getPosX()
        dy = y - self.player.getPosY()

        visee = pg.Vector2(dx, dy)
        visee = visee.normalize()

        self.bullets.append(BulletItem((self.player.getPosX(), self.player.getPosY()), (visee.x, visee.y)))

    def respawn(self):
        self.player.setPosition(200, 200)

    def update(self, dt, events):
        if self.background:
            x = 0
            while x < self.screen.get_size()[0]:
                self.screen.blit(self.background, (x, 0))
                x += self.background.get_size()[0]
        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN:
                posX, posY = pg.mouse.get_pos()
                offset_x, offset_y = self.camera.getOffset()
                self.shoot(-offset_x + posX, -offset_y + posY)

        for b in self.list_gravity_bloc:
            b.move(dt)

        for elem in self.level_elements:
            elem.display(self.screen, self.camera)

        for b in self.bullets:
            b.display(self.screen, self.camera)
            b.move(dt)

            if not b.active:
                self.bullets.remove(b)

        self.player.display(self.screen, self.camera)
        self.player.move(dt)
        self.camera.move(dt)
        if self.player.is_dead():
            self.respawn()

        keys = pg.key.get_pressed()

        if keys[pg.K_SPACE] or keys[pg.K_UP]:
            self.player.jump(dt)
        if keys[pg.K_d] or keys[pg.K_RIGHT]:
            self.player.goRight(dt)
        if keys[pg.K_q] or keys[pg.K_LEFT]:
            self.player.goLeft(dt)
