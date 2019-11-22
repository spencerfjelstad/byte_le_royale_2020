from game.controllers.controller import Controller


class WealthController(Controller):
    def __init__(self):
        super().__init__()


    def update(self,player):
        city = player.city
        city.gold += 1



