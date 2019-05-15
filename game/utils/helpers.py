import random


def decision(probability):
    return random.random() < probability / 10


def clamp(value, min_value=0, max_value=100):
    return min(max_value, max(value, min_value))
