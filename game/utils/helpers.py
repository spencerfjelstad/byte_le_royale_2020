import json
import os
import random


def clamp(value, min_value=0, max_value=100):
    """
    Restricts a given value from going outside the range, default of 0 and 100
    :param value: given value to be clamped
    :param min_value: minimum value of the clamping range
    :param max_value: maximum value of the clamping range
    :return: the value given but restricted to max or min if it goes outside the range
    """
    return min(max_value, max(value, min_value))


def decision(probability):
    """
    Function useful for giving a random True or False based on a given odds
    :param probability: float value between 0 and 1. higher is greater odds
    :return: boolean value of result
    """
    return random.random() < probability


def enum_iter(enum_class):
    """
    Creates a list of all enum elements of a given enum class (including none or default values)
    :param enum_class: Enum class to retrieve all possibilities from
    :return: list containing all enum of the given type
    """
    return [enum_class.__dict__[key] for key in enum_class.__dict__ if not key.startswith("__")]

def enum_to_string(enum, val):
    """

    :param enum:
    :param val:
    :return:
    """
    return [k for k, v in dict(enum.__dict__).items() if not k.startswith("__") and v == val][0]

def write(data, file):
    """
    Given json formatted data, create a new file at given directory and dump the information there
    :param data: json formatted data to write to the new file
    :param file: file directory and file name (preferably with .json extension)
    """
    file_dir = os.path.dirname(file)

    # Make folders if necessary
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)

    # Open and write to file
    with open(file, 'w+') as out:
        json.dump(data, out)
