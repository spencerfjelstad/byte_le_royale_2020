from game.common.stats import GameStats
from game.common.city import City
from game.common.disasters import LastingDisaster
from game.common.sensor import Sensor
from game.controllers.controller import Controller
from game.config import *
from game.utils.helpers import enum_iter

import math


class EffortController(Controller):
    def __init__(self):
        super().__init__()

    def handle_actions(self, player):
        if self.controllers is None:
            raise Exception("Effort controller currently requires importing other controllers first.")

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
                self.disaster_controller.reduce_disaster(player, act, amount)
            elif isinstance(act, Sensor):
                self.sensor_controller.upgrade_sensor(player, act, amount)
            elif act in enum_iter(ActionType):
                # TODO: Implement or remove from action.py
                raise NotImplementedError("Effort allocated towards ActionType not yet implemented.")
            else:
                raise ValueError(f"Player {player} allocated amount {amount} towards illegal target {act}. "
                                 "Validation should have prevented this.")
