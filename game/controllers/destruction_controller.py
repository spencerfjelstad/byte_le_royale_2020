from game.common.enums import *
from game.controllers.controller import Controller
from game.config import *


class DestructionController(Controller):
    def __init__(self):
        super().__init__()

    def handle_actions(self, player):
        # Loop through each disaster
        city = player.city
        for disaster in player.disasters:
            # Skip the disaster if it's dead
            if disaster.status == DisasterStatus.dead:
                continue

            # Apply the effects of the disaster on the city, don't go below 0
            city.structure = max(city.structure - disaster.structure_damage, 0)
            city.population = max(city.population - disaster.population_damage, 0)
