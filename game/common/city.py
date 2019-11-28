from game.common.enums import *
from game.common.building import Building
from game.common.sensor import Sensor
from game.common.stats import GameStats
from game.utils.helpers import enum_iter


class City:
    def __init__(self):
        self.city_name = "City"
        self.object_type = ObjectType.city
        self.structure = GameStats.city_structure
        self.max_structure = self.structure
        self.population = GameStats.city_population
        self.gold = GameStats.city_gold
        self.resources = GameStats.resources
        self.location = CityLocation.plains
        self.sensors = dict()
        for sens_type in enum_iter(SensorType):
            sens = Sensor()
            sens.sensor_type = sens_type
            self.sensors[sens_type] = sens

        self.buildings = dict()
        for building_type in enum_iter(BuildingType):
            building = Building(building_type)
            self.buildings[building_type] = building

        self.remaining_man_power = self.population
        self.level = CityLevel.level_zero
        self.effort_remaining = GameStats.city_upgrade_cost[CityLevel.level_one]

    def to_json(self):
        data = dict()

        data['city_name'] = self.city_name
        data['object_type'] = self.object_type
        data['structure'] = self.structure
        data['max_structure'] = self.max_structure
        data['population'] = self.population
        data['gold'] = self.gold
        data['resources'] = self.resources
        data['location'] = self.location
        data['sensors'] = {sensor_type: sensor.to_json() for sensor_type, sensor in self.sensors.items()}
        data['buildings'] = {building_type: building.to_json() for building_type, building in self.buildings.items()}
        data['remaining_man_power'] = self.remaining_man_power
        data['level'] = self.level
        data['effort_remaining'] = self.effort_remaining

        return data
    
    def from_json(self, data):
        self.city_name = data['city_name']
        self.object_type = data['object_type']
        self.structure = data['structure']
        self.max_structure = data['max_structure']
        self.population = data['population']
        self.gold = data['gold']
        self.resources = data['resources']
        self.location = data['location']

        self.sensors = dict()
        for sensor_type, sensor_data in data['sensors'].items():
            sensor = Sensor()
            sensor.from_json(sensor_data)
            self.sensors[sensor_type] = sensor
        self.buildings = dict()

        for building_type, building_data in data['buildings'].items():
            building = Building()
            building.from_json(building_data)
            self.buildings[building_type] = building

        self.remaining_man_power = data['remaining_man_power']
        self.level = data['level']
        self.effort_remaining = data['effort_remaining']

    def __str__(self):
        p = f"""City name: {self.city_name}
            Structure: {self.structure}
            Population: {self.population}
            Gold: {self.gold}
            Resources: {self.resources}
            Level: {self.level}
            """

        return p
