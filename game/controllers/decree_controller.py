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
                self.print(f"reducing damage on disaster {disaster}...")
                self.print(f"Before: pop = {disaster.population_damage}, struct = {disaster.structure_damage}")
                disaster.population_damage = disaster.population_damage * GameStats.decree_population_effect
                disaster.structure_damage = disaster.structure_damage * GameStats.decree_structure_effect
                self.print(f"After: pop = {disaster.population_damage}, struct = {disaster.structure_damage}")
