import json
import os
import sys

from game.common.enums import *
from game.common import *


class GameLogParser:
    def __init__(self, log_dir):
        if not os.path.exists(log_dir):
            raise Exception(f"Invalid log directory: {log_dir}")

        self.log_dir = log_dir

        self.tick = 0
        self.turns = []

        self.load_turns()

    # Load all turns into memory
    def load_turns(self):
        for file in os.listdir(self.log_dir):
            if 'turn' in file:
                with open(self.log_dir + file) as f:
                    self.turns.append(json.load(f))

    # Interface for retrieving game logs
    def get_turn(self):
        if len(self.turns) > 0:
            self.tick += 1
            return self.turns.pop(0)
        else:
            return None
