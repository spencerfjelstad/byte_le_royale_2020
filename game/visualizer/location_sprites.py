# import pygame
# from game.visualizer.sprite_sheet_functions import *
# from game.config import *
# from game.common.enums import CityLocation
#
# class LocationSprites(pygame.sprite.Sprite):
#     def __init__(self, sprite_dimensions, location_type):
#         super().__init__()
#         #loads the image
#
#         sprite_sheet = SpriteSheet("game/visualizer/assets/location_assets/location_plains.png")
#         self.image = sprite_sheet.get_image(sprite_dimensions[0], sprite_dimensions[1], sprite_dimensions[2], sprite_dimensions[3])
#
#         self.rect = self.image.get_rect()
#
# class LocationDefault(LocationSprites):
#     def __init__(self, x, y, location_type):
#         LocationSprites.__init__(self, [-x, -y, DISPLAY_SIZE[0], DISPLAY_SIZE[1]], location_type)
#

import cocos


class LocationLayer(cocos.layer.Layer):
    def __init__(self, display_size, image):
        self.display = display_size
        self.image = image
        super().__init__()
        locations = {
            'plains': 'game/visualizer/assets/location_assets/location_plains.png',
            '1': '',
            '2': '',
            '3': '',
            '4': ''
        }

        location = cocos.sprite.Sprite(locations.get(image))
        location.position = self.display[0]/2, self.display[1]/2

        self.add(location)
