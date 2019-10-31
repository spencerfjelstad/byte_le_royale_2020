from game.controllers.controller import Controller
from game.common.disasters.lasting_disaster import LastingDisaster
from game.common.enums import *
from game.common.stats import GameStats


class DecreeController(Controller):
    DECREE_DISASTER_MAPPINGS = {
        DecreeType.anti_fire_bears: DisasterType.fire,
        DecreeType.paperweights: DisasterType.tornado,
        DecreeType.hound_news: DisasterType.hurricane,
        DecreeType.moon_shoes: DisasterType.earthquake,
        DecreeType.away_spray: DisasterType.monster,
        DecreeType.giant_fly_swatter: DisasterType.ufo
    }

    def __init__(self):
        super().__init__()
        self.client_decree = None
        self.debug = False

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
                # Retrieve booster from the city's decree booster building
                if isinstance(disaster, LastingDisaster):
                    booster = player.city.buildings[BuildingType.lasting_decree_booster].booster
                else:
                    booster = player.city.buildings[BuildingType.instant_decree_booster].booster

                # Calculate decree effect, given default decree effect with the extra boost from the building booster
                decree_pop_effect = min(0, GameStats.decree_population_effect - GameStats.decree_population_effect * booster)
                decree_struct_effect = min(0, GameStats.decree_structure_effect - GameStats.decree_structure_effect * booster)

                self.print(f"reducing damage on disaster {disaster}...")
                self.print(f"Before: pop = {disaster.population_damage}, struct = {disaster.structure_damage}")

                # apply
                disaster.population_damage = disaster.population_damage * decree_pop_effect
                disaster.structure_damage = disaster.structure_damage * decree_struct_effect

                self.print(f"After: pop = {disaster.population_damage}, struct = {disaster.structure_damage}")
