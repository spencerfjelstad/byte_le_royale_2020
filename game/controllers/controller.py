from abc import ABC, abstractmethod
import sys


class Controller(ABC):
    debug = False

    @classmethod
    def log(cls, message):
        if cls.debug is True:
            print(message)
            sys.stdout.flush()

    @classmethod
    def set_log_status(cls, log_status):
        cls.debug = log_status
