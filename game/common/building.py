from game.common.game_object import GameObject
from game.common.enums import ObjectType, BuildingLevel, BuildingType
from game.utils.helpers import enum_to_string


# Side buildings that can be upgraded to provide various effects
class Building(GameObject):
    def __init__(self, building_type=None):
        super().__init__()
        self.building_type = building_type
        self.object_type = ObjectType.building
        self.level = BuildingLevel.level_zero
        self.effort_remaining = 0

    def to_json(self):
        data = super().to_json()

        data["building_type"] = self.building_type
        data["object_type"] = self.object_type
        data["level"] = self.level
        data["effort_remaining"] = self.effort_remaining

        return data

    def from_json(self, data):
        super().from_json(data)
        self.building_type = data["building_type"]
        self.object_type = data["object_type"]
        self.level = data["level"]
        self.effort_remaining = data["effort_remaining"]

    def __str__(self):
        return f"""Building Type: {enum_to_string(BuildingType, self.building_type).replace("_", " ")}
            Building Level: {self.level}
            Building Effort Remaining: {self.effort_remaining}
            Building Object Type: {self.object_type}
            """
