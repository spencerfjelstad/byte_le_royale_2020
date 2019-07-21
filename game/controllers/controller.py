
class Controller:

    def __init__(self):
        self.debug = False

    def log(self, message):
        if self.debug is True:
            print(message)
