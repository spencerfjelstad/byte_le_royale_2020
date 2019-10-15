class ActionType:
    none = 0
    repair = 1
    upgrade = 2
    accumulate_wealth = 3
    build = 4


class CityLocation:
    plains = 0
    desert = 1
    mountains = 2
    coastal = 3
    radioactive_wasteland = 4


class CityLevel:
    level_zero = 0
    level_one = 1
    level_two = 2


class CityType:
    none = 0
    healthy = 1
    sturdy = 2
    invested = 3


class DamageScaling:
    low = 0
    medium = 1
    high = 2
    extreme = 3


class DecreeType:
    anti_fire_bears = 0
    paperweights = 1
    hound_news = 2
    moon_shoes = 3
    away_spray = 4
    giant_fly_swatter = 5


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


class EventType:
    sensor_upgrade = 0
    disaster_spawned = 1
    disaster_eliminated = 2


class ObjectType:
    none = 0
    action = 1
    disaster = 2
    sensor = 3
    city = 4
    player = 5


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
    scp_foundation = 4  # placeholder?
    satellite_dish = 5


class DebugLevel:
    none = 0
    client = 1
    controller = 2
    engine = 3
