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

    def upgrade_sensor(self, player, sensor, number):
        # Validate input
        if number < 0:
            self.print("Negative effort not accepted.")
            return
        if not isinstance(player, Player):
            self.print("The player argument is not a Player object.")
            return
        if not isinstance(sensor, Sensor):
            self.print("The sensor argument is not a Sensor object.")
            return
        if sensor not in player.city.sensors.values():
            self.print("Sensor is not a part of the city.")
            self.print("Sensor: {}".format(sensor))
            for sens in player.city.sensors:
                self.print("City sensor: {}".format(sens))
            return
        if sensor.sensor_level == SensorLevel.level_three:
            self.print("Sensor level is already maxed.")
            return

        current_level = sensor.sensor_level
        if current_level == SensorLevel.level_zero:
            next_level = SensorLevel.level_one
        elif current_level == SensorLevel.level_one:
            next_level = SensorLevel.level_two
        elif current_level == SensorLevel.level_two:
            next_level = SensorLevel.level_three
        else:
            self.print("sensor's sensor_level value is invalid.")
            return

        sensor.sensor_effort_remaining -= number
        # if limit maxed, begin upgrade
        if sensor.sensor_effort_remaining <= 0:
            self.print("Sensor level {} reached!".format(next_level))
            # apply changes
            left_over = sensor.sensor_effort_remaining * -1  # reverse, because effort allocation must be positive
            sensor.sensor_effort_remaining = GameStats.sensor_effort[next_level]
            sensor.sensor_level = next_level

            # with left over effort, attempt upgrade again
            self.upgrade_sensor(player, sensor, left_over)
