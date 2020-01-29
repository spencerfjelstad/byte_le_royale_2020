from game.controllers.singleton_controller import SingletonController


class FunStatController(SingletonController):
    def __init__(self):
        super().__init__()
        self.debug = False

        # Stats for decree correctness ratio
        self.total_disasters = 0
        self.disasters_correctly_protected = 0

        # Stats for average population
        self.total_population_ever = 0

        # Stats for average structure
        self.total_structure_ever = 0

        # Stats for effort successfully allocated
        self.total_effort_applied = 0
        self.effort_correctly_applied = 0

        # Stats for damage taken
        self.total_population_damage = 0
        self.total_structure_damage = 0

    def export(self):
        stats = dict()

        stats['total_disasters'] = self.total_disasters
        stats['disasters_correctly_protected'] = self.disasters_correctly_protected

        stats['total_population_ever'] = self.total_population_ever

        stats['total_structure_ever'] = self.total_structure_ever

        stats['total_effort_applied'] = self.total_effort_applied
        stats['effort_correctly_applied'] = self.effort_correctly_applied

        stats['total_population_damage'] = self.total_population_damage
        stats['total_structure_damage'] = self.total_structure_damage

        return stats
