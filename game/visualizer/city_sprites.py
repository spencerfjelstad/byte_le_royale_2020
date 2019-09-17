import pygame
from game.visualizer.sprite_sheet_functions import *
from game.config import *

class CitySprite(pygame.sprite.Sprite):
    def __init__(self, sprite_dimensions, city_level):
        super().__init__()

        #loads the image
        sprite_sheet = SpriteSheet("game/visualizer/assets/city_assets/city_default.png")
        self.image = sprite_sheet.get_image(sprite_dimensions[0], sprite_dimensions[1], sprite_dimensions[2], sprite_dimensions[3])

        #image needs rect to work
        self.rect = self.image.get_rect()
#Initialize all the city sprite objects
class CitySpriteLevel0(CitySprite):
    def __init__(self, x, y, city_level):
        CitySprite.__init__(self, [-x, -y, DISPLAY_SIZE[0], DISPLAY_SIZE[1]], city_level)
class CitySpriteLevel1(CitySprite):
    def __init__(self, x, y, city_level):
        CitySprite.__init__(self, [-x, -y, DISPLAY_SIZE[0], DISPLAY_SIZE[1]], city_level)
class CitySpriteLevel2(CitySprite):
    def __init__(self, x, y, city_level):
        CitySprite.__init__(self, [-x, -y, DISPLAY_SIZE[0], DISPLAY_SIZE[1]], city_level)
class CitySpriteDestroyedLevel0(CitySprite):
    def __init__(self, x, y, city_level):
        CitySprite.__init__(self, [-x, -y, DISPLAY_SIZE[0], DISPLAY_SIZE[1]], city_level)
class CitySpriteDestroyedLevel1(CitySprite):
    def __init__(self, x, y, city_level):
        CitySprite.__init__(self, [-x, -y, DISPLAY_SIZE[0], DISPLAY_SIZE[1]], city_level)
class CitySpriteDestroyedLevel2(CitySprite):
    def __init__(self, x, y, city_level):
        CitySprite.__init__(self, [-x, -y, DISPLAY_SIZE[0], DISPLAY_SIZE[1]], city_level)






