import uuid

from game.common.game_object import GameObject
from game.common.enums import *
from game.utils.helpers import enum_to_string


class Disaster(GameObject):
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.status = DisasterStatus.dead
        self.type = None
        self.population_damage = None
        self.structure_damage = None
        self.object_type = ObjectType.disaster

    def destroy(self):
        self.status = DisasterStatus.dead

    def to_json(self):
        data = dict()
        data["id"] = self.id
        data["status"] = self.status
        data["disaster_type"] = self.type
        data["population_damage"] = self.population_damage
        data["structure_damage"] = self.structure_damage
        data["object_type"] = self.object_type

        return data

    def from_json(self, data):
        self.id = data["id"]
        self.status = data["status"]
        self.type = data["disaster_type"]
        self.population_damage = data["population_damage"]
        self.structure_damage = data["structure_damage"]
        self.object_type = data["object_type"]

    def __str__(self):
        p = f"""Disaster Status: {self.status}
            Disaster Type: {enum_to_string(DisasterType,self.type).replace("_", " ")}
            Disaster Population Damage: {self.population_damage}
            Disaster Structure Damage: {self.structure_damage}
            Disaster Object Type: {self.object_type}
            """
        return p


