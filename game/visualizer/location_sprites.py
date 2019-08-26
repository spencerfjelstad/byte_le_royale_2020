import pygame
from game.common.enums import CityLocation


class LocationSprites(pygame.sprite.Sprite):
    def __init__(self, x, y, location_type):
        super().__init__()


class LocationDefault(LocationSprites):
    def __init__(self, x, y):
        pass
