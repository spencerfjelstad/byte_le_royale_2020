import os
import sys
import importlib
import json
import time
from tqdm import tqdm
from multiprocessing import Process

from game.common.player import *
from game.common.action import *
from game.common.disasters import *
from game.common.city import *
from game.config import *

from game.controllers.destruction_controller import DestructionController
from game.controllers.sensor_controller import SensorController

from game.utils.thread import Thread

clients = list()

destructionController = DestructionController()
sensorController = SensorController()

game_over = False


def main():
    loop()


def loop():
    global clients
    boot()
        
    odds = load()
    max_turns = len(odds)

    for turn in tqdm(range(1, max_turns + 1), bar_format="Game running at {rate_fmt}", unit=" turns"):
        if len(clients) <= 0:
            print("No clients found")
            exit()

        current_odds = odds[str(turn)]

        current_odds['rates'] = {int(key): val for key, val in current_odds['rates'].items()}

        pre_tick(turn, current_odds)
        tick(turn, current_odds)
        post_tick(turn, current_odds)

    print("Game reached max turns and is closing.")


# Gets players established with their objects and such
def boot():
    # Load clients in
    global clients
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
    for client in clients:
        client.city = City()
        client.team_name = client.code.team_name()


# Loads all of the results of the generate() functionality into memory
def load():
    if not os.path.exists('logs/'):
        raise FileNotFoundError('Log directory not found.')
        
    if not os.path.exists('logs/game_map.json'):
        raise FileNotFoundError('Game map not found. This is likely because it has not been generated.')

    # Delete previous logs
    [os.remove(f'logs/{path}') for path in os.listdir('logs/') if 'turn' in path]
        
    world = None
    with open('logs/game_map.json') as json_file:
        world = json.load(json_file)
    return world 


# Read from the outlined game map and establish the world given
def pre_tick(turn, odds):
    # Turn disaster notification into a real disaster
    for disaster in odds['disasters']:
        dis = None
        if disaster is DisasterType.earthquake:
            dis = Earthquake()
        elif disaster is DisasterType.fire:
            dis = Fire()
        elif disaster is DisasterType.hurricane:
            dis = Hurricane()
        elif disaster is DisasterType.monster:
            dis = Monster()
        elif disaster is DisasterType.tornado:
            dis = Tornado()
        elif disaster is DisasterType.ufo:
            dis = Ufo()

        if dis is None:
            raise TypeError(f'Attempt to create disaster failed because given type: {disaster}, does not exist.')

        for client in clients:
            client.disasters.append(dis)
    pass

    # Calculate error ranges
    global sensorController
    sensorController.calculate_turn_ranges(turn, odds['rates'])
    sensor_estimates = sensorController.turn_ranges[turn]

    # give clients their corresponding sensor odds
    for client in clients:
        sensor_results = dict()
        for sensor, level in client.city.sensors.items():
            sensor_results[sensor] = sensor_estimates[sensor][level]
        client.city.sensor_results = sensor_results


# Send client state of the world and a place to put what they want to do
def tick(turn, odds):
    take_players_turn()
    apply_turn_logic()


# Send clients their respective world information and receive their turn actions
def take_players_turn():
    global clients

    # Create list of threads that run the client's code
    threads = list()
    for client in clients:
        # This creates a chunk of memory that the client can write to without overwriting other people's actions
        actions = Action()
        client.action = actions

        # Create the thread, args being the things the client will need
        thr = Thread(func=client.code.take_turn, args=(actions, client.city, client.disasters,))
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


# Take the given actions and apply logic through the logic controllers
def apply_turn_logic():
    global clients

    # Set the clients up for logic controller
    player = clients[0]

    # Apply world logic
    global destructionController

    destructionController.handle_actions(player)

    # I  II
    # II IL
    if player.city.population <= 0 or player.city.structure <= 0:
        global game_over
        game_over = True


# Create log of the turn and end the game if necessary
def post_tick(turn, odds):
    global clients

    # Write turn results to log file
    turn_dict = dict()
    turn_dict['rates'] = odds['rates']
    turn_dict['players'] = list()
    for client in clients:
        turn_dict['players'].append(client.to_json())
    with open(f"logs/turn_{turn:04d}.json", 'w+') as f:
        json.dump(turn_dict, f)

    # Check if game has ended
    global game_over
    if game_over:
        # Game is over, create the results file and end the game
        print("\nCity has been defeated. Game has ended.")
        exit()


if __name__ == '__main__':
    main()
