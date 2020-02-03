import random

import cocos
import pyglet
from cocos.actions import *

from game.visualizer.global_stats import GlobalStats


class FireLayer(cocos.layer.Layer):
    def __init__(self, display_size, turn_info, assets):
        super().__init__()
        self.display = display_size
        self.info = turn_info
        self.images = assets

        global_stats = GlobalStats()

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
            for n in range(random.randint(0,19)):
                section1_x = random.randint(self.display[0] / 2, self.display[0] / 2 + 120)
                section1_y = random.randint(self.display[1]/2 - 8, self.display[1]/2 + 160)

                self.fire = self.images["fire"][n]
                self.fire_x = random.randint(section1_x, section1_x)
                self.fire_y = random.randint(section1_y, section1_y)
                self.fire.position = (self.fire_x, self.fire_y)
                self.add(self.fire)


class TornadoLayer(cocos.layer.Layer):
    def __init__(self, display_size, turn_info, assets):
        super().__init__()
        self.display = display_size
        self.info = turn_info
        self.images = assets

        global_stats = GlobalStats()

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
            self.tornado = self.images['tornado']
            self.tornado_x = 0
            self.tornado_y = int(self.display[1] / 2)

            self.tornado.position = (self.tornado_x, self.tornado_y)
            self.tornado.do(MoveBy((self.display[0], 0), global_stats.disaster_turn_time * global_stats.turn_speed))
            self.add(self.tornado)


class BlizzardLayer(cocos.layer.Layer):
    def __init__(self, display_size, turn_info, assets):
        super().__init__()
        self.display = display_size
        self.info = turn_info
        self.images = assets

        rates = -1
        # Check the rate
        try:
            for key, item in self.info['rates'].items():
                if key is "2":
                    rates = item
        except:
            print("YEET")

        # If the rate is 0, that means the blizzard happened, so draw to screen
        if rates == 0:
            self.blizzard = self.images['blizzard']
            self.blizzard_x = int(self.display[0] / 2)
            self.blizzard_y = int((self.display[1] / 2) + 64)

            self.blizzard.position = (self.blizzard_x, self.blizzard_y)
            self.add(self.blizzard)


class EarthquakeLayer(cocos.layer.Layer):
    def __init__(self, display_size, turn_info, assets):
        super().__init__()
        self.display = display_size
        self.info = turn_info
        self.images = assets

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
            self.earthquake = self.images['earthquake']
            self.earthquake_x = int(self.display[0] / 2)
            self.earthquake_y = 104

            self.earthquake.position = (self.earthquake_x, self.earthquake_y)
            self.add(self.earthquake)


class MonsterLayer(cocos.layer.Layer):
    def __init__(self, display_size, turn_info, assets):
        super().__init__()
        self.display = display_size
        self.info = turn_info
        self.images = assets

        global_stats = GlobalStats()

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
            self.monster = self.images['monster']
            self.monster_x = int(self.display[0] / 4)
            self.monster_y = int(self.display[1])

            self.monster.position = (self.monster_x, self.monster_y)
            self.monster.do(MoveBy((self.monster_x, -400), global_stats.disaster_turn_time * global_stats.turn_speed))

            self.add(self.monster)


class UFOLayer(cocos.layer.Layer):
    def __init__(self, display_size, turn_info, assets):
        super().__init__()
        self.display = display_size
        self.info = turn_info
        self.images = assets

        global_stats = GlobalStats()

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
            self.ufo = self.images['ufo']
            self.ufo_x = self.display[0]/2
            self.ufo_y = 400
            self.ufo.position = (self.ufo_x, self.ufo_y)
            # self.ufo.do(MoveBy((self.display[0], 0), global_stats.disaster_turn_time * global_stats.turn_speed))

            self.add(self.ufo)


class LastingDisasterLayer(cocos.layer.Layer):
    def __init__(self, display_size, turn_info, assets):
        super().__init__()
        self.display = display_size
        self.info = turn_info
        self.images = assets

        fire_count = 0
        bliz_count = 0
        monst_count = 0

        num_dis = len(self.info['player']['disasters'])
        # Visualize when there is a lasting fire disaster
        if num_dis > 0:
            for i in range(num_dis):
                if self.info['player']['disasters'][i]['disaster_type'] == 0:

                    self.fire_spr = self.images['fire_tracker']
                    self.fire_spr.position = 730, 32
                    self.add(self.fire_spr)
                    fire_count += 1
                    self.fire_count_label = cocos.text.Label(
                        f"x {fire_count}",
                        font_name="Comic Sans",
                        font_size=24,
                        bold=True,
                        anchor_x="center",
                        position=(794, 32)
                    )

                elif self.info['player']['disasters'][i]['disaster_type'] == 2:
                    # Visualize when there is a lasting fire disaster
                    self.blizz_spr = self.images['bliz_tracker']
                    self.blizz_spr.position = 858, 32
                    self.add(self.blizz_spr)

                    bliz_count += 1
                    self.bliz_count_label = cocos.text.Label(
                        f"x {bliz_count}",
                        font_name="Comic Sans",
                        font_size=24,
                        bold=True,
                        anchor_x="center",
                        position=(922, 32)
                    )

                elif self.info['player']['disasters'][i]['disaster_type'] == 4:
                    # Visualize when there is a lasting fire disaster
                    self.monst_spr = self.images['monst_tracker']
                    self.monst_spr.position = 986, 32
                    self.add(self.monst_spr)

                    monst_count += 1
                    self.monst_count_label = cocos.text.Label(
                        f"x {monst_count}",
                        font_name="Comic Sans",
                        bold=True,
                        font_size=24,
                        anchor_x="center",
                        position=(1050, 32)
                    )
            try:
                self.add(self.fire_count_label)
            except:
                pass
            try:
                self.add(self.bliz_count_label)
            except:
                pass
            try:
                self.add(self.monst_count_label)
            except:
                pass



