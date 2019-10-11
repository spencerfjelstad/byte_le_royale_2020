import cocos
import pyglet
from cocos.sprite import Sprite


class HurricaneLayer(cocos.layer.Layer):
    def __init__(self, display_size, turn_info):
        super().__init__()
        self.display = display_size
        self.info = turn_info

        #Loads the hurricane animation
        image = pyglet.image.load_animation("game/visualizer/assets/disaster_assets/hurricane.gif")
        rates = -1
        #Check the rate
        try:
            for key, item in self.info['rates'].items():
                if key is "2":
                    rates = item
        except:
            print("YEET")
        #If the rate is 0, that means the hurricane happened, so draw to screen
        if rates == 0:
            self.hurricane = cocos.sprite.Sprite(image)

            self.hurricane_x = int(self.display[0]/2)
            self.hurricane_y = int(self.display[1]/2)

            self.hurricane.position = (self.hurricane_x, self.hurricane_y)
            self.add(self.hurricane)


