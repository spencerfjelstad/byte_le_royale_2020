from game.common.enums import *


class GameStats:

    # cost in man_power to upgrade a building
    building_upgrade_cost = {
        BuildingType.police_station: {
            BuildingLevel.level_zero: 0,
            BuildingLevel.level_one: 40750,
        },
        BuildingType.gelato_shop: {
            BuildingLevel.level_zero: 0,
            BuildingLevel.level_one: 35050,
        },
        BuildingType.big_canoe: {
            BuildingLevel.level_zero: 0,
            BuildingLevel.level_one: 80100,
        },
        BuildingType.mint: {
            BuildingLevel.level_zero: 0,
            BuildingLevel.level_one: 28440,
        },
        BuildingType.billboard: {
            BuildingLevel.level_zero: 0,
            BuildingLevel.level_one: 28440,
        },
        BuildingType.printer: {
            BuildingLevel.level_zero: 0,
            BuildingLevel.level_one: 35050,
        }
    }

    # Costs to go up to the next city level
    city_upgrade_cost = {
        CityLevel.level_zero: 0,
        CityLevel.level_one: 15000,
        CityLevel.level_two: 16875,
        CityLevel.level_three: 20625
    }

    # cost in man_power to build a sensor
    sensor_upgrade_cost = {
        SensorLevel.level_zero: 0,
        SensorLevel.level_one: 4000,
        SensorLevel.level_two: 8500,
        SensorLevel.level_three: 13500
    }

    # Decree effectiveness when applied against a disaster
    # (0 implies decree has no effect, 1.0 implies decree completely negates the disaster)
    decree_population_effect = 0.5
    decree_structure_effect = 0.5

    # Boost multiplied by the decree if you have a structure with the matching level
    decree_boost = {
        BuildingLevel.level_zero: 1,
        BuildingLevel.level_one: 1.5,
    }

    everything_boost = {
        'wealth': {
            BuildingLevel.level_zero: 0,
            BuildingLevel.level_one: 200,
        },
        'population': {
            BuildingLevel.level_zero: 0,
            BuildingLevel.level_one: 30,
        },
        'structure': {
            BuildingLevel.level_zero: 0,
            BuildingLevel.level_one: 30,
        }
    }

    wealth_boost = {
        BuildingLevel.level_zero: 0,
        BuildingLevel.level_one: 150,
    }

    population_boost = {
        BuildingLevel.level_zero: 0,
        BuildingLevel.level_one: 25,
    }

    structure_boost = {
        BuildingLevel.level_zero: 0,
        BuildingLevel.level_one: 25,
    }

    # required effort to stop lasting disasters
    disaster_initial_efforts = {
        DisasterType.fire: {
            DisasterLevel.level_zero: 400,
            DisasterLevel.level_one: 800,
            DisasterLevel.level_two: 1350,
            DisasterLevel.level_three: 2200
        },
        DisasterType.blizzard: {
            DisasterLevel.level_zero: 600,
            DisasterLevel.level_one: 1350,
            DisasterLevel.level_two: 2025,
            DisasterLevel.level_three: 3300
        },
        DisasterType.monster: {
            DisasterLevel.level_zero: 800,
            DisasterLevel.level_one: 1800,
            DisasterLevel.level_two: 3300,
            DisasterLevel.level_three: 5600
        },
    }

    # structural damage caused by a disaster
    disaster_structure_damages = {
        DisasterType.fire: {
            DisasterLevel.level_zero: 1,
            DisasterLevel.level_one: 1,
            DisasterLevel.level_two: 1,
            DisasterLevel.level_three: 1
        },
        DisasterType.tornado: {
            DisasterLevel.level_zero: 25,
            DisasterLevel.level_one: 50,
            DisasterLevel.level_two: 75,
            DisasterLevel.level_three: 100
        },
        DisasterType.blizzard: {
            DisasterLevel.level_zero: 3,
            DisasterLevel.level_one: 3,
            DisasterLevel.level_two: 3,
            DisasterLevel.level_three: 3
        },
        DisasterType.earthquake: {
            DisasterLevel.level_zero: 50,
            DisasterLevel.level_one: 100,
            DisasterLevel.level_two: 200,
            DisasterLevel.level_three: 300
        },
        DisasterType.monster: {
            DisasterLevel.level_zero: 10,
            DisasterLevel.level_one: 10,
            DisasterLevel.level_two: 10,
            DisasterLevel.level_three: 10
        },
        DisasterType.ufo: {
            DisasterLevel.level_zero: 50,
            DisasterLevel.level_one: 100,
            DisasterLevel.level_two: 200,
            DisasterLevel.level_three: 400
        },
    }

    # population damage caused by a disaster
    disaster_population_damages = {
        DisasterType.fire: {
            DisasterLevel.level_zero: 2,
            DisasterLevel.level_one: 2,
            DisasterLevel.level_two: 2,
            DisasterLevel.level_three: 2
        },
        DisasterType.tornado: {
            DisasterLevel.level_zero: 12,
            DisasterLevel.level_one: 25,
            DisasterLevel.level_two: 37,
            DisasterLevel.level_three: 50
        },
        DisasterType.blizzard: {
            DisasterLevel.level_zero: 6,
            DisasterLevel.level_one: 6,
            DisasterLevel.level_two: 6,
            DisasterLevel.level_three: 6
        },
        DisasterType.earthquake: {
            DisasterLevel.level_zero: 25,
            DisasterLevel.level_one: 50,
            DisasterLevel.level_two: 100,
            DisasterLevel.level_three: 150
        },
        DisasterType.monster: {
            DisasterLevel.level_zero: 5,
            DisasterLevel.level_one: 5,
            DisasterLevel.level_two: 5,
            DisasterLevel.level_three: 5
        },
        DisasterType.ufo: {
            DisasterLevel.level_zero: 100,
            DisasterLevel.level_one: 200,
            DisasterLevel.level_two: 400,
            DisasterLevel.level_three: 800
        },
    }

    # Dictionary of when the disasters will start to be the given level
    disaster_level_markers = {
        DisasterType.fire: {
            DisasterLevel.level_zero: 0,
            DisasterLevel.level_one: 250,
            DisasterLevel.level_two: 500,
            DisasterLevel.level_three: 750
        },
        DisasterType.tornado: {
            DisasterLevel.level_zero: 0,
            DisasterLevel.level_one: 300,
            DisasterLevel.level_two: 600,
            DisasterLevel.level_three: 900
        },
        DisasterType.blizzard: {
            DisasterLevel.level_zero: 0,
            DisasterLevel.level_one: 500,
            DisasterLevel.level_two: 750,
            DisasterLevel.level_three: 1000
        },
        DisasterType.earthquake: {
            DisasterLevel.level_zero: 0,
            DisasterLevel.level_one: 550,
            DisasterLevel.level_two: 850,
            DisasterLevel.level_three: 1150
        },
        DisasterType.monster: {
            DisasterLevel.level_zero: 0,
            DisasterLevel.level_one: 750,
            DisasterLevel.level_two: 1000,
            DisasterLevel.level_three: 1250
        },
        DisasterType.ufo: {
            DisasterLevel.level_zero: 0,
            DisasterLevel.level_one: 800,
            DisasterLevel.level_two: 1100,
            DisasterLevel.level_three: 1400
        },
    }

    # When converting effort to one of the below, multiply the effort amount by the multiplier
    # Keep multiplier above 0 and close to 1
    effort_gold_multiplier = 1
    effort_population_multiplier = 0.5
    effort_structure_multiplier = 0.5

    # starting city population
    city_population = 40

    # starting city health
    city_structure = 100

    # gold
    city_gold = 0
    city_gold_accumulative = 10
    city_type_invested_bonus = 20000

    # Max structure based on city level
    city_max_structure = {
        CityLevel.level_zero: 200,
        CityLevel.level_one: 225,
        CityLevel.level_two: 275,
        CityLevel.level_three: 350
    }

    # error range provided by each sensor
    sensor_ranges = {
        SensorLevel.level_zero: 100,
        SensorLevel.level_one: 50,
        SensorLevel.level_two: 20,
        SensorLevel.level_three: 1
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
