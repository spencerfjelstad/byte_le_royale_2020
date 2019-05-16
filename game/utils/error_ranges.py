import math
import random

from game.common.stats import GameStats
from game.common.enums import *
from game.utils.helpers import *

# provide_sensor_ranges
# @parameters
# odds : dict : the odds the disasters are occurring on a given turn
#
# @returns
# adjusted_weights : dict : a dictionary of dictionaries that provides the detected error by each sensor
def provide_sensor_ranges(odds):

    adjusted_weights = {}

    for disaster in enum_iter(DisasterType):
        sensor_odds = {}

        disaster_odds = odds[disaster]

        for sensor_level in enum_iter(SensorLevel):
            sensor_odds[ sensor_level ] = provide_sensor_range( disaster_odds, sensor_level )

        adjusted_weights[disaster] = sensor_odds

    return adjusted_weights

# provide_sensor_range
# @parameters
# chance : number : the odds of a single disaster is occurring on a turn
# range : SensorLevel : the level of the associated sensor of the disaster
#
# @returns
# adjusted_odds : number : random odds between 0 and 1 near the chance given the sensor
def provide_sensor_range(chance, sensor_level):
    chance = math.floor(chance*100)

    for level in enum_iter(SensorLevel):
        if sensor_level == level:
            range = GameStats.sensor_ranges[level]
            break
    else:
        raise Exception("Sensor level out of bounds. Should be SensorLevel.level_zero <= x <= SensorLevel.level_three.")

    range = math.floor(range / 2)
    min_chance = chance - range
    max_chance = chance + range

    # Modify chance so it doesn't provide us odds out of bounds
    if min_chance < 0:
        min_chance = 0
    if max_chance > 100:
        max_chance = 100

    return random.randrange(min_chance, max_chance + 1) / 100

# my_example_odds = {
#     DisasterType.fire: 0.3,
#     DisasterType.tornado: 0.2,
#     DisasterType.hurricane: 0.14,
#     DisasterType.earthquake: 0.29,
#     DisasterType.monster: 0.9,
#     DisasterType.ufo: 0.1,
# }
# my_sensor_odds = provide_sensor_ranges( my_example_odds )
# print( my_example_odds )
# print("-=-=-=-=-")
# print( my_sensor_odds )
# print("-=-=-=-=-")
