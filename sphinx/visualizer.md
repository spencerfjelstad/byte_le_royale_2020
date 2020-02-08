# Visualizer

### How to start the visualizer:
In your pipenv shell, run python .\launcher.pyz visualizer (or v). This will launch the visualizer with default options. The following table lists other flags that can be used to edit the default settings.

Command        | Shorthand  | Effect
---------------|:----------:|-------
--help         | -h         | Displays the commands available for the visualizer
-fullscreen    | -f         | Launches the visualizer in fullscreen
-skip          | -s         | Visualizer will close automatically on endscreen
-gamma (value) | -g (value) | Manually input a set gamma value (not recommended)

### Controls:

|Input      | Result                                               |
|-----------|------------------------------------------------------|
|CTRL + f   | Toggle fullscreen                                    |
|CTRL + x   | Toggle fps display                                   |
|CTRL + s   | Take a screenshot!                                   |
|UP Arrow   | Increase visualizer speed up to 4x                   |
|DOWN Arrow | Decrease visualizer speed down to 0.25x             |
|z          | Skip to endscreen (only usable after loading screen) |
|1          | Endscreen only, switches graph to display Population |
|2          | Endscreen only, switches graph to display Structure  |
|3          | Endscreen only, switches graph to display Gold       |

### What's Displayed:

#### Decrees:
The top left corner of the screen displays the decree active for the current turn. If the decree matches the disaster occuring that turn, the word 'Protected!' will appear beneath it.

##### Forecast Tape:
The forecast tape displays the disasters for the current turn as well as two turns in the past and future.  
Disasters that appear in the forecast tape are also marked with a colored indicator. The different colors represent the level of that disaster, according to the table below. These levels correspond to the `Disaster.level` values for each disaster.

Color | Level
--- | ---
Bronze | 0
Silver | 1
Gold | 2
Uranium | 3
Plutonium | 4

##### Sensors:
The antenna-like structures around the screen are your sensors! Each sensor has its own level, visualized with a colored bar in the middle. The higher the bar, the more accurate the sensor. The sensor color to disaster relationship is described in the following table.

Type | Color
--- | ---
Fire | Red
Tornado | Yellow
Blizzard | Icy Blue
Earthquake | Brown
Monster | Orange
UFO | Green

##### People:
Besides one location, each person represents about 1/20th of the current turns allocated effort. Any unused effort is represented by people dancing on the roof of the tallest building. Otherwise, people are placed according to where that turn's effort is allocated. Examples being people in the sky to fix a blizzard and in a parking lot to upgrade the city.

##### Status Bar:
The status bar at the bottom of the screen can be split into three sections. The leftmost section contains the two health bars, one for Population and one for Structure. Each bar is divided into 50pt chunks. The middle section displays ongoing lasting disasters, with a multplier showing how many of the same one are happening. The turn a marker disappears from this area is the turn it is dealt with. It still deals damage that turn! Finally, the rightmost section displays your current gold count and visualizer speed multiplier.