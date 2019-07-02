from game.common.enums import *
from game.common.stats import *

class Sensor:
    def __init__(self):
        self.sensor_type = None
        self.object_type = ObjectType.sensor
        self.sensor_level = SensorLevel.level_one

    def effort_progress(self, effort):
        pass

    def to_json(self):
        data = dict()

        data['sensor_type'] = self.sensor_type
        data['object_type'] = self.object_type
        data['sensor_level'] = self.sensor_level
        return data

    def from_json(self, data):
        self.sensor_type = data['sensor_type']
        self.object_type = data['object_type']
        self.sensor_level = data['sensor_level']