import json
import os

import pygame.draw

from Bloc.GravityBlocStoppable import GravityBlocStoppable
from Bloc.EndBloc import EndBloc
from Bloc.InvertGravityBloc import InvertGravityBloc
from Bloc.NoKillBloc import NoKillBloc
from Bloc.SpawnBloc import SpawnBloc
from Editor.Editor import Editor
from Item.BulletItem import BulletItem
from Item.GravityItem import GravityItem
from LoreDisplayer import LoreDisplayer
from Menu.Pause import Pause
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


    def __init__(self, name, screen, callback):
        self.name = name
        self.level_elements = []
        self.level_name = name
        self.screen = screen
        self.game_end = callback
        self.is_pause = False
        self.pause = Pause(self.end_pause, self.respawn, self.game_end)
        self.is_in_text = True
        pygame.mixer.music.stop()

        self.is_music = None
        self.lore = None
        self.background = None
        self.grid = None
        self.size = None
        self.json_data = None
        self.text = None
        self.load_json()

        # Get center of the screen
        self.grid_width = self.size[1] * self.default_size[0]
        self.grid_height = self.size[0] * self.default_size[1]
        self.x_center = (screen.get_size()[0] - self.grid_width) // 2
        self.y_center = (screen.get_size()[1] - self.grid_height) // 2
        self.spawn = (0, 0)
        self.load_grid()

        self.player = Player(self.spawn)
        self.camera = Camera(self.player, screen.get_size())
        self.player.setPosition(self.spawn[0], self.spawn[1])
        self.init_music()

        self.is_in_editor = False
        self.editor = None

        self.font = pygame.font.Font("view/font/LuckiestGuy-Regular.ttf", 15)

    def load_json(self):
        try:
            # Loading level file
            with open(os.path.dirname(os.path.realpath(__file__)) + "/Levels/" + self.name, "r") as f:
                self.json_data = json.load(f)

            self.size = self.json_data["size"]
            self.grid = self.json_data["grid"]

            self.background = None
            if self.json_data.get("background", False):
                try:
                    bg = pg.image.load(
                        f"{os.path.dirname(os.path.realpath(__file__))}/view/backgrounds/{self.json_data['background']}")
                    new_width = (bg.get_size()[0] * self.screen.get_size()[1]) // bg.get_size()[0]
                    bg = pg.transform.scale(bg, (self.screen.get_size()[0], self.screen.get_size()[1]))

                    self.background = bg
                except FileNotFoundError as e:
                    print("Background not found")
                    self.background = None

            if self.json_data.get("lore", False):
                self.lore = LoreDisplayer(self.json_data["lore"], self.end_lore)
            else:
                self.is_in_text = False

            if self.json_data.get("music", False):
                self.is_music = True
                pygame.mixer.music.load(os.path.dirname(os.path.realpath(__file__)) + "/ressources/" + self.json_data["music"])
            else:
                self.is_music = False

            if self.json_data.get("text", False):
                self.text = self.json_data["text"]
        except json.JSONDecodeError:
            print("Error decoding level json file")
        except KeyError as e:
            print("Missing key in level file: ", e)
    def end_lore(self):
        self.is_in_text = False

    def init_music(self):
        if self.is_music:
            pygame.mixer.music.stop()
            pygame.mixer.music.set_volume(.08)
            pygame.mixer.music.play(-1)
    def end_pause(self):
        self.is_pause = False

    def endcallback(self):
        self.game_end()

    def load_grid(self):
        self.bullets = []
        self.level_elements = []
        GravityBloc.items = []
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
                        elif material[1] == GravityBloc or material[1] == InvertGravityBloc or material[1] == GravityBlocStoppable:
                            bloc = material[1](pos)
                            self.list_gravity_bloc.append(bloc)
                        elif material[1] == EndBloc:
                            bloc = material[1](pos, self.endcallback, material[0])
                        elif material[1] == SpawnBloc:
                            bloc = material[1](pos, material[0])
                            self.spawn = pos
                        else:
                            bloc = None
                    if bloc:
                        self.level_elements.append(bloc)

    def shoot(self, x, y, button):
        dx = x - self.player.getPosX()
        dy = y - self.player.getPosY()

        visee = pg.Vector2(dx, dy)
        visee = visee.normalize()

        self.bullets.append(BulletItem((self.player.getPosX(), self.player.getPosY()), (visee.x, visee.y), button))

    def respawn(self):
        self.player.setPosition(self.spawn[0], self.spawn[1])
        GravityItem.items = []
        self.load_grid()
        self.end_pause()
        self.init_music()

    def open_editor(self):
        if self.is_music:
            pygame.mixer.music.stop()
        self.is_in_editor = True
        self.editor = Editor(self.screen, self.name, self.close_editor)

    def close_editor(self):
        self.is_in_editor = False
        self.load_json()
        self.load_grid()
        self.editor = None
        self.init_music()

    def setcheckpoint(self, pos):
        self.spawn = pos

    def draw_text(self, text, font, x, y):
        textObj = font.render(text, 1, "white")
        textrect = textObj.get_rect()
        textrect.center = (x, y)
        self.screen.blit(textObj, textrect)

    def update(self, dt, events):
        if self.is_in_text:
            self.lore.update(self.screen, dt, events)
            return

        if self.is_in_editor:
            self.editor.update(events, dt)
            return

        if self.background:
            offset_x, offset_y = self.camera.getParralaxOffset(0.5)
            bgX = (offset_x % self.background.get_size()[0] - self.screen.get_size()[0])
            bgY = offset_y + 50
            self.screen.blit(self.background, (bgX, bgY))
            self.screen.blit(self.background, (bgX + self.background.get_size()[0], bgY))

        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN:
                posX, posY = pg.mouse.get_pos()
                offset_x, offset_y = self.camera.getOffset()
                self.shoot(-offset_x + posX, -offset_y + posY, event.button)
            if event.type == pg.KEYUP:
                if event.key == pg.K_ESCAPE:
                    self.is_pause = not self.is_pause
                if event.key == pg.K_j:
                    self.open_editor()

        for b in self.list_gravity_bloc:
            b.move(dt)

        for elem in self.level_elements:
            elem.display(self.screen, self.camera)

        # Hover gravity bloc
        posX, posY = pg.mouse.get_pos()
        offset_x, offset_y = self.camera.getOffset()

        for b in GravityBloc.getItems():
            if b.testCollision(-offset_x + posX, -offset_y + posY):
                x = offset_x + b.getPosX()
                y = offset_y + b.getPosY()
                s = pygame.surface.Surface((b.getWidth(), b.getHeight()), pygame.SRCALPHA)
                s.fill((0, 0, 0, 0))
                pygame.draw.rect(s, (0, 0, 0, 50), (1, 1, b.getWidth() - 2, b.getHeight() - 2), border_radius=3)
                self.screen.blit(s, (x - b.getWidth() / 2, y - b.getHeight() / 2))

        if self.text is not None:
            for (x, y), text in self.text:
                (cx, cy) = self.camera.getOffset()
                (px, py) = (self.x_center + x * self.default_size[0], self.y_center + y * self.default_size[1])
                self.draw_text(text, self.font, px + cx, py + cy)

        for b in self.bullets:
            b.display(self.screen, self.camera)
            b.move(dt)

            if not b.active:
                self.bullets.remove(b)

        self.player.display(self.screen, self.camera)
        self.player.move(dt)
        self.camera.move(dt)
        if self.player.is_dead(self.grid_height):
            self.respawn()

        keys = pg.key.get_pressed()

        if keys[pg.K_SPACE] or keys[pg.K_UP]:
            self.player.jump(dt)
        if keys[pg.K_d] or keys[pg.K_RIGHT]:
            self.player.goRight(dt)
        if keys[pg.K_q] or keys[pg.K_LEFT]:
            self.player.goLeft(dt)

        if self.is_pause:
            self.pause.update(self.screen, events)
