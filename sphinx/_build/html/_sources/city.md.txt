# City
Your city is what you must protect against disasters. It houses several important stats that stand between you and GAME OVER, Population and Structure. Structure acts as your population's max cap, so if your structure reaches zero, so does your population. Once population reaches zero, your city falls and it's game over. You can protect your city by having the correct [decrees](decrees.html), upgrading [buildings](buildings.html), and by allocating [effort](effort.html) to `ActionType.regain_population` and `ActionType.repair_structure`.

Your city can start with different bonuses and advantages. This can be assigned in the city_type method in your client. For example, if we wanted to have a popular city, we would return `CityType.popular` in the city_type method.

There are 6 kinds of cities to choose from:
* Healthy: Starts with population already up to structure, giving your city a headstart in allocating effort
* Sturdy: Starts with structure up to max structure, allowing you to focus on population.
* Invested: Start with 5000 gold.
* Pyrophobic: Upgrades the fire sensor to level 1. 
* Popular: Upgrades the population booster building to level 1.
* Modern: Upgrades the city to level one. 

Your city starts with default stats:

Stat | Value
--- | ---
Max Structure | 200
Current Structure | 100
Current Population | 40
Gold | 0

These values can be increased either through automatic accumulation, effort allocation, or upgrades.
While gold is automatically accumulated at a rate of 3 gold per turn, the max structure can be upgraded by `actions.add_effort(ActionType.upgrade_city, amount)`. 

Level | Effort Cost | Max Structure
--- | --- | ---
Base | 0 | 200
1 | 15000 | 225
2 | 16875 | 275
3 | 20625 | 350