import cocos
import pyglet


class TornadoLayer(cocos.layer.Layer):
    def __init__(self, display_size, turn_info):
        super().__init__()
        self.display = display_size
        self.info = turn_info

        # Loads the Tornado Image
        image = "game/visualizer/assets/disaster_assets/tornado.png"
        rates = -1
        # Check the rate
        try:
            for key, item in self.info['rates'].items():
                if key is "1":
                    rates = item
        except:
            print("YEET")
        # If the rate is 0, that means the tornado happened, so draw to screen
        if rates == 0:
            self.tornado = cocos.sprite.Sprite(image)
            self.tornado_x = int(self.display[0]/2)
            self.tornado_y = int(self.display[1]/2)

            self.tornado.position = (self.tornado_x, self.tornado_y)
            self.add(self.tornado)


class HurricaneLayer(cocos.layer.Layer):
    def __init__(self, display_size, turn_info):
        super().__init__()
        self.display = display_size
        self.info = turn_info

        # Loads the hurricane animation
        image = pyglet.image.load_animation("game/visualizer/assets/disaster_assets/hurricane.gif")
        rates = 0
        # Check the rate
        try:
            for key, item in self.info['rates'].items():
                if key is "2":
                    rates = item
        except:
            print("YEET")
        # If the rate is 0, that means the hurricane happened, so draw to screen
        if rates == 0:
            self.hurricane = cocos.sprite.Sprite(image)
            self.hurricane.opacity = 155
            self.hurricane_x = int(self.display[0]/2)
            self.hurricane_y = int(self.display[1]/2)

            self.hurricane.position = (self.hurricane_x, self.hurricane_y)
            self.add(self.hurricane)



