from game.common.enums import *
from game.common.stats import *


class Sensor:
    def __init__(self):
        self.sensor_type = None
        self.object_type = ObjectType.sensor
        self.sensor_level = SensorLevel.level_zero
        self.sensor_effort_remaining = 0
        self.sensor_results = None

    def to_json(self):
        data = dict()

        data['sensor_type'] = self.sensor_type
        data['object_type'] = self.object_type
        data['sensor_level'] = self.sensor_level
        data['sensor_effort_remaining'] = self.sensor_effort_remaining
        data['sensor_results'] = self.sensor_results
        return data

    def from_json(self, data):
        self.sensor_type = data['sensor_type']
        self.object_type = data['object_type']
        self.sensor_level = data['sensor_level']
        self.sensor_effort_remaining = data['sensor_effort_remaining']
        self.sensor_results = data['sensor_results']
