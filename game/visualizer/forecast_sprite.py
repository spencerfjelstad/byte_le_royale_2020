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

        # Forecast Holder
        fore_sprite = self.images['forecast_hold']
        fore_sprite.position = 640, 662
        self.add(fore_sprite)

        # Generates list of future and past turns given the current turn and saves it as 'forecast'
        forecast = self.parser.turns[clamp(turn-3, 0, turn):clamp(turn+2, 0, len(self.parser.turns)):]

        # For each item in forecast displays the correct image in the correct location
        for i in range(len(forecast)):
            # Choose a random clear forecast sprite
            num = (turn + i) % 9
            if num in [0, 1, 6]:
                spr = self.images['clear2'][i]
            elif num in [2, 4, 7]:
                spr = self.images['clear'][i]
            elif num in [3, 5, 8]:
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
                spr.position = self.display[0]/2+(i+3)*64-192, self.display[1]-50
            elif self.turn < 3:
                spr.position = self.display[0]/2+(i+2)*64-192, self.display[1]-50
            else:
                spr.position = self.display[0]/2+(i+1)*64-192, self.display[1]-50
            self.add(spr)


class DisasterLevelLayer(cocos.layer.Layer):
    def __init__(self, turn, display_size, log_parser, assets):
        self.turn = turn
        self.display = display_size
        self.parser = log_parser
        self.images = assets
        super().__init__()

        # Generates list of future and past turns given the current turn and saves it as 'forecast'
        forecast = self.parser.turns[clamp(turn - 3, 0, turn):clamp(turn + 2, 0, len(self.parser.turns)):]
        for i in range(len(forecast)):
            if len(forecast[i]['events']) > 0:
                for j in forecast[i]['events']:
                    if j['event_type'] == 3:
                        level = j['disaster']['level']
                        if level == 0:
                            spr = self.images['bronze'][i]
                        elif level == 1:
                            spr = self.images['silver'][i]
                        elif level == 2:
                            spr = self.images['gold'][i]
                        elif level == 3:
                            spr = self.images['uranium'][i]
                        elif level == 4:
                            spr = self.images['pluto'][i]

                        spr.position = self.display[0] / 2 + (i + 1) * 64 - 170, self.display[1] - 72
                        self.add(spr)

                        # 682, 648
