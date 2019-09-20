from game.controllers.controller import Controller


class SingletonController(Controller):
    _instance = None

    def __init__(self):
        super().__init__()

        if self.__class__._instance is not None:
            print(f"{self.__class__.__name__} is a singleton and has already been instantiated. "
                  f"Use {self.__class__.__name__}.get_instance() to get instance of the class.")
        else:
            self.__class__._instance = self

    @classmethod
    def get_instance(cls):
        return cls._instance
