import math
import random

from game.common.stats import GameStats
from game.common.enums import *
from game.controllers.controller import Controller
from game.utils.helpers import *


class SensorController(Controller):

    def __init__(self):
        super().__init__()
        self.turn_ranges = dict()

    def handle_actions(self, world):
        pass

    def calculate_turn_ranges(self, turn, odds):
        if turn in self.turn_ranges:
            raise ValueError("This turn has already been calculated.")

        adjusted_weights = {}

        for disaster in enum_iter(DisasterType):
            sensor_odds = {}

            disaster_odds = math.floor( odds[disaster] * 100 )

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

                # Modify chance so it doesn't provide us odds out of bounds
                if min_chance < 0:
                    min_chance = 0
                if max_chance > 100:
                    max_chance = 100

                sensor_odds[sensor_level] = random.randrange(min_chance, max_chance + 1) / 100

            adjusted_weights[disaster] = sensor_odds

        self.turn_ranges[turn] = adjusted_weights
