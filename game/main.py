import os
import importlib
import json
from tqdm import tqdm

from game.common.player import *
from game.config import *

from game.controllers.master_controller import MasterController

from game.utils.thread import Thread

clients = list()
current_world = None
master_controller = MasterController()
turn_number = 1


def main():
    loop()


def loop():
    global clients
    global master_controller

    boot()
    world = load()

    for turn in tqdm(master_controller.game_loop_logic(), bar_format="Game running at {rate_fmt}", unit=" turns"):
        if len(clients) <= 0:
            print("No clients found")
            exit()

        pre_tick(turn, world)
        tick(turn)
        post_tick(turn)

    print("Game reached max turns and is closing.")


# Gets players established with their objects and such
def boot():
    global clients
    global master_controller

    # Load clients in
    for filename in os.listdir('game/clients/'):
        filename = filename.replace('.py', '')
        if filename in ['__init__', '__pycache__']:
            continue
        im = importlib.import_module(f'game.clients.{filename}')
        obj = im.Client()
        player = Player(
           code=obj
        )
        clients.append(player)

    # Set up player objects

    if SET_NUMBER_OF_CLIENTS == 1:
        master_controller.give_clients_objects(clients[0])
    else:
        master_controller.give_clients_objects(clients)


# Loads all of the results of the generate() functionality into memory
def load():
    if not os.path.exists('logs/'):
        raise FileNotFoundError('Log directory not found.')
        
    if not os.path.exists('logs/game_map.json'):
        raise FileNotFoundError('Game map not found.')

    # Delete previous logs
    [os.remove(f'logs/{path}') for path in os.listdir('logs/') if 'turn' in path]
        
    world = None
    with open('logs/game_map.json') as json_file:
        world = json.load(json_file)
    return world 


# Read from the outlined game map and establish the world given
def pre_tick(turn, world):
    global master_controller
    global current_world

    current_world = world[str(turn)]

    if SET_NUMBER_OF_CLIENTS == 1:
        master_controller.interpret_current_turn_data(clients[0], current_world, turn)
    else:
        master_controller.interpret_current_turn_data(clients, current_world, turn)


# Send client state of the world and a place to put what they want to do
def tick(turn):
    global clients
    global current_world
    global master_controller

    # Create list of threads that run the client's code
    threads = list()
    for client in clients:
        arguments = master_controller.clients_turn_arguments(client, current_world, turn)

        # Create the thread, args being the things the client will need
        thr = Thread(func=client.code.take_turn, args=arguments)
        threads.append(thr)

    # Sets the threads to be daemonic
    def dae(d):
        d.daemon = True

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
            print(f'{client.id} failed to reply in time and has been dropped')

    # Apply bulk of game logic
    if SET_NUMBER_OF_CLIENTS == 1:
        master_controller.turn_logic(clients[0], current_world, turn)
    else:
        master_controller.turn_logic(clients, current_world, turn)


# Create log of the turn and end the game if necessary
def post_tick(turn):
    global clients
    global current_world
    global master_controller

    # Write turn results to log file
    data = None
    if SET_NUMBER_OF_CLIENTS == 1:
        data = master_controller.create_turn_log(clients[0], current_world, turn)
    else:
        data = master_controller.create_turn_log(clients, current_world, turn)

    global turn_number
    with open(f"logs/turn_{turn_number:04d}.json", 'w+') as f:
        json.dump(data, f)
    turn_number += 1

    # Check if game has ended
    if master_controller.game_over_check():
        # Game is over, create the results file and end the game
        print("\nGame has ended.")
        exit()


if __name__ == '__main__':
    main()
