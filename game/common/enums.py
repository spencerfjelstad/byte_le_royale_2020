from enum import Enum

class DisasterType(Enum):
    fire = 0
    tornado = 1
    hurricane = 2
    earthquake = 3
    monster = 4
    ufo = 5

class ActionType(Enum):
    none = 0
    repair = 1
    upgrade = 2
    accumulate_wealth = 3
    build = 4

class SensorType(Enum):
    fire_alarm = 0
    rock_on_a_rope = 1
    coast_guard = 2
    seismograph = 3
    ## TODO: come up with a sensor that detects monsters
    satellite_dish = 5

class SensorLevel(Enum):
    level_zero = 0
    level_one = 1
    level_two = 2
    level_three = 3