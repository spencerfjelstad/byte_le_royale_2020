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
            SensorType.fire_alarm: DecreeType.anti_fire_bears,
            SensorType.rock_on_a_rope: DecreeType.paperweights,
            SensorType.coast_guard: DecreeType.hound_news,
            SensorType.seismograph: DecreeType.moon_shoes,
            SensorType.scp_foundation: DecreeType.away_spray,
            SensorType.satellite_dish: DecreeType.giant_fly_swatter
        }

    def team_name(self):
        return "Bobs the Builders"

    def city_name(self):
        return "Under_Constructionopolis"

    def city_type(self):
        return CityType.none  # still dunno what this is

    # This is where your AI will decide what to do
    def take_turn(self, actions, city, disasters):

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
        building_types = enum_iter(BuildingType)
        sensor_types = enum_iter(SensorType)

        num_of_buildings = len(building_types)
        num_of_cities = 1
        num_of_sensors = len(sensor_types)
        total_construction_projects = num_of_buildings + num_of_cities + num_of_sensors

        # work work
        for building_type in building_types:
            actions.add_effort(city.buildings[building_type], city.population/total_construction_projects)

        actions.add_effort(city, city.population / total_construction_projects)

        for sensor_type in sensor_types:
            actions.add_effort(city.sensors[sensor_type], city.population / total_construction_projects)


