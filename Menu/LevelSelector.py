import json
import os


class LevelSelector:

    def __init__(self):
        self.levels = []
        basepath = os.path.dirname(os.path.realpath(__file__)) + "/../Levels/"
        for entry in os.listdir(basepath):
            if os.path.isfile(os.path.join(basepath, entry)):
                if ".json" in entry:
                    with open(os.path.join(basepath, entry), "r") as f:
                        json_data = json.load(f)
                        json_data['grid'] = None
                        self.levels.append(json_data)

    def update(self, screen, dt, events):
        space_witdh = 100


