# client structure

Make sure that your client file contains the word "client" in the filename, and has the following methods in the file.

## __init__(self):
Use this function to save variables across turns. Keep the `super().__init__()` line in this function, since this 
will help for debug levels.

## print(self, *args):
By using our built-in print statement, you can enable and disable all print statement easily by calling the 
launcher.pyz's debug argument.

## team_name(self):
In this function, return your team name so it appears on the visualizer. 

## city_name(self):
In this function, return your city name so it appears on the visualizer (if your city has successfully built the billboard)

## city_type(self):
In this function, return a CityType enum to get an extra boost at the start of the game.

## take_turn(self, turn, actions, city, disasters):
This will be your main control of your AI. This function gets called every turn until your city gets destroyed. 
Decide actions and set decrees here. 

The turn parameter will return the current turn number.
The actions parameter is the Action object that you can set decrees or set actions to.
The city parameter is your city. Your sensors and buildings are found here.
The disasters parameter is all current disasters affecting your city, including lasting disasters and instant disasters.

You will not have to return anything from this function.
