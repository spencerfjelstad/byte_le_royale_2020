from game.common.enums import *
from game.common.stats import *

class City:
    def __init__(self):
        self.city_name = "City"
        self.health = GameStats.city_health
        self.population = GameStats.city_population
        self.gold = GameStats.city_gold
        self.location = CityLocation.default
        self.sensors = {
            SensorType.fire_alarm : SensorLevel.level_zero,
            SensorType.rock_on_a_rope : SensorLevel.level_zero,
            SensorType.coast_guard : SensorLevel.level_zero,
            SensorType.seismograph : SensorLevel.level_zero,
            SensorType.scp_foundation : SensorLevel.level_zero,
            SensorType.satellite_dish : SensorLevel.level_zero
        }
