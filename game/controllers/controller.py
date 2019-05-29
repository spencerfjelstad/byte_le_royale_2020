from abc import ABC, abstractmethod
import warnings


class Controller(ABC):
    __instance = None

    @abstractmethod
    def __init__(self):
        if self.__class__.__instance is None:
            self.__class__.__instance = self
        else:
            warnings.warn("There is already an instance of " + self.__class__.__name__ + ". "
                          "Use " + self.__class__.__name__ + ".get_instance() to get an instance of this class.")

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls()
        return cls.__instance

    @classmethod
    def del_instance(cls):
        cls.__instance = None
