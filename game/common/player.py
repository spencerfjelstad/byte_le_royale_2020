import uuid

from game.common.enums import *
from game.common.city import City
from game.common.action import Action
from game.common.disasters import *


class Player:
    def __init__(self, code=None, team_name=None, city=None, action=None, disasters=[]):
        self.id = str(uuid.uuid4())
        self.team_name = team_name
        self.code = code
        self.city = city
        self.action = action
        self.disasters = disasters
        self.object_type = ObjectType.player

    def to_json(self):
        data = dict()

        data['id'] = self.id
        data['team_name'] = self.team_name
        data['city'] = self.city.to_json()
        data['action'] = self.action.to_json()
        data['disasters'] = [dis.to_json() for dis in self.disasters]
        data['object_type'] = self.object_type

        return data

    def from_json(self, data):
        self.id = data['id']
        self.team_name = data['team_name']
        cit = City()
        self.city = cit.from_json(data['city'])
        act = Action()
        self.action = act.from_json(data['action'])
        self.disasters = []
        for dis in data['disasters']:
            dis_type = dis['type']
            obj = None
            if dis_type == DisasterType.earthquake:
                obj = Earthquake()
            elif dis_type == DisasterType.fire:
                obj = Fire()
            elif dis_type == DisasterType.hurricane:
                obj = Hurricane()
            elif dis_type == DisasterType.monster:
                obj = Monster()
            elif dis_type == DisasterType.tornado:
                obj = Tornado()
            elif dis_type == DisasterType.ufo:
                obj = Ufo()
            obj.from_json(dis)
            self.disasters.append(obj)
        self.object_type = data['object_type']


    def __str__(self):
        p = f"""ID: {self.id}
            Team name: {self.team_name}
            City: {self.city}
            Action: {self.action}
            Disasters: {self.disasters}
            """
        return p