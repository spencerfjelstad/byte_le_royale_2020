import math
import random

from game.common.stats import GameStats
from game.common.enums import *

# provide_sensor_ranges
# @parameters
# odds : dict : the odds the disasters are occurring on a given turn
#
# @returns
# adjusted_weights : dict : a dictionary of dictionaries that provides the detected error by each sensor
def provide_sensor_ranges(odds):

    adjusted_weights = {}

    for disaster in [ DisasterType.fire,
                      DisasterType.tornado,
                      DisasterType.hurricane,
                      DisasterType.earthquake,
                      DisasterType.monster,
                      DisasterType.ufo ]:
        sensor_odds = {}

        disaster_odds = odds[disaster]

        for sensor_level in [ SensorLevel.level_zero,
                              SensorLevel.level_one,
                              SensorLevel.level_two,
                              SensorLevel.level_three ]:
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

    range = math.floor(GameStats.sensor_ranges[sensor_level] / 2)

    if sensor_level == SensorLevel.level_zero:
        range = GameStats.sensor_ranges[0]
    elif sensor_level == SensorLevel.level_one:
        range = GameStats.sensor_ranges[1]
    elif sensor_level == SensorLevel.level_two:
        range = GameStats.sensor_ranges[2]
    elif sensor_level == SensorLevel.level_three:
        range = GameStats.sensor_ranges[3]
    else:
        raise Exception("Sensor level out of bounds. Should be SensorLevel.level_zero <= x <= SensorLevel.level_three.")

    # Modify chance so it doesn't provide us odds out of bounds
    if chance - range < 0:
        chance = range
    if chance + range > 100:
        chance = 100 - range

    return random.randrange(chance - range, chance + range + 1) / 100

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