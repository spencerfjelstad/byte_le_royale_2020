from game.common.buildings.building import Building
from game.common.enums import BuildingLevel, BuildingType
from game.common.stats import GameStats


# Boosts the effectiveness of decrees for lasting disasters
class LastingDecreeBooster(Building):
    def __init__(self):
        super().__init__()
        self.building_type = BuildingType.lasting_decree_booster
        self.booster = GameStats.decree_boost[self.building_level]
        self.effort_remaining = GameStats.building_effort[BuildingLevel.level_one]

    def to_json(self):
        data = super().to_json()

        data["building_type"] = self.building_type
        data["booster"] = self.booster
        data["effort_remaining"] = self.effort_remaining

        return data

    def from_json(self, data):
        super().from_json(data)

        self.building_type = data["building_type"]
        self.booster = data["booster"]
        self.effort_remaining = data["effort_remaining"]
