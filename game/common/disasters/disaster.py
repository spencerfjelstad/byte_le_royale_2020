from game.common.game_object import GameObject
from game.common.enums import *
from game.utils.helpers import enum_to_string


class Disaster(GameObject):
    def __init__(self, level=DisasterLevel.level_zero):
        super().__init__()
        self.status = DisasterStatus.dead
        self.type = None
        self.population_damage = None
        self.structure_damage = None
        self.object_type = ObjectType.disaster
        self.level = level

    def destroy(self):
        self.status = DisasterStatus.dead

    def to_json(self):
        data = super().to_json()
        data["id"] = self.id
        data["status"] = self.status
        data["disaster_type"] = self.type
        data["population_damage"] = self.population_damage
        data["structure_damage"] = self.structure_damage
        data["object_type"] = self.object_type
        data["level"] = self.level

        return data

    def from_json(self, data):
        super().from_json(data)
        self.status = data["status"]
        self.type = data["disaster_type"]
        self.population_damage = data["population_damage"]
        self.structure_damage = data["structure_damage"]
        self.object_type = data["object_type"]
        self.level = data["level"]

    def __str__(self):
        p = f"""Disaster Status: {self.status}
            Disaster Type: {enum_to_string(DisasterType,self.type).replace("_", " ")}
            Disaster Level: {self.level}
            Disaster Population Damage: {self.population_damage}
            Disaster Structure Damage: {self.structure_damage}
            Disaster Object Type: {self.object_type}
            """
        return p


