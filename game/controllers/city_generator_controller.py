from game.common.enums import *
from game.common.stats import GameStats
from game.controllers.controller import Controller
from game.config import *


class CityGeneratorController(Controller):
    def __init__(self):
        super().__init__()

    def handle_actions(self, player, city_type):
        if city_type is CityType.none:
            pass
        elif city_type is CityType.healthy:
            # Start with population up to structure
            player.city.population = player.city.structure
        elif city_type is CityType.sturdy:
            # Start with structure up to max structure
            player.city.structure = player.city.max_structure
        elif city_type is CityType.invested:
            # Start with boosted gold
            player.city.gold += GameStats.city_type_invested_bonus
        elif city_type is CityType.pyrophobic:
            # Upgrade the fire sensors to level one
            fire_alarm = player.city.sensors[SensorType.fire]
            fire_alarm.level = SensorLevel.level_one
            fire_alarm.effort_remaining = GameStats.sensor_upgrade_cost[SensorLevel.level_two]
        elif city_type is CityType.popular:
            # Upgrade the population booster building to level one
            population_booster = player.city.buildings[BuildingType.billboard]
            population_booster.level = BuildingLevel.level_one
            population_booster.effort_remaining = GameStats.building_upgrade_cost[BuildingType.billboard][CityLevel.level_one]
        elif city_type is CityType.modern:
            # Upgrade the city to level one
            city = player.city
            city.level = CityLevel.level_one
            city.effort_remaining = GameStats.city_upgrade_cost[CityLevel.level_two]
