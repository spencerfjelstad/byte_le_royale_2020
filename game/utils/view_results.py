import game.config as config
import json


# WARNING: Use at your own risk.
# This can create a lot of variable names dynamically, so don't hand it a large list.
def set_vars(json):
    if len(json) > 10:
        print("I don't think you meant to use this json. There are a too many variables in here.\nExiting...")
        return

    # I'm going to do what's called a pro gamer move
    for key, var in json.items():
        # For every key in the json, create a variable for use with python interpreter
        globals()[key.lower()] = var
        print(f"Created variable {key.lower()}.")
    print("Done")


with open(config.RESULTS_FILE, 'r') as results_file:
    # Read file in as JSON string
    file_str = results_file.read()

    # Convert the JSON string to a dictionary
    contents = json.loads(file_str)
    set_vars(contents)
