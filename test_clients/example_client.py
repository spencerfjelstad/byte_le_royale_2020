from game.client.user_client import UserClient
from game.common.enums import *


class Client(UserClient):
    # Variables and info you want to save between turns go here
    def __init__(self):
        super().__init__()
        # ADD VARIABLES BELOW HERE

        self.turn = 0

        # ADD VARIABLES ABOVE HERE

    def team_name(self):
        """
        Allows the team to set a team name. The character limit is 35 characters.
        :return: Your team name
        """
        return "Team Winners"

    def city_name(self):
        """
        Allows the team to name their city. The city name will be displayed on the visualizer.
        The character limit is 50 characters.
        :return:
        """
        return "Winner-opolis"

    def city_type(self):
        """
        Set your city type here! Your city type will give you a benefit at the very start of the game.
        :return:
        """
        return CityType.invested

    # This is where your AI will decide what to do
    def take_turn(self, actions, city, disasters):
        """
        This is where your AI will decide what to do. Add effort allocations towards ActionTypes or objects to
        tell your population what to do. Make sure to set a single decree on your turn!
        :param actions:     This is the actions object that you will add effort allocations or decrees to.
        :param city:        Your city. You can find your sensors, buildings, population, structure, and other info here.
        :param disasters:   Current disasters damaging your city will appear hear. Lasting disasters will appear here
                            until you eliminate them, while instant disasters will only appear for a single turn here.
        """
        self.turn += 1
        self.print(f"Current turn: {self.turn}")

        actions.add_effort(ActionType.regain_population, 10)

        if len(disasters) != 0:
            actions.add_effort(disasters[0], 10)

        actions.set_decree(DecreeType.cheese)
