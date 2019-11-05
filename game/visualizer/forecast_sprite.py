import cocos
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
            spr = self.images["6"]
            for key, item in forecast[i]['rates'].items():
                if item == 0:
                    spr = self.images[key]
            if self.turn < 2:
                spr.position = self.display[0]/2+(i+3)*64-172, self.display[1]-50
            elif self.turn < 3:
                spr.position = self.display[0]/2+(i+2)*64-172, self.display[1]-50
            else:
                spr.position = self.display[0]/2+(i+1)*64-172, self.display[1]-50
            self.add(spr)
