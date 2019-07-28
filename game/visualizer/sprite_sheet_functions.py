import pygame
import zipfile

class SpriteSheet(object):

    def __init__(self, file_name):
        f = zipfile.ZipFile("br_launcher.pyz", 'r')
        self.sprite_sheet = pygame.image.load(f.open(file_name)).convert_alpha()

    def get_image(self, x, y, width, height):
        image = pygame.Surface([width, height], pygame.SRCALPHA).convert_alpha()
        image.blit(self.sprite_sheet, (0,0), (x, y, width, height))
        return image

