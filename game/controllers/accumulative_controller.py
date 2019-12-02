from game.controllers.controller import Controller
from game.common.stats import GameStats
from game.common.enums import *
from game.utils.helpers import clamp

class AccumulativeController(Controller):
    def __init__(self):
        super().__init__()


    def update(self,player):
        city = player.city

        #Wealth
        building_level = city.buildings[BuildingType.wealth_booster].level
        booster = GameStats.wealth_boost[building_level]

        self.print(f"Gold to add: {booster}")
        #Adding the boost from the side structure and the default gold accumulation
        city.gold += booster + GameStats.city_gold_accumulative

        # Structure
        building_level = city.buildings[BuildingType.structure_booster].level
        structure_added = GameStats.structure_boost[building_level]

        self.print(f"Structure to add: {structure_added}")

        city.structure += structure_added
        #Clamped to max_structure
        city.structure = clamp(city.structure, max_value=city.max_structure)
        self.print(f"Final structure: {city.structure}")

        #Population
        building_level = city.buildings[BuildingType.population_booster].level
        population_added = GameStats.population_boost[building_level]

        self.print(f"Population to add: {population_added}")

        city.population += population_added
        #Clamped to structure
        city.population = clamp(city.population, max_value=city.structure)
        self.print(f"Final population: {city.population}")

