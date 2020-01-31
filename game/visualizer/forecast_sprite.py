import cocos
import random
from game.utils.helpers import *


class ForecastLayer(cocos.layer.Layer):
    def __init__(self, turn, display_size, log_parser, assets):
        self.turn = turn
        self.display = display_size
        self.parser = log_parser
        self.images = assets
        super().__init__()
        # Generates list of future and past turns given the current turn and saves it as 'forecast'
        forecast = self.parser.turns[clamp(turn-3, 0, turn):clamp(turn+2, 0, len(self.parser.turns)):]

        # For each item in forecast displays the correct image in the correct location
        for i in range(len(forecast)):
            # Choose a random clear forecast sprite
            num = random.randint(0, 2)
            if num == 0:
                spr = self.images['clear'][i]
            elif num == 1:
                spr = self.images['clear2'][i]
            else:
                spr = self.images['clear3'][i]

            for key, item in forecast[i]['rates'].items():
                if item == 0 and key == "0":
                    spr = self.images['fire'][i]
                if item == 0 and key is "1":
                    spr = self.images['tornado'][i]
                if item == 0 and key is "2":
                    spr = self.images['blizzard'][i]
                if item == 0 and key is "3":
                    spr = self.images['earthquake'][i]
                if item == 0 and key is "4":
                    spr = self.images['monster'][i]
                if item == 0 and key is "5":
                    spr = self.images['ufo'][i]
            if self.turn < 2:
                spr.position = self.display[0]/2+(i+3)*64-172, self.display[1]-50
            elif self.turn < 3:
                spr.position = self.display[0]/2+(i+2)*64-172, self.display[1]-50
            else:
                spr.position = self.display[0]/2+(i+1)*64-172, self.display[1]-50
            self.add(spr)


class DisasterLevelLayer(cocos.layer.Layer):
    def __init__(self, turn, display_size, log_parser, assets):
        self.turn = turn
        self.images = assets
        self.parser = log_parser
        super().__init__()
        # forecast = self.parser.turns[clamp(turn - 3, 0, turn):clamp(turn + 2, 0, len(self.parser.turns)):]
        # for i in range(len(forecast)):
        #     for key, item in forecast[i]['player']['city'].items():
        spr = self.images['bronze'][0]
        spr.position = 682, 648
        self.add(spr)


class ForecastHolderLayer(cocos.layer.Layer):
    def __init__(self, assets):
        self.images = assets
        super().__init__()

        spr = self.images['forecast_hold']
        spr.position = 660, 662
        self.add(spr)
