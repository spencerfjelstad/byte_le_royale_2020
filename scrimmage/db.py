import time
import json
import os

from scrimmage.utilities import Thread


class DB:
    def __init__(self):
        self.data = None
        if not os.path.exists('db.json'):
            self.data = list()
        else:
            with open('db.json', 'r') as f:
                self.data = json.load(f)
                print(self.data)

        self.lock = False

        self.save_thread = Thread(self.live_saving, ())
        self.save_thread.start()

    def add_entry(self, tid=None, teamname=None, vis_logs=None, code_file=None):
        entry = {
            'tid': tid,
            'teamname': teamname,
            'vis_logs': vis_logs,
            'code_file': code_file,
            'submissions': 0,
        }

        if not os.path.exists(teamname):
            os.mkdir(teamname)

        self.data.append(entry)

    def query(self, tid=None, teamname=None):
        self.await_lock()

        results = list()
        for entry in self.data:
            if tid is not None and entry['tid'] != tid:
                continue
            if teamname is not None and entry['teamname'] != teamname:
                continue

            results.append(entry)

        self.lock = False
        return results

    def dump(self):
        self.await_lock()

        self.lock = False
        return self.data

    def await_lock(self):
        while self.lock:
            time.sleep(1)
        self.lock = True

    def live_saving(self):
        while True:
            time.sleep(5)

            self.await_lock()
            with open('db.json', 'w+') as f:
                json.dump(self.data, f)

            self.lock = False
