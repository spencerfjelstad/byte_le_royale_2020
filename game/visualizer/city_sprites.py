import pygame
from game.visualizer.sprite_sheet_functions import *
from game.config import *
from game.visualizer.game_log_parser import *

def draw_city_sprites(turn_info, surf):
    x = 484
    y = 0

    #Draw Sprite object
    CitySprite(x , y , surf, turn_info)




class CitySprite(pygame.sprite.Sprite):
    def __init__(self, x, y, surf, turn_info):
        super().__init__()
        self.info = turn_info
        # Create list of paths for sprites
        images = [
            "game/visualizer/assets/city_assets/city_default.png",
            "game/visualizer/assets/city_assets/city_level1.png",
            "game/visualizer/assets/city_assets/city_level2.png",
            "game/visualizer/assets/city_assets/city_level3.png"
        ]
        # Get turn info for the structure of the city
        structure = 0
        try:
            structure = int(self.info['player'].get('city').get('structure'))
        except:
            print("NO! >:(")

        # Check how much structure is left, and change sprite accordingly
        if structure > 150:
            self.image = pygame.image.load(images[3])
        elif structure > 100:
            self.image = pygame.image.load(images[2])
        elif structure > 50:
            self.image = pygame.image.load(images[1])
        else:
            self.image = pygame.image.load(images[0])

        #Gets the width and height of sprite
        self.rect = self.image.get_rect()

        #Draws sprite to screen
        surf.blit(self.image, (x,y))

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
