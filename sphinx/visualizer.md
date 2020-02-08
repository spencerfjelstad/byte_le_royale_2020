# Visualizer

### How to start the visualizer:
In your pipenv shell, run python .\launcher.pyz visualizer (or v). This will launch the visualizer with default options. The following table lists other flags that can be used to edit the default settings.

Command        | Shorthand  | Effect
---------------|:----------:|-------
--help         | -h         | Displays the commands available for the visualizer and how to use them
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
|DOWN Arrow | Decrease visualizer speed dowwn to 0.25x             |
|z          | Skip to endscreen (only usable after loading screen) |
|1          | Endscreen only, switches graph to display Population |
|2          | Endscreen only, switches graph to display Structure  |
|3          | Endscreen only, switches graph to display Gold       |

