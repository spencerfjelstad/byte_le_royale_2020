import pygame
from game.visualizer.sprite_sheet_functions import *
from game.config import *
from game.visualizer.game_log_parser import *

def draw_city_sprites(turn_info, group, surf):
    group.empty()
    # Sprite changing logic
    city_x = 484


    # Checks city_structure and draws sprite accordingly
    structure = int(turn_info['player'].get('city').get('structure'))
    if structure > 150:
        city_y = 0
        city_sprite = CitySpriteLevel1(city_x, city_y, turn_info)
        group.add(city_sprite)
    else:
        city_y = 200
        group.empty()
        city_sprite = CitySpriteLevel0(city_x, city_y, turn_info)
        group.add(city_sprite)

    group.draw(surf)



class CitySprite(pygame.sprite.Sprite):
    def __init__(self, sprite_dimensions, turn_info):
        super().__init__()
        self.info = turn_info
        #loads and gets the correct image
        structure = int(self.info['player'].get('city').get('structure'))
        if structure > 150:
            sprite_sheet = SpriteSheet("game/visualizer/assets/city_assets/city_level1.png")
        else:
            sprite_sheet = SpriteSheet("game/visualizer/assets/city_assets/city_default.png")



        # sprite_dimensions[0] and [1] are x.
        # [2] and [3] are the width and height. width and height must be the display width and height, because
        # SpriteSheet is basically making a new surface, and the surface must be the same size the the display for the image
        # to be drawn properly onto the screen
        self.image = sprite_sheet.get_image(-sprite_dimensions[0], -sprite_dimensions[1], sprite_dimensions[2], sprite_dimensions[3])

        #image needs rect to work
        self.rect = self.image.get_rect()
#Initialize all the city sprite objects
class CitySpriteLevel0(CitySprite):
    def __init__(self, x, y, info):
        CitySprite.__init__(self, [x, y, DISPLAY_SIZE[0], DISPLAY_SIZE[1]], info)
class CitySpriteLevel1(CitySprite):
    def __init__(self, x, y, info):
        CitySprite.__init__(self, [x, y, DISPLAY_SIZE[0], DISPLAY_SIZE[1]], info)
class CitySpriteLevel2(CitySprite):
    def __init__(self, x, y, info):
        CitySprite.__init__(self, [x, y, DISPLAY_SIZE[0], DISPLAY_SIZE[1]], info)
class CitySpriteDestroyedLevel0(CitySprite):
    def __init__(self, x, y, info):
        CitySprite.__init__(self, [x, y, DISPLAY_SIZE[0], DISPLAY_SIZE[1]], info)
class CitySpriteDestroyedLevel1(CitySprite):
    def __init__(self, x, y, info):
        CitySprite.__init__(self, [x, y, DISPLAY_SIZE[0], DISPLAY_SIZE[1]], info)
class CitySpriteDestroyedLevel2(CitySprite):
    def __init__(self, x, y, info):
        CitySprite.__init__(self, [x, y, DISPLAY_SIZE[0], DISPLAY_SIZE[1]], info)






