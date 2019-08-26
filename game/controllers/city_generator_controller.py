from game.common.enums import *
from game.controllers.controller import Controller
from game.config import *


class CityGeneratorController(Controller):
    def __init__(self):
        super().__init__()

    def handle_actions(self, player, city_type):
        if city_type is CityType.none:
            pass
        elif city_type is CityType.healthy:
            player.city.population += 25
        elif city_type is CityType.sturdy:
            player.city.structure += 25
        elif city_type is CityType.invested:
            # bump city sensors up a level
            pass
