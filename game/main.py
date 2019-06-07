import os
import sys
import importlib
import json
import time
from tqdm import tqdm
from multiprocessing import Process

from game.common.player import *
from game.common.action import *
from game.config import *
from game.controllers import *
from game.utils.thread import Thread


def main():
    loop()


def loop():
    clients = boot()
        
    world = load()
    max_turns = len(world)

    DisasterController.set_log_state(False)
    EconomyController.set_log_state(False)

    for turn in tqdm(range(1, max_turns + 1)):
        if len(clients) <= 0:
            print("No clients found")
            exit()

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
        im = importlib.import_module(f'game.clients.{filename}')
        obj = im.Client()
        player = Player(
           obj,
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
    # Create list of threads that run the client's code
    threads = list()
    for client in clients:
        # This creates a chunk of memory that the client can write to without overwriting other people's actions
        actions = Action()
        action_receipt[client.id] = actions

        # Create the thread, args being the things the client will need
        thr = Thread(func=client.code.take_turn, args=(actions,))
        threads.append(thr)

    # Sets the threads to be daemonic
    def dae(d): d.daemon = True
    [dae(thr) for thr in threads]

    # Start all of the threads. This is where the client's code is actually be run.
    [thr.start() for thr in threads]

    # Boot up a timer in the meantime so the main thread can move on if a client is taking too long.
    # Will move on earlier if all of the threads are finished first.
    _ = 0
    while True in [thr.is_alive() for thr in threads] and _ < MAX_OPERATIONS_PER_TURN:
        _ += 1

    # Go through all the threads and see which ones are still running.
    for client, thr in zip(clients, threads):
        if thr.is_alive():
            clients.remove(client)
            action_receipt.pop(client.id, None)
            print(f'{client.id} failed to reply in time and has been dropped')

    # Process client actions
    for key, item in action_receipt.items():
        print(key)
        res = ''
        for act in item._allocation_list:
            res += f'{act} '
        print(res)


def post_tick():
    pass


if __name__ == '__main__':
    main()
