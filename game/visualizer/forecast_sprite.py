import cocos
from game.utils.helpers import *


class ForecastLayer(cocos.layer.Layer):
    def __init__(self, turn, display_size, log_parser):
        self.turn = turn
        self.display = display_size
        self.parser = log_parser
        super().__init__()
        images = {
            "0": "game/visualizer/assets/forecast_assets/tape_fire.png",
            "1": "game/visualizer/assets/forecast_assets/tape_tornado.png",
            "2": "game/visualizer/assets/forecast_assets/tape_hurricane.png",
            "3": "game/visualizer/assets/forecast_assets/tape_earthquake.png",
            "4": "game/visualizer/assets/forecast_assets/tape_monster.png",
            "5": "game/visualizer/assets/forecast_assets/tape_ufo.png",
            "6": "game/visualizer/assets/forecast_assets/tape_clear.png"
        }

        forecast = self.parser.turns[clamp(turn-3, 0, turn):clamp(turn+2, 0, len(self.parser.turns)):]

        for i in range(len(forecast)):
            spr = cocos.sprite.Sprite(images["6"])
            for key, item in forecast[i]['rates'].items():
                if item == 0:
                    spr = cocos.sprite.Sprite(images[key])
            if self.turn < 2:
                spr.position = self.display[0]/2+(i+3)*64-172, self.display[1]-50
            elif self.turn < 3:
                spr.position = self.display[0]/2+(i+2)*64-172, self.display[1]-50
            else:
                spr.position = self.display[0]/2+(i+1)*64-172, self.display[1]-50
            self.add(spr)
