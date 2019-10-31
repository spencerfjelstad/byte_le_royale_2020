from game.common.enums import *


class GameStats:

    # cost in man_power to upgrade a building
    building_effort = {
        BuildingLevel.level_zero: 0,
        BuildingLevel.level_one: 50,
        BuildingLevel.level_two: 100,
        BuildingLevel.level_three: 500
    }

    # Costs to go up to the next city level
    city_upgrade_cost = {
        CityLevel.level_zero: 0,
        CityLevel.level_one: 100,
        CityLevel.level_two: 300
    }

    # Percentage of remaining strength of a disaster
    # (100 implies decree has no effect, 0 implies decree completely negates the disaster)
    decree_population_effect = 0
    decree_structure_effect = 0

    # Boost added onto a decree if you have a structure with the matching level
    decree_boost = {
        BuildingLevel.level_zero: 0,
        BuildingLevel.level_one: 0.1,
        BuildingLevel.level_two: 0.25,
        BuildingLevel.level_three: 0.5
    }

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

    # When converting effort to one of the below, multiply the effort amount by the multiplier
    # Keep multiplier above 0 and close to 1
    effort_gold_multiplier = 1
    effort_population_multiplier = 1
    effort_structure_multiplier = 1

    # population
    city_population = 100

    # health
    city_structure = 200

    # resources
    resources = 100

    # gold
    city_gold = 100

    # cost in gold to build a sensor
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

    action_sort_order = {
        ActionType.none: 0,
        ActionType.repair_structure: 2,
        ActionType.regain_population: 3,
        ActionType.accumulate_wealth: 4,
        ActionType.upgrade_city: 1
    }
    object_sort_order = {
        ObjectType.none: 5,
        ObjectType.disaster: 6,
        ObjectType.sensor: 7,
        ObjectType.city: 1.5,
        ObjectType.building: 8,
    }
