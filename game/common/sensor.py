from game.common.enums import *
from game.common.stats import *

class Sensor:
    def __init__(self):
        self.sensor_type = None
        self.object_type = ObjectType.sensor
        self.sensor_level = SensorLevel.level_one

    #Keeps track of the current progress of the amount of effort needed to completely build the sensor
    def effort_progress(self, effort, sensor_type):
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