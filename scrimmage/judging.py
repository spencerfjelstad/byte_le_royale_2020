import json
import os
import shutil
import statistics
import subprocess
import zipfile

import pymongo

from scrimmage.utilities import *


def main():
    db_client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = db_client["royale"]
    db_collection = db["teams"]

    number_of_runs = 10

    # Establish folder things will be run in
    path = 'scrimmage/judging'
    if not os.path.exists(path):
        os.mkdir(path)

    shutil.copy('launcher.pyz', path)

    # Generate a set number of game maps to run
    game_maps = list()
    game_map_path = f'{path}/logs/game_map.json'
    for x in range(number_of_runs):
        p = subprocess.Popen('python launcher.pyz generate', cwd=path, shell=True)
        stdout, stderr = p.communicate()

        # Convert file to binary string and save it
        game_maps.append([file_to_binary(game_map_path)])

    # Clean up location
    shutil.rmtree(game_map_path, ignore_errors=True)

    results = dict()
    # For each client in the list, run them through each match
    for entry in db_collection.find({}):
        print(f'Working on team {entry["teamname"]}')
        
        internal_results = list()

        # Put the client in the folder
        if entry['code_file'] is not None:
            binary_to_file(f'{path}/client.py', entry['code_file']['contents'])

            for game_map in game_maps:
                # Put the game map in the log folder
                binary_to_file(game_map_path, game_map)

                # Run the game
                p = subprocess.Popen('python launcher.pyz run', cwd=path, shell=True)
                stdout, stderr = p.communicate()

                # Take the results and save it
                results_path = path + '/logs/results.json'
                r = dict()
                with open(results_path, 'r') as f:
                    r = json.load(f)

                score = r['Score']

                # Zip log files up
                with zipfile.ZipFile(f'{path}/logs.zip', 'w') as z:
                    for filename in os.listdir(f'{path}/logs'):
                        z.write(f'{path}/logs/{filename}', arcname=f'logs/{filename}')

                b = file_to_binary(f'{path}/logs.zip')

                internal_results.append({'Score': score,
                                'Logs': b})

        # Generate results
        best_run = 0
        best_log = None
        for res in internal_results:
            if res['Score'] > best_run:
                best_run = res['Score']
                best_log = res['Logs']

        
        score_count = len([x['Score'] for x in internal_results])
        average_score = statistics.mean([x['Score'] for x in internal_results]) if score_count > 0 else 0
        median_score = statistics.median([x['Score'] for x in internal_results]) if score_count > 0 else 0

        results[entry['teamname']] = {'Best Score': best_run,
                                      'Average Score': average_score,
                                      'Median Score': median_score,
                                      'Best log': best_log}

    # Export the results of all clients to a file
    results_path = 'scrimmage/results'
    if os.path.exists(results_path):
        shutil.rmtree(results_path)
    if not os.path.exists(results_path):
        os.mkdir(results_path)

    # Create folder for each team containing their client and best logs
    for team, res in results.items():
        os.mkdir(f'{results_path}/{team}')

        # Get code file
        cf = [x for x in db_collection.find({'teamname': team})][0]['code_file']

        if cf is not None:
            binary_to_file(f'{results_path}/{team}/{cf["name"]}', cf['contents'])
        if res is not None and res['Best log'] is not None:
            binary_to_file(f'{results_path}/{team}/logs.zip', [res['Best log']])

        res.pop('Best log', None)

    # Dump total results to a file
    with open(results_path + '/final_results.json', 'w') as f:
        json.dump(results, f)

    # Final cleanup
    shutil.rmtree(path)


if __name__ == '__main__':
    main()
