from game.controllers.controller import Controller
from game.common.stats import GameStats
from game.common.enums import *
from game.utils.helpers import clamp


class AccumulativeController(Controller):
    def __init__(self):
        super().__init__()

    def update(self, player):
        city = player.city

        # Everything boosted - Wealth
        building_level = city.buildings[BuildingType.everything_booster].level
        booster = GameStats.everything_boost['wealth'][building_level]
        self.print(f"Everything: Wealth to add: {booster}")
        city.gold += booster

        # Everything boosted - Structure
        booster = GameStats.everything_boost['structure'][building_level]
        self.print(f"Everything: Structure to add: {booster}")
        city.structure += booster
        # Clamped to max_structure
        city.structure = clamp(city.structure, max_value=city.max_structure)

        # Everything boosted - Population
        booster = GameStats.everything_boost['population'][building_level]
        self.print(f"Everything: Population to add: {booster}")
        city.population += booster

        # Clamped to structure
        city.population = clamp(city.population, max_value=city.structure)

        # Wealth boosted
        building_level = city.buildings[BuildingType.wealth_booster].level
        booster = GameStats.wealth_boost[building_level]

        self.print(f"Gold to add: {booster} plus normal accumulative gold: {GameStats.city_gold_accumulative}")
        # Adding the boost from the side structure
        city.gold += booster

        # Structure boosted
        building_level = city.buildings[BuildingType.structure_booster].level
        structure_added = GameStats.structure_boost[building_level]

        self.print(f"Structure to add: {structure_added}")

        city.structure += structure_added
        # Clamped to max_structure
        city.structure = clamp(city.structure, max_value=city.max_structure)
        self.print(f"Final structure: {city.structure}")

        # Population boosted
        building_level = city.buildings[BuildingType.population_booster].level
        population_added = GameStats.population_boost[building_level]

        self.print(f"Population to add: {population_added}")

        city.population += population_added
        # Clamped to structure
        city.population = clamp(city.population, max_value=city.structure)
        self.print(f"Final population: {city.population}")

        # Normal accumulation of gold
        city.gold += GameStats.city_gold_accumulative

