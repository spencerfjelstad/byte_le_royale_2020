from abc import ABC, abstractmethod


class Controller(ABC):

    @abstractmethod
    def __init__(self):
        self.debug = False

    def log(self, message):
        if self.debug is True:
            print(message)
