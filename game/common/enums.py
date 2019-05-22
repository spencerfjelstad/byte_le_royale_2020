class ActionType:
    none = 0
    repair = 1
    upgrade = 2
    accumulate_wealth = 3
    build = 4


class DamageScaling:
    low = 0
    medium = 1
    high = 2
    extreme = 3


class DisasterStatus:
    live = 1
    dead = 0


class DisasterType:
    fire = 0
    tornado = 1
    hurricane = 2
    earthquake = 3
    monster = 4
    ufo = 5


class PreemptiveType:
    anti_fire_bears = 0
    paperweights = 1
    moon_shoes = 2
    hound_news = 3
    away_spray = 4
    giant_fly_swatter = 5


class ReactiveType:
    fire_station = 0
    pow_sham = 1
    monster_hunter = 2  # also considered mech


class SensorLevel:
    level_zero = 0
    level_one = 1
    level_two = 2
    level_three = 3


class SensorType:
    fire_alarm = 0
    rock_on_a_rope = 1
    coast_guard = 2
    seismograph = 3
    ## TODO: come up with a sensor that detects monsters
    satellite_dish = 5
