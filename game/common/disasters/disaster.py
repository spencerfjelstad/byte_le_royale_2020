from game.common.enums import *


class Disaster:
    def __init__(self):
        self.status = DisasterStatus.dead
        self.type = None
        self.population_damage = None
        self.structure_damage = None
        self.object_type = ObjectType.disaster

    def destroy(self):
        self.status = DisasterStatus.dead

    def to_json(self):
        data = dict()

        data["status"] = self.status
        data["disaster_type"] = self.type
        data["population_damage"] = self.population_damage
        data["structure_damage"] = self.structure_damage
        data["object_type"] = self.object_type

        return data

    def from_json(self, data):
        self.status = data["status"]
        self.type = data["disaster_type"]
        self.population_damage = data["population_damage"]
        self.structure_damage = data["structure_damage"]
        self.object_type = data["object_type"]

    def __str__(self):
        p = f"""Disaster Status: {self.status}
            Disaster Type: {self.type}
            Disaster Population Damage: {self.population_damage}
            Disaster Structure Damage: {self.structure_damage}
            Disaster Object Type: {self.object_type}
            """
        return p


