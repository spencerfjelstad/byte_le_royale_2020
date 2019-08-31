from game.common.enums import *


class GameStats:

    # multiplier done by instant disasters
    disaster_damage_instant_multiplier = 5

    # damage done at each damage level
    disaster_damage_scale = {
        DamageScaling.low: 1,
        DamageScaling.medium: 2,
        DamageScaling.high: 3,
        DamageScaling.extreme: 4
    }

    # required effort to stop lasting disasters
    disaster_initial_efforts = {
        DisasterType.fire: 100,
        DisasterType.hurricane: 200,
        DisasterType.monster: 300
    }

    # structural damage caused by a disaster
    disaster_structure_damages = {
        DisasterType.fire: disaster_damage_scale[DamageScaling.low],
        DisasterType.tornado: disaster_damage_scale[DamageScaling.medium] * disaster_damage_instant_multiplier,
        DisasterType.hurricane: disaster_damage_scale[DamageScaling.medium],
        DisasterType.earthquake: disaster_damage_scale[DamageScaling.high] * disaster_damage_instant_multiplier,
        DisasterType.monster: disaster_damage_scale[DamageScaling.extreme],
        DisasterType.ufo: disaster_damage_scale[DamageScaling.medium] * disaster_damage_instant_multiplier
    }

    # population damage caused by a disaster
    disaster_population_damages = {
        DisasterType.fire: disaster_damage_scale[DamageScaling.medium],
        DisasterType.tornado: disaster_damage_scale[DamageScaling.low] * disaster_damage_instant_multiplier,
        DisasterType.hurricane: disaster_damage_scale[DamageScaling.high],
        DisasterType.earthquake: disaster_damage_scale[DamageScaling.medium] * disaster_damage_instant_multiplier,
        DisasterType.monster: disaster_damage_scale[DamageScaling.medium],
        DisasterType.ufo: disaster_damage_scale[DamageScaling.extreme] * disaster_damage_instant_multiplier
    }

    # units of man_power per 1k population
    man_power = 5
    #population
    city_population = 100
    #health
    city_structure = 200
    #resources
    resources = 100
    #gold
    city_gold = 100

    #cost in gold to build a sensor
    sensor_costs = {
        SensorLevel.level_zero: 0,
        SensorLevel.level_one: 100,
        SensorLevel.level_two: 500,
        SensorLevel.level_three: 1000
    }

    # cost in man_power to build a sensor
    sensor_effort = {
        SensorLevel.level_zero: 0,
        SensorLevel.level_one: 50,
        SensorLevel.level_two: 100,
        SensorLevel.level_three: 500
    }

    # error range provided by each sensor
    sensor_ranges = {
        SensorLevel.level_zero: 30,
        SensorLevel.level_one: 15,
        SensorLevel.level_two: 8,
        SensorLevel.level_three: 2
    }
