import os
import sys
import importlib
from tqdm import tqdm
from multiprocessing.dummy import Pool as ThreadPool

from common.client import *


def main():
    loop(1000)


def loop(max_turns):
    clients = boot()
    if len(clients) <= 0:
        print("No clients found")
        exit()

    for turn in tqdm(range(1, max_turns + 1)):
        turn += 1

        pre_tick()
        tick(clients)
        post_tick()

    print("Game reached max turns and is closing.")


def boot():
    clients = list()
    for filename in os.listdir('game/clients'):
        filename = filename.replace('.py', '')
        if filename in ['__init__', '__pycache__']:
            continue
        player = Client(
           importlib.import_module('clients.'+filename),
           1
        )
        clients.append(player)

    return clients


def pre_tick():
    pass


def tick(clients):
    #pool = ThreadPool(len(clients))
    #pool.map(lambda x: x.code.take_turn(), clients)
    #pool.close()
    for client in clients:
        client.code.take_turn()


def post_tick():
    pass


if __name__ == '__main__':
    main()
