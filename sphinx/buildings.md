# Buildings
Buildings can be constructed in your city to improve your city's functionality. Buildings can improve decrees, wealth, population, and structure. Without upgrading them, they sit as empty spots on your city. To build them, allocate effort to one of the buildings in `city.buildings`. Once the required amount of effort to upgrade is reached, the building will be upgraded.

For example, if you wanted to allocate effort to the Instant Decree Booster, you would type `actions.add_effort(city.buildings.instant_decree_booster, amount)`. For more information on allocating effort, see [Effort](effort.html).

There are 6 types of buildings:
- [Instant Decree Booster](#instant-decree-booster)
- [Lasting Decree Booster](#lasting-decree-booster)
- [Wealth Booster](#wealth-booster)
- [Population Booster](#population-booster)
- [Structure Booster](#structure-booster)
- [Everything Booster](#everything-booster)


## Instant Decree Booster
Shown as the police station, this increases the effectiveness of your correctly guessed decrees for instant disasters by a multiplier that increases with each upgrade.

Level | Effort Required | Decree Boost Multiplier
--- | --- | ---
1 | 13800 | 1.1
2 | 18100 | 1.25
3 | 25300 | 1.5

## Lasting Decree Booster
Shown as the gelato shop, this increases the effectiveness of your correctly guessed decrees for lasting disasters by a multiplier that increases with each upgrade.

Level | Effort Required | Decree Boost Multiplier
--- | --- | ---
1 | 12000 | 1.1
2 | 15750 | 1.25
3 | 22000 | 1.5

## Wealth Booster
Shown as the bank, this gives you additional wealth by an amount that increases with each upgrade.

Level | Effort Required | Wealth Added
--- | --- | ---
1 | 9600 | 20
2 | 12600 | 40
3 | 17600 | 60

## Population Booster
Shown as the billboard, this gives you additional population by an amount that increases with each upgrade. This does not increase your population above your structure level.

Level | Effort Required | Population Added
--- | --- | ---
1 | 9600 | 5
2 | 12600 | 15
3 | 17600 | 25

## Structure Booster
Shown as the 3D printer, this gives you additional structure by an amount that increases with each upgrade. This does not increase your structure above your max structure level. 

Level | Effort Required | Structure Added
--- | --- | ---
1 | 12000 | 5
2 | 15750 | 15
3 | 22000 | 25

## Everything Booster
The big canoe. This beast gives you additional wealth, population, and structure. As with the population and structure boosters, population and structure will not be added past their max. However, structure is added first, so if population and structure are equal, they will increase at equal rates. 

Level | Effort Required | Wealth Added | Population Added | Structure Added
--- | --- | --- | --- | ---
1 | 25000 | 20 | 10 | 10
2 | 35000 | 40 | 20 | 20
3 | 45000 | 60 | 30 | 30


