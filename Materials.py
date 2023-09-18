import pygame as pg
import os


class Materials:
    directory = os.path.dirname(os.path.realpath(__file__)) + "/textures"
    materials = {
        1: pg.image.load(f"{directory}/dirt_snow.png")
    }

    @staticmethod
    def get_material(id_img):
        try:
            return Materials.materials[id_img]
        except KeyError:
            return None

    @staticmethod
    def as_list():
        return list(Materials.materials.items())
