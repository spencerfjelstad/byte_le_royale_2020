from game.common.game_object import GameObject
from game.common.enums import *
from game.common.building import Building
from game.common.sensor import Sensor
from game.common.stats import GameStats
from game.utils.helpers import enum_iter


class City(GameObject):
    def __init__(self):
        super().__init__()
        self.city_name = "City"
        self.city_type = CityType.none
        self.object_type = ObjectType.city
        self.structure = GameStats.city_structure
        self.max_structure = GameStats.city_max_structure[CityLevel.level_zero]
        self.population = GameStats.city_population
        self.gold = GameStats.city_gold
        self.sensors = dict()
        for sens_type in enum_iter(SensorType):
            sens = Sensor()
            sens.sensor_type = sens_type
            self.sensors[sens_type] = sens

        self.buildings = dict()
        for building_type in enum_iter(BuildingType):
            building = Building(building_type)
            self.buildings[building_type] = building

        self.level = CityLevel.level_zero
        self.effort_remaining = GameStats.city_upgrade_cost[CityLevel.level_one]

    def to_json(self):
        data = super().to_json()

        data['city_name'] = self.city_name
        data['city_type'] = self.city_type
        data['object_type'] = self.object_type
        data['structure'] = self.structure
        data['max_structure'] = self.max_structure
        data['population'] = self.population
        data['gold'] = self.gold
        data['sensors'] = {sensor_type: sensor.to_json() for sensor_type, sensor in self.sensors.items()}
        data['buildings'] = {building_type: building.to_json() for building_type, building in self.buildings.items()}
        data['level'] = self.level
        data['effort_remaining'] = self.effort_remaining

        return data
    
    def from_json(self, data):
        super().from_json(data)
        self.city_name = data['city_name']
        self.city_type = data['city_type']
        self.object_type = data['object_type']
        self.structure = data['structure']
        self.max_structure = data['max_structure']
        self.population = data['population']
        self.gold = data['gold']

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

        self.level = data['level']
        self.effort_remaining = data['effort_remaining']

    def __str__(self):
        p = f"""City name: {self.city_name}
            Structure: {self.structure}
            Population: {self.population}
            Gold: {self.gold}
            Level: {self.level}
            Object Type: {self.object_type}
            """

        return p
