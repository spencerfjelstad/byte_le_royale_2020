import os
import sys
import importlib
import json
from tqdm import tqdm
from multiprocessing.dummy import Pool as ThreadPool

from game.common.client import *


def main():
    loop()


def loop():
    clients = boot()
    if len(clients) <= 0:
        print("No clients found")
        exit()
        
    world = load()
    max_turns = len(world)

    for turn in tqdm(range(1, max_turns + 1)):
        pre_tick()
        tick(world[str(turn)], clients)
        post_tick()

    print("Game reached max turns and is closing.")


def boot():
    clients = list()
    for filename in os.listdir('game/clients/'):
        filename = filename.replace('.py', '')
        if filename in ['__init__', '__pycache__']:
            continue
        player = Client(
           importlib.import_module('game.clients.' + filename),
           1
        )
        clients.append(player)

    return clients
    

def load():
    if not os.path.exists('logs/'):
        raise FileNotFoundError('Log directory not found')
        
    if not os.path.exists('logs/game_map.json'):
        raise FileNotFoundError('Game map not found. This is likely because it has not been generated.')
        
    world = None
    with open('logs/game_map.json') as json_file:
        world = json.load(json_file)
    return world 


def pre_tick():
    pass


def tick(world, clients):
    #pool = ThreadPool(len(clients))
    #pool.map(lambda x: x.code.take_turn(), clients)
    #pool.close()
    print(world['rates'])
    for client in clients:
        client.code.take_turn()
        


def post_tick():
    pass


if __name__ == '__main__':
    main()
