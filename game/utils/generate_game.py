import json
import random
import time
import os

from game.config import *
from game.utils.helpers import *


def generate():
    print('generating map please wait :)')
    time.sleep(1)
    total = {}
    
    act = 0
    
    rates = {
        DisasterType.fire : 0.0,
        DisasterType.tornado : 0.0,
        DisasterType.hurricane : 0.0,
        DisasterType.earthquake : 0.0,
        DisasterType.monster : 0.0,
        DisasterType.ufo : 0.0,
    }
    
    for x in range(1, MAX_TURNS + 1):
        activations = []
        
        if x > STARTING_FREE_TURNS:  
            for key,item in rates.items():
                rates[key] += random.random() * INDIVIDUAL_WEIGHTS[key]
                rates[key] = min(rates[key], 1.0)
                if rates[key] == 1.0 or decision(rates[key]):
                    activations.append(key)
                    rates[key] = 0
                    INDIVIDUAL_WEIGHTS[key] *= ACTIVATION_DEPRECIATION_RATE
                    act += 1
                
                INDIVIDUAL_WEIGHTS[key] += DISASTER_CHANCE_GROWTH_RATE * random.random() * INDIVIDUAL_WEIGHTS[key]
            
        #os.system('cls')
        #print(f'Turn {x}')
        #print_dict(rates, "Current turn odds")
        #print_dict(INDIVIDUAL_WEIGHTS, "Current weights")
        #print(*activations)
        #print(f'activations: {act}')
        
        total[x] = {'data': {'rates': rates, 'disasters': activations}}
        
    write(total)


def print_dict(dict, name='dict'):
    res = name + '\n'
    for key, item in dict.items():
        res += (f'{key}: {item}\n')
        
    print(res)


def write(dict):
    if not os.path.exists('logs'):
        os.makedirs('logs')
    
    with open('logs/game_map.json', 'w+') as out:
        json.dump(dict, out)
