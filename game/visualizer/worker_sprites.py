import math
import random

import cocos

from game.common.enums import *


class WorkerLayer(cocos.layer.Layer):
    def __init__(self, turn, display_size, parser, assets):
        self.size = display_size
        self.images = assets
        super().__init__()
        self.batch = cocos.batch.BatchNode()
        self.add(self.batch)
        info = parser.get_turn(turn)

        total_effort_expended = 0

        for item, amount in info['player']['action']['effort']:
            x = 0
            y = 0
            max_x = 0
            max_y = 0
            image = None
            total_effort_expended += amount
            count = math.floor((amount * (20 / 350)))

            if item is ActionType.repair_structure:
                image = 'hammer'
                x = 952
                y = 181
                max_x = 1059
                max_y = 221
            elif item is ActionType.regain_population:
                image = 'phone'
                x = 1114
                y = 122
                max_x = 1276
                max_y = 132
            elif item is ActionType.accumulate_wealth:
                image = 'money'
                x = 378
                y = 121
                max_x = 474
                max_y = 133
            elif item is ActionType.upgrade_city:
                image = 'pick'
                x = 949
                y = 144
                max_x = 1103
                max_y = 167
            elif 'object_type' in item and item['object_type'] is ObjectType.sensor:
                image = 'pick'
                if item['sensor_type'] is SensorType.fire:
                    x = 1212
                    y = 436
                    max_x = 1244
                    max_y = 444
                elif item['sensor_type'] is SensorType.tornado:
                    x = 980
                    y = 441
                    max_x = 1012
                    max_y = 447
                elif item['sensor_type'] is SensorType.blizzard:
                    x = 733
                    y = 521
                    max_x = 764
                    max_y = 539
                elif item['sensor_type'] is SensorType.earthquake:
                    x = 201
                    y = 392
                    max_x = 236
                    max_y = 400
                elif item['sensor_type'] is SensorType.monster:
                    x = 514
                    y = 394
                    max_x = 548
                    max_y = 405
                elif item['sensor_type'] is SensorType.ufo:
                    x = 26
                    y = 309
                    max_x = 61
                    max_y = 316
            elif 'object_type' in item and item['object_type'] is ObjectType.disaster:
                image = 'hammer'
                if item['disaster_type'] is DisasterType.fire:
                    x = 621
                    y = 356
                    max_x = 758
                    max_y = 504
                elif item['disaster_type'] is DisasterType.blizzard:
                    x = 917
                    y = 632
                    max_x = 1186
                    max_y = 708
                elif item['disaster_type'] is DisasterType.monster:
                    x = 404
                    y = 441
                    max_x = 508
                    max_y = 498
            elif 'object_type' in item and item['object_type'] is ObjectType.building:
                image = 'hammer'
                if item['building_type'] is BuildingType.printer:
                    x = 51
                    y = 148
                    max_x = 175
                    max_y = 222
                elif item['building_type'] is BuildingType.big_canoe:
                    x = 578
                    y = 295
                    max_x = 874
                    max_y = 309
                elif item['building_type'] is BuildingType.gelato_shop:
                    x = 520
                    y = 146
                    max_x = 566
                    max_y = 158
                elif item['building_type'] is BuildingType.billboard:
                    x = 1173
                    y = 226
                    max_x = 1276
                    max_y = 307
                elif item['building_type'] is BuildingType.mint:
                    x = 381
                    y = 145
                    max_x = 497
                    max_y = 160
                elif item['building_type'] is BuildingType.police_station:
                    x = 226
                    y = 145
                    max_x = 335
                    max_y = 160

            self.add_worker(x, y, max_x, max_y, image, count)

        # Add 1:1 to max of 20 dancing rooftop pedestrians who should probably be doing something else but aren't
        if total_effort_expended < info['player']['city']['population']:
            self.add_worker(
                350,
                617,
                406,
                620,
                'normal',
                min(info['player']['city']['population'] - total_effort_expended, 20)
            )

    def add_worker(self, x, y, max_x, max_y, image, count):
        if image is None:
            return

        for n in range(count):
            worker = self.images[image].pop(0)
            self.images[image].append(worker)
            real_x = random.randint(x, max_x)
            real_y = random.randint(y, max_y)

            # Fit sprite within pixel scale
            real_x -= real_x % 4
            real_y -= real_y % 4
            worker.position = (real_x, real_y)

            # Flip workers to look towards the center of their spawnable range
            if max_x - real_x < (max_x - x) / 2:
                worker.scale_x = -1
            else:
                worker.scale_x = 1

            self.batch.add(worker)
