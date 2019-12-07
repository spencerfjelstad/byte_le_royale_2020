from game.common.game_object import GameObject
from game.common.enums import *
from game.common.stats import *
from game.utils.helpers import enum_to_string


class Sensor(GameObject):
    def __init__(self):
        self.sensor_type = None
        self.object_type = ObjectType.sensor
        self.level = SensorLevel.level_zero
        self.effort_remaining = GameStats.sensor_effort[SensorLevel.level_one]
        self.sensor_results = None

    def to_json(self):
        data = dict()

        data['sensor_type'] = self.sensor_type
        data['object_type'] = self.object_type
        data['level'] = self.level
        data['effort_remaining'] = self.effort_remaining
        data['sensor_results'] = self.sensor_results
        return data

    def from_json(self, data):
        self.sensor_type = data['sensor_type']
        self.object_type = data['object_type']
        self.level = data['level']
        self.effort_remaining = data['effort_remaining']
        self.sensor_results = data['sensor_results']

    def __str__(self):
        p = f"""Sensor Type: {enum_to_string(SensorType,self.sensor_type).replace("_", " ")}
            Sensor Level: {self.level}
            Sensor Effort Remaining: {self.effort_remaining}
            Sensor Results: {self.sensor_results}
            """
        return p
