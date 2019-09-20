from game.controllers.singleton_controller import SingletonController


class EventController(SingletonController):
    EVENT_REQ = {
        "type",
        "turn",
    }

    def __init__(self):
        super().__init__()
        self.debug = False
        self.events = list()

    def add_event(self, log):
        for req in EventController.EVENT_REQ:
            if req not in log:
                print(f"attempted to log an event without requirement '{req}'.")
                return

        self.events.append(log)
