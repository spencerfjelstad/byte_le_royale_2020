import cocos
from game.utils.helpers import *


class ForecastLayer(cocos.layer.Layer):
    def __init__(self, turn, log_parser):
        self.turn = turn
        self.parser = log_parser
        super().__init__()

        forecast = self.parser.turns[clamp(turn-3, 0, turn):clamp(turn+2, 0, len(self.parser.turns)):]

        for i in range(len(forecast)):
            label = cocos.text.Label(str(forecast[i]["player"].get('city').get('sensors').get('0').get('sensor_results')),
                                     font_name="Times New Roman",
                                     font_size=64,
                                     anchor_x='center',
                                     anchor_y='center')
            label.position = (i+1)*192, 200
            self.add(label)