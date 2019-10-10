import threading


class Thread(threading.Thread):
    def __init__(self, func, args):
        threading.Thread.__init__(self)
        self.args = args
        self.func = func

    def run(self):
        self.func(*self.args)
