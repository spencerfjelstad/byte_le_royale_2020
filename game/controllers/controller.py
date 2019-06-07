from abc import ABC, abstractmethod


class Controller(ABC):
    debug = False

    @classmethod
    def log(cls, message):
        if cls.debug is True:
            print(message)
