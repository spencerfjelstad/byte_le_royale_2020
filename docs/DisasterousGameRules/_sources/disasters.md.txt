# Disasters
Disasters are what threaten your city's survival. They damage your city's population and structure. Some are more powerful than others, and some are more likely, so plan carefully. The damage caused by disasters can be mitigated by having the corresponding decree and building. However, keep upgrading parts of your city, because the disasters will get more difficult the more turns your city survives.

There are two types of disasters: lasting disasters and instant disasters. 

## Lasting Disasters
Lasting disasters include fire, blizzard, and monster. They stick around in the disasters array, causing population and structure damage each turn they exist. In order to put them out, you need to allocate enough effort to match the disaster's `effort_remaining` attribute. These lasting disasters can stack if ignored, and multiple of the same kind may exist.

### Fire

Level| Population DMG | Structure DMG | Effort Required
--- | --- | --- | ---
0 | 2 | 1 | 400
1 | 2 | 1 | 800
2 | 2 | 1 | 1350
3 | 2 | 1 | 2200
4 | 4 | 2 | 2200

### Blizzard

Level| Population DMG | Structure DMG | Effort Required
--- | --- | --- | ---
0 | 6 | 3 | 600
1 | 6 | 3 | 1350
2 | 6 | 3 | 2025
3 | 6 | 3 | 3300
4 | 12 | 6 | 3300

### Monster

Level| Population DMG | Structure DMG | Effort Required
--- | --- | --- | ---
0 | 5 | 10 | 800
1 | 5 | 10 | 1800
2 | 5 | 10 | 3300
3 | 5 | 10 | 5600
4 | 10 | 20 | 5600

## Instant Disasters
Instant disasters include tornado, earthquake, and UFO. These appear in the disasters array the turn they affect the city, but will disappear after the turn is over. They cause significantly more damage, so be sure to prepare accordingly. They require no effort to be allocated. 

### Tornado

Level| Population DMG | Structure DMG
--- | --- | ---
0 | 12 | 25
1 | 25 | 50
2 | 37 | 75
3 | 50 | 100
4 | 75 | 150

### Earthquake

Level| Population DMG | Structure DMG
--- | --- | ---
0 | 25 | 50
1 | 50 | 100
2 | 100 | 200
3 | 150 | 300
4 | 250 | 400

### UFO

Level| Population DMG | Structure DMG
--- | --- | ---
0 | 100 | 50
1 | 200 |100
2 | 400 | 200
3 | 800 | 400
4 | 1396 | 698
