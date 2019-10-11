import threading
from game.config import Debug, DebugLevel
from game.utils.secure_importer import secure_importer


class Thread(threading.Thread):
    def __init__(self, func, args):
        threading.Thread.__init__(self)
        self.args = args
        self.func = func

    def run(self):
        self.func(*self.args)


# Thread in control of running a client's turn function
def client_thread(client, arguments):

    # Apply import restrictions
    __original_importer = __builtins__['__import__']
    __builtins__['__import__'] = secure_importer

    # Try to run client code
    try:
        client.code.take_turn(*arguments)
    except ImportError as e:
        debug(f"ignoring client {client}. Attempted to import restricted module.")
        debug(e)
    except Exception as e:
        debug("client failed turn for unknown reason.")
        debug(e)
    finally:
        # Restore original importer for server use
        __builtins__['__import__'] = __original_importer


# Debug print statement
def debug(*args):
    if Debug.level >= DebugLevel.engine:
        print('Engine: ', end='')
        print(*args)