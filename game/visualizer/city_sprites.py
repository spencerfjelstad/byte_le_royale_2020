# import pygame
# from game.visualizer.sprite_sheet_functions import *
# from game.config import *
#
# class CitySprite(pygame.sprite.Sprite):
#     def __init__(self, sprite_dimensions, city_level):
#         super().__init__()
#
#         #loads the image
#         sprite_sheet = SpriteSheet("game/visualizer/assets/city_assets/city_default.png")
#         self.image = sprite_sheet.get_image(sprite_dimensions[0], sprite_dimensions[1], sprite_dimensions[2], sprite_dimensions[3])
#
#         #image needs rect to work
#         self.rect = self.image.get_rect()
# #Initialize all the city sprite objects
# class CitySpriteLevel0(CitySprite):
#     def __init__(self, x, y, city_level):
#         CitySprite.__init__(self, [-x, -y, DISPLAY_SIZE[0], DISPLAY_SIZE[1]], city_level)
# class CitySpriteLevel1(CitySprite):
#     def __init__(self, x, y, city_level):
#         CitySprite.__init__(self, [-x, -y, DISPLAY_SIZE[0], DISPLAY_SIZE[1]], city_level)
# class CitySpriteLevel2(CitySprite):
#     def __init__(self, x, y, city_level):
#         CitySprite.__init__(self, [-x, -y, DISPLAY_SIZE[0], DISPLAY_SIZE[1]], city_level)
# class CitySpriteDestroyedLevel0(CitySprite):
#     def __init__(self, x, y, city_level):
#         CitySprite.__init__(self, [-x, -y, DISPLAY_SIZE[0], DISPLAY_SIZE[1]], city_level)
# class CitySpriteDestroyedLevel1(CitySprite):
#     def __init__(self, x, y, city_level):
#         CitySprite.__init__(self, [-x, -y, DISPLAY_SIZE[0], DISPLAY_SIZE[1]], city_level)
# class CitySpriteDestroyedLevel2(CitySprite):
#     def __init__(self, x, y, city_level):
#         CitySprite.__init__(self, [-x, -y, DISPLAY_SIZE[0], DISPLAY_SIZE[1]], city_level)
import cocos


class CityLayer(cocos.layer.Layer):
    def __init__(self, display_size, turn_info):
        self.display = display_size
        self.info = turn_info
        super().__init__()
        images = [
            "game/visualizer/assets/city_assets/city_default.png",
            "game/visualizer/assets/city_assets/city_level1.png",
            "game/visualizer/assets/city_assets/city_level2.png",
            "game/visualizer/assets/city_assets/city_level3.png"
        ]
        structure = 0
        try:
            structure = int(self.info['player'].get('city').get('structure'))
        except:
            print("NO! >:(")

        if structure > 150:
            self.city = cocos.sprite.Sprite(images[3])
        elif structure > 100:
            self.city = cocos.sprite.Sprite(images[2])
        elif structure > 50:
            self.city = cocos.sprite.Sprite(images[1])
        else:
            self.city = cocos.sprite.Sprite(images[0])

        self.city.position = self.display[0]-804/2, self.display[1]-498/2
        self.add(self.city)
