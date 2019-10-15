import cocos
import pyglet
from cocos.actions import  *


class FireLayer(cocos.layer.Layer):
    def __init__(self, display_size, turn_info):
        super().__init__()
        self.display = display_size
        self.info = turn_info
        # Loads the Fire Animation
        image = pyglet.image.load_animation("game/visualizer/assets/disaster_assets/fire.gif")
        rates = -1
        # Check the rate
        try:
            for key, item in self.info['rates'].items():
                if key is "0":
                    rates = item
        except:
            print("YEET")

        # If the rate is 0, that means the Fire happened, so draw to screen
        if rates == 0:
            self.fire = cocos.sprite.Sprite(image)
            self.fire_x = int(self.display[0]-self.fire.width/2)
            self.fire_y = int(self.display[1]/4)

            self.fire.position = (self.fire_x, self.fire_y)
            self.add(self.fire)


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
            self.tornado_x = 0
            self.tornado_y = int(self.display[1]/2)

            self.tornado.position = (self.tornado_x, self.tornado_y)
            self.tornado.do(MoveBy((self.display[0], 0), 2))
            self.add(self.tornado)


class HurricaneLayer(cocos.layer.Layer):
    def __init__(self, display_size, turn_info):
        super().__init__()
        self.display = display_size
        self.info = turn_info

        # Loads the hurricane animation
        image = pyglet.image.load_animation("game/visualizer/assets/disaster_assets/hurricane.gif")
        rates = -1
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


class EarthquakeLayer(cocos.layer.Layer):
    def __init__(self, display_size, turn_info):
        super().__init__()
        self.display = display_size
        self.info = turn_info

        # Loads the earthquake animation
        image = pyglet.image.load_animation("game/visualizer/assets/disaster_assets/earthquake.gif")
        rates = -1
        # Check the rate
        try:
            for key, item in self.info['rates'].items():
                if key is "3":
                    rates = item
        except:
            print("YEET")

        # If the rate is 0, that means the earthquake happened, so draw to screen
        if rates == 0:
            self.earthquake = cocos.sprite.Sprite(image)
            self.earthquake_x = int(self.display[0]/2)
            self.earthquake_y = int(self.display[1]/2)

            self.earthquake.position = (self.earthquake_x, self.earthquake_y)
            self.add(self.earthquake)


class MonsterLayer(cocos.layer.Layer):
    def __init__(self, display_size, turn_info):
        super().__init__()
        self.display = display_size
        self.info = turn_info

        # Loads the monster animation
        image = "game/visualizer/assets/disaster_assets/monster.png"
        rates = -1
        # Check the rate
        try:
            for key, item in self.info['rates'].items():
                if key is "4":
                    rates = item
        except:
            print("YEET")

        # If the rate is 0, that means the monster happened, so draw to screen
        if rates == 0:
            self.monster = cocos.sprite.Sprite(image)
            self.monster_x = int(self.display[0]/2)
            self.monster_y = int(self.display[1])

            self.monster.position = (self.monster_x, self.monster_y)
            self.monster.do(MoveBy((self.monster_x, -self.monster_y/2), 2))
            self.add(self.monster)


class UFOLayer(cocos.layer.Layer):
    def __init__(self, display_size, turn_info):
        super().__init__()
        self.display = display_size
        self.info = turn_info

        # Loads the ufo animation
        image = pyglet.image.load_animation("game/visualizer/assets/disaster_assets/ufo.gif")
        rates = -1
        # Check the rate
        try:
            for key, item in self.info['rates'].items():
                if key is "5":
                    rates = item
        except:
            print("YEET")

        # If the rate is 0, that means the ufo happened, so draw to screen
        if rates == 0:
            self.ufo = cocos.sprite.Sprite(image)
            self.ufo_x = 0
            self.ufo_y = int(self.display[1]/2)

            self.ufo.position = (self.ufo_x, self.ufo_y)
            self.ufo.do(MoveBy((self.display[0], 0), 2))
            self.add(self.ufo)




