# Buildings
Buildings can be constructed in your city to improve your city's functionality. Buildings can improve decrees, wealth, population, and structure. Without upgrading them, they sit as empty spots on your city. To build them, allocate effort to one of the buildings in `city.buildings`. However, buildings also require gold equal to the required effort to upgrade. In order to apply allocated effort to a building you must have an equivalent amount of gold. The gold will be automatically spent and any access effort will be wasted. Once the required amount of effort and gold required to upgrade is reached, the building will be upgraded.

For example, if you wanted to allocate effort to the Instant Decree Booster, you would type `actions.add_effort(city.buildings[BuildingType.police_station], amount)`. For more information on allocating effort, see [Effort](effort.html).

There are 6 types of buildings:
- [Police Station](#police-station)
- [Gelato Shop](#gelato-shop)
- [Mint](#mint)
- [Billboard](#billboard)
- [3D Printer](#3d-printer)
- [Big Canoe](#big-canoe)


## Police Station
This increases the effectiveness of your correctly guessed decrees for instant disasters.

Level | Effort Required | Gold Required | Damage Mitigated
--- | --- | --- | ---
Base | 0 | 0 | 50%
1 | 40750 | 40750 | 75%

## Gelato Shop
This increases the effectiveness of your correctly guessed decrees for lasting disasters.

Level | Effort Required | Gold Required | Damage Mitigated
--- | --- | --- | ---
Base | 0 | 0 | 50%
1 | 35050 | 35050 | 75%

## Mint
This gives you additional wealth for free.

Level | Effort Required | Gold Required | Wealth Added
--- | --- | --- | ---
1 | 28440 | 28440 | 150

## Billboard
This gives you additional population through tourism. This does not increase your population above your structure level. This amount is added every turn.

Level | Effort Required | Gold Required | Population Added
--- | --- | --- | ---
1 | 28440 | 28440 | 25

## 3D Printer
Shown as the 3D printer, this gives you additional structure. This does not increase your structure above your max structure level. This amount is added every turn.

Level | Effort Required | Gold Required | Structure Added
--- | --- | --- | ---
1 | 35050 | 35050 | 25

## Big Canoe
The big canoe. This beast gives you additional wealth, population, and structure. As with the population and structure boosters, population and structure will not be added past their max. However, structure is added first, so if population and structure are equal, they will increase at equal rates. 

Level | Effort Required | Gold Required | Wealth Added | Population Added | Structure Added
--- | --- | --- | --- | --- | ---
1 | 80100 | 80100*__* | 200 | 30 | 30


