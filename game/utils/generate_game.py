import json
import random
import time

from game.common.config import *


def generate():
    rates = {
        DisasterType.fire : 0.0,
        DisasterType.tornado : 0.0,
        DisasterType.hurricane : 0.0,
        DisasterType.earthquake : 0.0,
        DisasterType.monster : 0.0,
        DisasterType.ufo : 0.0,
    }
    
    for x in range(1, MAX_TURNS + 1):
        if x <= STARTING_FREE_TURNS:
            continue
            
        for key,item in rates.items():
            rates[key] += math.randrange(INDIVIDUAL_WEIGHTS[key])
            INDIVIDUAL_WEIGHTS[key] += DISASTER_CHANCE_GROWTH_RATE * math.randrange(INDIVIDUAL_WEIGHTS[key])
            
        print_dict(rates, "Current turn odds")
        print_dict(INDIVIDUAL_WEIGHTS, "Current weights")
        
        time.sleep(1)


def print_dict(dict, name='dict'):
    res = name + '\n'
    for key, item in dict.items():
        res += (f'{key}: {item}\n')


def write(dict):
    with open('game_map.json', 'w+') as out:
        json.dump(data, out)
