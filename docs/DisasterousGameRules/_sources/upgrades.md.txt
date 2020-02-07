# Upgrades
While more detailed information can be found at their respective pages, here are all the tables relating to upgradable objects.

## Buildings
You can upgrade [buildings](buildings.html) that improve your city in various ways.
### Police Station
To upgrade, do `actions.add_effort(city.buildings[BuildingType.police_station], amount)`.

Level | Effort Required | Damage Mitigated
--- | --- | ---
Base | 0 | 50%
1 | 40750 | 75%

### Gelato Shop
To upgrade, do `actions.add_effort(city.buildings[BuildingType.gelato_shop], amount)`.

Level | Effort Required | Damage Mitigated
--- | --- | ---
Base | 0 | 50%
1 | 35050 | 75%

### Mint
To upgrade, do `actions.add_effort(city.buildings[BuildingType.mint], amount)`.

Level | Effort Required | Wealth Added
--- | --- | ---
1 | 28440 | 150

### Billboard
To upgrade, do `actions.add_effort(city.buildings[BuildingType.billboard], amount)`.

Level | Effort Required | Population Added
--- | --- | ---
1 | 28440 | 25

### 3D Printer
To upgrade, do `actions.add_effort(city.buildings[BuildingType.printer], amount)`.

Level | Effort Required | Structure Added
--- | --- | ---
1 | 35050 | 25

### Big Canoe
To upgrade, do `actions.add_effort(city.buildings[BuildingType.big_canoe], amount)`.

Level | Effort Required | Wealth Added | Population Added | Structure Added
--- | --- | --- | --- | ---
1 | 80100 | 60 | 30 | 30


## City
Your [city](city.html) can be upgraded to increase the max structure.

Level | Effort Cost | Max Structure
--- | --- | ---
Base | 0 | 200
1 | 15000 | 225
2 | 16875 | 275
3 | 20625 | 350

## Sensors
Your sensors can be upgraded to improve their accuracy. You need to upgrade each one individually. 

Level | Effort Cost | Sensor Inaccuracy Range
--- | --- | ---
Base | 0 | 100
1 | 4000 | 50
2 | 8500 | 20
3 | 13500 | 1
