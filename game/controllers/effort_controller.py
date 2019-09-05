from game.common.stats import GameStats
from game.common.city import City
from game.common.disasters import LastingDisaster
from game.common.player import Player
from game.common.sensor import Sensor
from game.controllers.controller import Controller
from game.config import *
from game.utils.helpers import enum_iter

import math


class EffortController(Controller):
    def __init__(self):
        super().__init__()

    def handle_actions(self, player):
        # handle advanced verification of allocation list
        player.city.remaining_man_power = player.city.population
        allocations = dict()  # condensed duplicate entries

        for allocation in player.action._allocation_list:
            act, amount = allocation

            # Do any additional, server side action validation here

            # Skip action (no man power left)
            if player.city.remaining_man_power == 0:
                self.print("All man power exhausted. Skipping allocation: {}".format(allocation))
                continue

            # Reduce requested amount to maximum remaining
            if amount > player.city.remaining_man_power:
                self.print("Too much man power requested for action. Reducing to remaining man power.")
                amount = player.city.remaining_man_power

            # Reduce man power
            player.city.remaining_man_power -= amount

            # Save action
            if act not in allocations:
                allocations[act] = 0
            allocations[act] += amount

        # Handle control of efforts here
        for act, amount in allocations.items():
            if isinstance(act, City):
                # TODO: Implement or remove from action.py
                raise NotImplementedError("Effort allocated towards city not yet implemented.")
            if isinstance(act, LastingDisaster):
                self.apply_disaster_effort(player, act, amount)
            elif isinstance(act, Sensor):
                self.apply_sensor_effort(player, act, amount)
            elif act in enum_iter(ActionType):
                # TODO: Implement or remove from action.py
                raise NotImplementedError("Effort allocated towards ActionType not yet implemented.")
            else:
                raise ValueError(f"Player {player} allocated amount {amount} towards illegal target {act}. "
                                 "Validation should have prevented this.")

    # Reduces disaster life when effort is applied
    def apply_disaster_effort(self, player, lasting_disaster, number):
        # Validate input
        if number < 0:
            self.print("Negative effort not accepted.")
            return
        if not isinstance(player, Player):
            self.print("The player argument is not a Player object.")
            return
        if not isinstance(lasting_disaster, LastingDisaster):
            self.print("The lasting_disaster argument is not a LastingDisaster object.")
            return
        if lasting_disaster.status != DisasterStatus.live:
            self.print("Disaster has already been stopped.")
            return

        lasting_disaster.reduce(number)

    # Upgrades sensors when effort is applied
    def apply_sensor_effort(self, player, sensor, number):
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
            # TODO: look at making this non-recursive
            self.upgrade_sensor(player, sensor, left_over)