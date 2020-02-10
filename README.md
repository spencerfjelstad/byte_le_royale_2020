# Byte-le Royale 2020
This is the code for Disaster Dispatcher, the game for the Byte-le Royale competition year 2020

## How to run the game:

### Getting the code

- Option 1: Clone the repository and run build.bat (sorry other OS users)
- Option 2: Download the latest release and put it in a folder with the Pipfile and the Pipfile.lock from the repository

### Installing the environment

1. Install Python 3.7 and `pip install pipenv`
2. Open powershell or a terminal in the folder where launcher.pyz is
3. Run `pipenv install -d` to install the environment with dev packages and wait for it to finish
4. Run `pipenv shell` to enter the environment

### Running the game

0. Make any modifications to my_client.py or remove it and add your own. Files with 'client' in the name are recognized as valid clients - this game will only run if there's exactly one!
1. Inside of the pipenvironment, you may run `python ./launcher.pyz --help` to see available game commands
2. To generate a new world file with different disasters, run `python ./launcher.pyz generate`
3. To run your client's code against the generated world, run`python ./launcher.pyz run`. If you leave out `python` at the start, any output (including errors) may not display!
	- 3.5. To run your client's code and view output from debug statements (using `self.print()`), you must run it with the `-debug` flag. Use `python ./launcher.pyz r -d 1` to run with client output, or a higher integer (up to 4) for game engine debug output.
4. To start the visualizer on the last run, use `python ./launcher.pyz visualizer`.

### Further documentation and information

- All game documentation that was available to competitors is available in the docs/DisasterousGameRules folder, however the links between the pages may become broken in the future. Opening each .html file manually as you need to read them should always work.
- This documentation should give you all the information you need to know about the game and writing a client. The scrimmage server is no longer running and will not function as it did during the competition, however local running is still available. The scrimmage server code is available in this repository, however it will require modification for clients to connect correctly.
