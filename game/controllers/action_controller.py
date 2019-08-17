from game.common.stats import GameStats
from game.controllers.controller import Controller
from game.config import *

import math

class ActionController(Controller):
    def __init__(self):
        super().__init__()

    def handle_actions(self, player):
        # handle advanced verification of allocation list
        player.city.remaining_man_power = player.city.population
        allocations = dict() # condensed duplicate entries

        for allocation in player.action._allocation_list:
            act, amount = allocation

            # Do any additional, server side action validation here
            if player.city.remaining_man_power == 0:
                print("All man power exhausted. Skipping allocation: {}".format(allocation))
                continue

            # Reduce requested amount to maximum remaining
            if amount > player.city.remaining_man_power:
                print("Too much man power requested for action. Reducing to remaining man power.")
                amount = player.city.remaining_man_power

            # Reduce man power
            player.city.remaining_man_power -= amount

            # Save action
            allocations[act] = amount + allocations.get(act, 0)

        for act, amount in allocations.items():
            # TODO: Handle control of efforts here (upgrade sensor, reduce disaster, etc.)
            #if isinstance(act, Sensor):
            #   pass
            #elif isinstance(act, Disaster):
            #   pass
            pass
