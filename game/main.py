import os
import sys
import importlib
import json
import time
from tqdm import tqdm
from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing import Process

from game.common.client import *
from game.config import *
from game.utils.thread import Thread


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


# Send client state of the world and a place to put what they want to do
def tick(world, clients):
    #pool = ThreadPool(len(clients))
    #pool.map(lambda x: x.code.take_turn(), clients)
    #pool.close()
    #print(world['rates'])
    action_receipt = {}

    '''Multi-processing method'''
    # processes = [Process(target=client.code.take_turn) for client in clients]
    #
    # def dae(d): d.daemon = True
    # [dae(proc) for proc in processes]
    #
    # [proc.start() for proc in processes]
    #
    # # Wait until the client returns or runs out of time
    # _ = 0
    # while None in [proc.exitcode for proc in processes] and _ < MAX_OPERATIONS_PER_TURN:
    #     _ += 1
    #
    # for x in range(len(processes)):
    #     p = processes[x]
    #     if p.exitcode is None:
    #         p.terminate()
    #         print(f'{clients[x].id} failed to reply in time')

    '''Multi-threading method'''
    threads = [Thread(func=client.code.take_turn) for client in clients]

    def dae(d): d.daemon = True
    [dae(thr) for thr in threads]

    [thr.start() for thr in threads]

    _ = 0
    while True in [thr.is_alive() for thr in threads] and _ < MAX_OPERATIONS_PER_TURN:
        _ += 1

    for x in range(len(threads)):
        thr = threads[x]
        if thr.is_alive():
            print(f'{clients[x].id} failed to reply in time')



def post_tick():
    pass


if __name__ == '__main__':
    main()
