from game.common.enums import ObjectType, BuildingLevel


# Side buildings that can be upgraded to provide various effects
class Building:
    def __init__(self):
        self.building_type = None
        self.object_type = ObjectType.building
        self.level = BuildingLevel.level_zero
        self.effort_remaining = 0

    def to_json(self):
        data = dict()

        data["building_type"] = self.building_type
        data["object_type"] = self.object_type
        data["level"] = self.level
        data["effort_remaining"] = self.effort_remaining

        return data

    def from_json(self, data):
        self.building_type = data["building_type"]
        self.object_type = data["object_type"]
        self.level = data["level"]
        self.effort_remaining = data["effort_remaining"]
