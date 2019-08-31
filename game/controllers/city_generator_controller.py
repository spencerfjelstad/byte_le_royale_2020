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
            player.city.population += 50
        elif city_type is CityType.sturdy:
            player.city.structure += 50
        elif city_type is CityType.invested:
            player.city.resources += 25
            player.city.gold += 25
