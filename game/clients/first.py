
class Client:
    # Variables and info you want to save between turns go here
    def __init__(self):
        self.number = 100

    # This is where your AI will decide what to do
    def take_turn(self, actions):
        for x in range(self.number):
            pass
        actions.append(self.number)
        self.number += 100

        return 1
