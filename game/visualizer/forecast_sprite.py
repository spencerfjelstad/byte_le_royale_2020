import cocos
from game.utils.helpers import *


class ForecastLayer(cocos.layer.Layer):
    def __init__(self, turn, log_parser):
        self.turn = turn
        self.parser = log_parser
        super().__init__()

        forecast = self.parser.turns[clamp(turn-3, 0, turn):clamp(turn+2, 0, len(self.parser.turns)):]

        for i in range(len(forecast)):
            text = str(forecast[i]["player"].get('city').get('sensors').get('0').get('sensor_results'))
            label = cocos.text.Label('0' if text is ' ' else text,
                                     font_name="Times New Roman",
                                     font_size=64,
                                     anchor_x='center',
                                     anchor_y='center')
            if self.turn < 2:
                label.position = (i+3)*192, 200
            elif self.turn < 3:
                label.position = (i + 2) * 192, 200
            else:
                label.position = (i+1)*192, 200
            self.add(label)