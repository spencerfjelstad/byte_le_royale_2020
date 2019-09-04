import json
import os
from numpy import random as nprandom

from game.config import *
from game.utils.helpers import *


def generate():
    print('generating map please wait :)')

    # Implementation: pre-generate disaster list, generate rates to match
    # Generate basic list disasters will populate
    weight = APPROXIMATE_DISASTER_COUNT / MAX_TURNS
    skeleton_list = nprandom.choice(2, MAX_TURNS, p=[1 - weight, weight])
    skeleton_list = list(skeleton_list)

    # Bias disasters in list in accordance to config
    skeleton_list = bias_list(skeleton_list)

    # Remove disasters from starting buffer zone
    for x, element in enumerate(skeleton_list):
        if x > STARTING_FREE_TURNS:
            break
        if element:
            skeleton_list[x] = 0

    # Generate straight list of disaster order
    disaster_count = sum(skeleton_list)
    disaster_order = nprandom.choice([DisasterType.fire, DisasterType.tornado, DisasterType.hurricane,
                                      DisasterType.earthquake, DisasterType.monster, DisasterType.ufo],
                                     disaster_count,
                                     DISASTER_WEIGHTS)
    disaster_order = [int(x) for x in disaster_order]

    # Insert disasters into the disaster slots
    for x, element in enumerate(skeleton_list):
        skeleton_list[x] = []
        if element == 1:
            skeleton_list[x].append(disaster_order.pop(0))

    # Initialize basic list
    disaster_rates = {}
    for x in range(MAX_TURNS):
        disaster_rates[x + 1] = {
            'rates': {
                DisasterType.fire: 0,
                DisasterType.tornado: 0,
                DisasterType.hurricane: 0,
                DisasterType.earthquake: 0,
                DisasterType.monster: 0,
                DisasterType.ufo: 0,
            },
            'disasters': skeleton_list[x],
        }

    # Go through each disaster individually to determine rates
    for disaster_type in range(6):
        for key, item in disaster_rates.items():
            # If disaster is happening set the odds to 0
            if disaster_type in disaster_rates[key]['disasters']:
                disaster_rates[key]['rates'][disaster_type] = 0
                continue

            try:
                # Find next occurrence of the disaster
                next_occurrence_index = skeleton_list[key:].index([disaster_type]) + key + 1
                distance_away = next_occurrence_index - key
                rate = (2 * APPROXIMATE_DISASTER_COUNT / MAX_TURNS) / distance_away
                # add previous rate
                if key > 1:
                    rate += disaster_rates[key - 1]['rates'][disaster_type]

                disaster_rates[key]['rates'][disaster_type] = min(rate, 0.999)
            except ValueError:
                # If disaster doesn't happen again, its probably late in the game so just increase randomly
                rate = random.random() * 0.005
                if key > 1:
                    rate += disaster_rates[key - 1]['rates'][disaster_type]
                disaster_rates[key]['rates'][disaster_type] = min(rate, 0.999)

    # Convert to json file
    write(disaster_rates)


# Biases disasters towards the latter half of the game
def bias_list(given_list, current_depth=1):
    # prevent from going too deep
    total_disasters = sum(given_list)
    if current_depth > BIASING_DEPTH or total_disasters == 0:
        return given_list

    first_half = given_list[:len(given_list)//2]
    second_half = given_list[len(given_list)//2:]

    # if the rate of disasters in the first half of the list is outside the margin of error of what it should be,
    # bias the list until it fits
    first_disaster_ratio = (sum(first_half) / total_disasters)
    actual_ratio_with_error = DISASTER_BIAS + DISASTER_BIAS * BIAS_MARGIN_OF_ERROR
    attempts = 0
    max_attempts = len(first_half)
    while abs(first_disaster_ratio) > actual_ratio_with_error and attempts < max_attempts:
        attempts += 1

        # if more disasters in first list than second
        if first_disaster_ratio > DISASTER_BIAS:
            # if no disaster to move, exit
            if sum(first_half) == 0 or sum(second_half) == len(second_half):
                break
            # take random disaster occurrence from the first list and insert it into the second
            first_indexes = [i for i, e in enumerate(first_half) if e == 1]
            second_indexes = [i for i, e in enumerate(second_half) if e == 0]
            first_half[random.choice(first_indexes)] = 0
            second_half[random.choice(second_indexes)] = 1

        # if more disasters in second list than first
        else:
            # if no disaster to move, exit
            if sum(second_half) == 0 or sum(first_half) == len(first_half):
                break
            # take random disaster occurrence from the second list and insert it into the first
            first_indexes = [i for i, e in enumerate(first_half) if e == 0]
            second_indexes = [i for i, e in enumerate(second_half) if e == 1]
            first_half[random.choice(first_indexes)] = 1
            second_half[random.choice(second_indexes)] = 0

        # recalculate ratio
        first_disaster_ratio = (sum(first_half) / total_disasters)

    # balance inner lists
    bias_list(first_half, current_depth + 1)
    bias_list(second_half, current_depth + 1)

    return first_half + second_half


def print_dict(data, name='dict'):
    res = name + '\n'
    for key, item in data.items():
        res += f'{key}: {item}\n'
        
    print(res)


def write(data):
    if not os.path.exists('logs'):
        os.makedirs('logs')
    
    with open('logs/game_map.json', 'w+') as out:
        json.dump(data, out)
