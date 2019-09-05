import math
import random

from game.common.enums import *
from game.common.stats import GameStats
from game.common.player import Player
from game.common.sensor import Sensor
from game.controllers.controller import Controller
from game.utils.helpers import *


class SensorController(Controller):

    def __init__(self):
        super().__init__()
        self.turn_ranges = dict()
        self.debug = True

    def handle_actions(self, player):
        pass

    def calculate_turn_ranges(self, turn, odds):
        if turn in self.turn_ranges:
            raise ValueError("This turn has already been calculated.")

        adjusted_weights = {}

        for disaster in enum_iter(DisasterType):
            sensor_odds = {}

            disaster_odds = math.floor(odds[disaster] * 100)

            for sensor_level in enum_iter(SensorLevel):

                for level in enum_iter(SensorLevel):
                    if sensor_level == level:
                        range = GameStats.sensor_ranges[level]
                        break
                else:
                    raise Exception(
                        "Sensor level out of bounds. Should be SensorLevel.level_zero <= x <= SensorLevel.level_three.")

                range = math.floor(range / 2)
                min_chance = disaster_odds - range
                max_chance = disaster_odds + range

                captured_odds = random.randrange(min_chance, max_chance + 1)

                # handle results appearing below 0
                captured_odds = abs(captured_odds)

                # handle results appearing above 100
                if captured_odds >= 100:
                    captured_odds = 200 - captured_odds  # odds of 110 would become 90 (100 - 10 or 200 - 110)

                sensor_odds[sensor_level] = captured_odds / 100

            adjusted_weights[disaster] = sensor_odds

        self.turn_ranges[turn] = adjusted_weights
