from game.client.user_client import UserClient
from game.common.enums import *


class Client(UserClient):
    # Variables and info you want to save between turns go here
    def __init__(self):
        super().__init__()

    def team_name(self):
        return "Scrimmy Bingus"

    def city_name(self):
        return "Crungy Spingus"

    def city_type(self):
        return CityType.invested

    # This is where your AI will decide what to do
    def take_turn(self, turn, actions, city, disasters):
        # Set all the disasters to 0 damage
        for disaster in disasters:
            disaster.population_damage = 0
            disaster.structure_damage = 0

        buildings = city.buildings.values()
        sensors = city.sensors.values()

        # Try to level up buildings, cities, and sensors
        for building in buildings:
            building.level = BuildingLevel.level_three

        city.level = CityLevel.level_two

        for sensor in sensors:
            sensor.level = SensorLevel.level_three

        # Try to get rid of all the disasters
        disasters.clear()

        # Try to break necessary functionality
        city.object_type = None
        city.sensors = None
        city.buildings = None
