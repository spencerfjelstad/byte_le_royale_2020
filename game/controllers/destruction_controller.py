from game.common.enums import *
from game.controllers.controller import Controller
from game.controllers.fun_stat_controller import FunStatController
from game.config import *
from game.utils.helpers import clamp


class DestructionController(Controller):
    def __init__(self):
        super().__init__()

        self.fun_stat_controller = FunStatController.get_instance()

    def handle_actions(self, player):
        # Loop through each disaster
        city = player.city
        for disaster in player.disasters:
            # Skip the disaster if it's dead
            if disaster.status == DisasterStatus.dead:
                continue

            # Apply the effects of the disaster on the city, don't go below 0
            previous_structure = city.structure
            previous_population = city.population

            city.structure = clamp(city.structure - disaster.structure_damage, min_value=0, max_value=city.max_structure)
            city.population = clamp(city.population - disaster.population_damage, min_value=0, max_value=city.structure)

            # Fun stat controller intervention
            self.fun_stat_controller.total_population_damage += previous_population - city.population
            self.fun_stat_controller.total_structure_damage += previous_structure - city.structure
