import uuid

from game.common.enums import *


class Player:
    def __init__(self, code=None, team_name=None, city=None):
        self.id = str(uuid.uuid4())
        self.team_name = team_name
        self.code = code
        self.city = city
        self.object_type = ObjectType.player

    def to_json(self):
        data = dict()

        data['id'] = self.id
        data['team_name'] = self.team_name
        data['city'] = self.city
        data['object_type'] = self.object_type

        return data

    def from_json(self, data):
        self.id = data['id']
        self.team_name = data['team_name']
        self.city = data['city']
        self.object_type = data['object_type']
