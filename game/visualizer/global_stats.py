class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class GlobalStats(metaclass=Singleton):
    def __init__(self):
        self.turn_speed = 1
        self.base_turn_time = 0.1
        self.disaster_turn_time = 2
