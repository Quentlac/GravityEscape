import pygame as pg
import os
from Bloc.NoHitBoxBloc import NoHitBoxBloc
from Bloc.GravityBloc import GravityBloc
from Bloc.NoKillBloc import NoKillBloc
class Materials:
    directory = os.path.dirname(os.path.realpath(__file__)) + "/blocks"
    materials = {
        1: pg.image.load(f"{directory}/block-cactus.png"),
        2: pg.image.load(f"{directory}/block-dirt.png"),
        3: pg.image.load(f"{directory}/block-dirtsnow.png"),
        4: pg.image.load(f"{directory}/block-futuristic-lightning.png"),
        5: pg.image.load(f"{directory}/block-grass.png"),
        6: pg.image.load(f"{directory}/block-ice.png"),
        7: pg.image.load(f"{directory}/block-leaves.png"),
        8: pg.image.load(f"{directory}/block-logs.png"),
        9: pg.image.load(f"{directory}/block-metal.png"),
        10: pg.image.load(f"{directory}/block-purple-wire.png"),
        11: pg.image.load(f"{directory}/block-purple-wire-hori.png"),
        12: pg.image.load(f"{directory}/block-rebound.png"),
        13: pg.image.load(f"{directory}/block-red-wire.png"),
        14: pg.image.load(f"{directory}/block-red-wire-hori.png"),
        15: (pg.image.load(f"{directory}/block-redflower.png"), NoHitBoxBloc),
        16: pg.image.load(f"{directory}/block-sand.png"),
        17: pg.image.load(f"{directory}/block-snow.png"),
        18: pg.image.load(f"{directory}/block-stone.png"),
        19: pg.image.load(f"{directory}/block-stonesnow.png"),
        20: pg.image.load(f"{directory}/block-water.png"),
        21: (pg.image.load(f"{directory}/block-yellowflower.png"), NoHitBoxBloc),
        22: (pg.image.load(f"{directory}/block-gravity.png"), GravityBloc),
        23: (pg.image.load(f"{directory}/block-gravity-blue.png"), GravityBloc),
        24: (pg.image.load(f"{directory}/block-gravity-empty.png"), NoKillBloc),


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
