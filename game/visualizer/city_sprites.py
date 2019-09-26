import pygame
from game.visualizer.sprite_sheet_functions import *
from game.config import *
from game.visualizer.game_log_parser import *

def draw_city_sprites(turn_info, surf):
    x = 484
    y = 200
    #Draw Sprite object
    CitySprite(x , y , surf, turn_info)




class CitySprite(pygame.sprite.Sprite):
    def __init__(self, x, y, surf, turn_info):
        super().__init__()
        self.info = turn_info
        images = [
            "game/visualizer/assets/city_assets/city_level1.png",
            "game/visualizer/assets/city_assets/city_default.png",
        ]

        structure = int(self.info['player'].get('city').get('structure'))
        if structure is not None:
            if structure > 150:
                self.image = pygame.image.load(images[0])
            else:
                self.image = pygame.image.load(images[1])

        surf.blit(self.image, (x,y))
        #image needs rect to work
        self.rect = self.image.get_rect()






