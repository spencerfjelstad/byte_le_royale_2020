# Upgrades
While more detailed information can be found at their respective pages, here are all the tables relating to upgradable objects.

## Buildings
You can upgrade [buildings](buildings.html) that improve your city in various ways.
### Instant Decree Booster
To upgrade, do `actions.add_effort(city.buildings[BuildingType.instant_decree_booster], amount)`.

Level | Effort Required | Damage Mitigated
--- | --- | ---
Base | 0 | 50%
1 | 13800 | 55%
2 | 18100 | 62.5%
3 | 25300 | 75%

### Instant Decree Booster
To upgrade, do `actions.add_effort(city.buildings[BuildingType.lasting_decree_booster], amount)`.

Level | Effort Required | Damage Mitigated
--- | --- | ---
Base | 0 | 50%
1 | 12000 | 55%
2 | 15750 | 62.5%
3 | 22000 | 75%

### Wealth Booster
To upgrade, do `actions.add_effort(city.buildings[BuildingType.wealth_booster], amount)`.

Level | Effort Required | Wealth Added
--- | --- | ---
1 | 9600 | 20
2 | 12600 | 40
3 | 17600 | 60

### Population Booster
To upgrade, do `actions.add_effort(city.buildings[BuildingType.population_booster], amount)`.

Level | Effort Required | Population Added
--- | --- | ---
1 | 9600 | 5
2 | 12600 | 15
3 | 17600 | 25

### Structure Booster
To upgrade, do `actions.add_effort(city.buildings[BuildingType.structure_booster], amount)`.

Level | Effort Required | Structure Added
--- | --- | ---
1 | 12000 | 5
2 | 15750 | 15
3 | 22000 | 25

### Everything Booster
To upgrade, do `actions.add_effort(city.buildings[BuildingType.everything_booster], amount)`.

Level | Effort Required | Wealth Added | Population Added | Structure Added
--- | --- | --- | --- | ---
1 | 25000 | 20 | 10 | 10
2 | 35000 | 40 | 20 | 20
3 | 45000 | 60 | 30 | 30

## City
Your [city](city.html) can be upgraded to increase the max structure.

Level | Effort Cost | Max Structure
--- | --- | ---
1 | 20000 | 225
2 | 22500 | 275
3 | 27500 | 350

## Sensors
Your sensors can be upgraded to improve their accuracy. You need to upgrade each one individually. 

Level | Effort Cost | Sensor Inaccuracy Range
--- | --- | ---
Base | 0 | 60
1 | 6000 | 30
2 | 11250 | 15
3 | 18000 | 5
