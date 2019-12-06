import json
import os
import sys

from game.common.enums import *
from game.common.player import Player
from game.common.disasters import *
from game.common.action import Action


class GameLogParser:
    def __init__(self, log_dir):
        if not os.path.exists(log_dir):
            raise Exception(f"Invalid log directory: {log_dir}")

        self.log_dir = log_dir

        self.turns = []

        self.load_turns()

    # Load all turns into memory
    def load_turns(self):
        files = sorted(os.listdir(self.log_dir))

        for file in files:
            # skip "other" log files
            if 'turn' not in file:
                continue
            with open(self.log_dir + file) as f:
                self.turns.append(json.load(f))

    # Interface for retrieving game logs
    def get_turn(self, turn):
        if 1 <= turn <= len(self.turns):
            info = self.turns[turn-1]

            # if statements provide for reviewing logs that have already been deserialized
            if 'player' not in info:
                info['player'] = self.deserialize(info['player'])
            return info
        else:
            return None

    # Deserialize lists of things given to it
    def deserialize(self, data):
        objs = []

        for serialized_obj in data:
            obj_type = serialized_obj['object_type']

            if obj_type == ObjectType.player:
                obj = Player()
                obj.from_json(serialized_obj)
                objs.append(obj)
            elif obj_type == ObjectType.disaster:
                dis_type = serialized_obj['type']
                obj = None
                if dis_type == DisasterType.earthquake:
                    obj = Earthquake()
                elif dis_type == DisasterType.fire:
                    obj = Fire()
                elif dis_type == DisasterType.hurricane:
                    obj = Hurricane()
                elif dis_type == DisasterType.monster:
                    obj = Monster()
                elif dis_type == DisasterType.tornado:
                    obj = Tornado()
                elif dis_type == DisasterType.ufo:
                    obj = Ufo()
                obj.from_json(serialized_obj)
                objs.append(obj)
            elif obj_type == ObjectType.action:
                obj = Action()
                obj.from_json(serialized_obj)
                objs.append(obj)
            else:
                print(obj_type)

        return objs
