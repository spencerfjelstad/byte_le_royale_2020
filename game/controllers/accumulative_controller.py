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
        building_level = player.city.buildings[BuildingType.wealth_booster].building_level
        booster = GameStats.wealth_boost[building_level]

        gold_added = booster
        self.print(f"Gold to add: {gold_added}")

        city.gold += gold_added

        # Structure
        building_level = player.city.buildings[BuildingType.structure_booster].building_level
        structure_added = GameStats.structure_boost[building_level]

        self.print(f"Structure to add: {structure_added}")

        player.city.structure += structure_added
        #Clamped to max_structure
        player.city.structure = clamp(player.city.structure, max_value=player.city.max_structure)
        self.print(f"Final structure: {player.city.structure}")

        #Population
        building_level = player.city.buildings[BuildingType.population_booster].building_level
        population_added = GameStats.population_boost[building_level]

        self.print(f"Population to add: {population_added}")

        player.city.population += population_added
        #Clamped to structure
        player.city.population = clamp(player.city.population, max_value=player.city.structure)
        self.print(f"Final population: {player.city.population}")

