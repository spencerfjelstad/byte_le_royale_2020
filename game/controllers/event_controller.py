from game.controllers.singleton_controller import SingletonController


class EventController(SingletonController):
    EVENT_REQ = {
        "event_type",
    }

    def __init__(self):
        super().__init__()
        self.debug = False
        self.__events = list()  # list instead of set here, because set cannot be converted to JSON
        self.turn = None

    def add_event(self, log):
        for req in EventController.EVENT_REQ:
            if req not in log:
                self.print(f"attempted to log an event without requirement '{req}'.")
                return

        if "turn" not in log:
            log["turn"] = self.turn
        else:
            self.print(f"WARNING: turn number found in event before the event was added to event controller. "
                       f"Was this intentional?")

        self.__events.append(log)

    def get_events(self):
        return self.__events

    def update(self, turn):
        self.turn = turn
