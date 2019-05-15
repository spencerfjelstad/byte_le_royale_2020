class GameStats:

    # units of man_power per 1k population
    man_power = 5

    # cost in man_power to build a sensor
    sensor_costs = {
        0: 0,
        1: 50,
        2: 100,
        3: 500
    }

    # error range provided by each sensor
    sensor_ranges = {
        0: 30,
        1: 15,
        2: 8,
        3: 2
    }
