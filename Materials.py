import pygame as pg


class Materials:
    directory = "./textures"
    materials = {
        1: pg.image.load(f"{directory}/dirt_snow.png")
    }

    @staticmethod
    def get_material(id_img):
        try:
            return Materials.materials[id_img]
        except KeyError:
            return None
