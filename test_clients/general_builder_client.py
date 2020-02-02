from game.client.user_client import UserClient
from game.common.enums import *


# from game.utils.helpers import enum_iter
# when certain imports are illegal, ctrl+c & ctrl+v is your best friend...
def enum_iter(enum_class):
    """
    Creates a list of all enum elements of a given enum class (including none or default values)
    :param enum_class: Enum class to retrieve all possibilities from
    :return: list containing all enum of the given type
    """
    return [enum_class.__dict__[key] for key in enum_class.__dict__ if not key.startswith("__")]


class Client(UserClient):
    # Variables and info you want to save between turns go here
    def __init__(self):
        super().__init__()
        self.SENSOR_DECREE_MAPPINGS = {
            SensorType.fire: DecreeType.anti_fire_dogs,
            SensorType.tornado: DecreeType.paperweights,
            SensorType.blizzard: DecreeType.snow_shovels,
            SensorType.earthquake: DecreeType.rubber_boots,
            SensorType.monster: DecreeType.fishing_hook,
            SensorType.ufo: DecreeType.cheese
        }
        self.turn = 0

    def team_name(self):
        return "Bobs the Builders"

    def city_name(self):
        return "Under_Constructionopolis"

    def city_type(self):
        return CityType.none  # still dunno what this is

    # This is where your AI will decide what to do
    def take_turn(self, turn, actions, city, disasters):
        self.turn += 1

        # Set decree
        highest = -1
        highest_sensor = None
        for sensor in city.sensors.values():
            if sensor.sensor_results > highest:
                highest = sensor.sensor_results
                highest_sensor = sensor

        corresponding_decree = self.SENSOR_DECREE_MAPPINGS[highest_sensor.sensor_type]
        actions.set_decree(corresponding_decree)

        # planning phase

        lasting_disasters = [disaster for disaster in disasters if disaster.type in [DisasterType.fire, DisasterType.monster, DisasterType.blizzard]]
        total_construction_projects = 0
        for building in city.buildings.values():
            if building.level != BuildingLevel.level_three:
                total_construction_projects += 1

        for sensor in city.sensors.values():
            if sensor.level != SensorLevel.level_three:
                total_construction_projects += 1

        if city.level != CityLevel.level_two:
            total_construction_projects += 1

        # Actions
        if self.turn < 5:
            actions.add_effort(ActionType.repair_structure, city.population)
        elif self.turn < 10:
            actions.add_effort(ActionType.regain_population, city.population)
        elif city.structure < (city.max_structure / 2):
            actions.add_effort(ActionType.repair_structure, city.population)
        elif city.population < (city.structure / 2):
            actions.add_effort(ActionType.regain_population, city.population)
        elif lasting_disasters:
            for disaster in lasting_disasters:
                actions.add_effort(disaster, city.population / len(lasting_disasters))
        elif total_construction_projects > 0:
            get_gold = (city.gold < city.population)
            if get_gold:
                actions.add_effort(ActionType.accumulate_wealth, city.population / 2)
            for building in city.buildings.values():
                if building.level != BuildingLevel.level_three:
                    actions.add_effort(building, city.population / ((2 if get_gold else 1) * total_construction_projects))

            for sensor in city.sensors.values():
                if sensor.level != SensorLevel.level_three:
                    actions.add_effort(sensor, city.population / ((2 if get_gold else 1) * total_construction_projects))

            if city.level != CityLevel.level_two:
                actions.add_effort(city, city.population / ((2 if get_gold else 1) * total_construction_projects))
        else:
            actions.add_effort(ActionType.repair_structure, city.population / 2)
            actions.add_effort(ActionType.regain_population, city.population / 2)


