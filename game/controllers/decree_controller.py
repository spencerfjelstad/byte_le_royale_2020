from game.controllers.controller import Controller
from game.controllers.fun_stat_controller import FunStatController
from game.common.disasters.lasting_disaster import LastingDisaster
from game.common.enums import *
from game.common.stats import GameStats
from game.utils.helpers import clamp


class DecreeController(Controller):
    DECREE_DISASTER_MAPPINGS = {
        DecreeType.anti_fire_dogs: DisasterType.fire,
        DecreeType.paperweights: DisasterType.tornado,
        DecreeType.snow_shovels: DisasterType.blizzard,
        DecreeType.rubber_boots: DisasterType.earthquake,
        DecreeType.fishing_hook: DisasterType.monster,
        DecreeType.cheese: DisasterType.ufo
    }

    def __init__(self):
        super().__init__()
        self.client_decree = None

        self.fun_stat_controller = FunStatController.get_instance()

    def update_decree(self, decree):
        self.client_decree = decree

    def execute_decree(self, player):
        if self.client_decree is None:
            return

        for disaster in player.disasters:
            if isinstance(disaster, LastingDisaster) and not disaster.newly_spawned:
                # Ignore, decrees shouldn't effect old disasters
                continue

            if disaster.type == DecreeController.DECREE_DISASTER_MAPPINGS.get(self.client_decree):
                self.fun_stat_controller.disasters_correctly_protected += 1

                # Retrieve booster from the city's decree booster building
                if isinstance(disaster, LastingDisaster):
                    building_level = player.city.buildings[BuildingType.lasting_decree_booster].level
                    booster = GameStats.decree_boost[building_level]

                    decree_effort_effect = clamp(GameStats.decree_population_effect * booster, min_value=0, max_value=1)

                    self.print(f"Reducing effort required on disaster {disaster}...")
                    self.print(f"Before: {disaster.effort_remaining}")

                    disaster.effort_remaining = clamp(int(disaster.effort_remaining * (1 - decree_effort_effect)), min_value=1)

                    self.print(f"After: {disaster.effort_remaining}")
                else:
                    building_level = player.city.buildings[BuildingType.instant_decree_booster].level
                    booster = GameStats.decree_boost[building_level]

                    # Calculate decree effect, given default decree effect with the extra boost from the building booster
                    decree_pop_effect = clamp(GameStats.decree_population_effect * booster, min_value=0, max_value=1)
                    decree_struct_effect = clamp(GameStats.decree_structure_effect * booster, min_value=0, max_value=1)

                    self.print(f"reducing damage on disaster {disaster}...")
                    self.print(f"Before: pop = {disaster.population_damage}, struct = {disaster.structure_damage}")
                    # apply
                    disaster.population_damage = clamp(int(disaster.population_damage*(1-decree_pop_effect)), min_value=1)
                    disaster.structure_damage = clamp(int(disaster.structure_damage*(1-decree_struct_effect)), min_value=1)

                    self.print(f"After: pop = {disaster.population_damage}, struct = {disaster.structure_damage}")
