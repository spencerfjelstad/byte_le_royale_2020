import random


def clamp(value, min_value=0, max_value=100):
    return min(max_value, max(value, min_value))


def decision(probability):
    return random.random() < probability / 10


def enum_iter(enum_class):
    return [enum_class.__dict__[key] for key in enum_class.__dict__ if not key.startswith("__")]
