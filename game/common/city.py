from game.common.enums import *
from game.common.stats import *


class City:
    def __init__(self):
        self.city_name = "City"
        self.structure = GameStats.city_structure
        self.population = GameStats.city_population
        self.gold = GameStats.city_gold
        self.resources = GameStats.resources
        self.location = CityLocation.default
        self.sensors = {
            SensorType.fire_alarm: SensorLevel.level_zero,
            SensorType.rock_on_a_rope: SensorLevel.level_zero,
            SensorType.coast_guard: SensorLevel.level_zero,
            SensorType.seismograph: SensorLevel.level_zero,
            SensorType.scp_foundation: SensorLevel.level_zero,
            SensorType.satellite_dish: SensorLevel.level_zero
        }
        self.sensor_results = dict() # TODO: move this into sensor object plz && thx
    
    def to_json(self):
        data = dict()

        data['city_name'] = self.city_name
        data['structure'] = self.structure
        data['population'] = self.population
        data['gold'] = self.gold
        data['resources'] = self.resources
        data['location'] = self.location
        data['sensors'] = self.sensors
        data['sensor_results'] = self.sensor_results

        return data
    
    def from_json(self, data):
        self.city_name = data['city_name']
        self.structure = data['structure']
        self.population = data['population']
        self.gold = data['gold']
        self.resources = data['resources']
        self.location = data['location']
        self.sensors = data['sensors']
        self.sensor_results = data['sensor_results']

