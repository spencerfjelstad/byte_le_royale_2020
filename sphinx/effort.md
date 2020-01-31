# Effort

Effort is a unit of work that your city is capable of producing each turn. Effort is equal to the current population of the city and will rise and fall as the population does. Some actions require effort to complete, and sometimes it may take multiple turns of allocating effort to complete a project. Effort can be directed at one objective, or split up on multiple objectives at the same time, but you may not allocate more effort than you have population.

There are many ways you can allocate your effort. 

### Do Nothing
This will allocate your population to, well, nothing at all. Take the day off. Go see the movies. This will have no effect at all on the survival of your city.

### Upgrades
Allocating effort towards these objects will, once a threshold is reached, improve their effectiveness. Once the object is leveled up, any leftover effort will go towards its next level.
- City - This increases the maximum structure your city can hold. Since population is capped by your city's current structure, this will allow you to have more maximum population. Note that allocating effort towards upgrading your city will *not* increase your current structure amount; if you are looking to increase your current structure amount, then allocate effort towards Repair Structure. If your city is leveled up, any leftover effort will go towards its next level.
- Sensors - This will cause the sensor readings get more and more precise to the actual chance of a disaster occurring. Sensors must be leveled up individually.
The sensor objects can be found in the city.sensors variable.
- Buildings - Each building has unique effects, so [view each building's specific effects](Buildings) to see how they work. Like sensors, buildings must be leveled up individually.
Unlike sensors, buildings require wealth to upgrade. If you are allocating more effort than you have wealth, the allocated effort will be reduced to your available wealth. However, the remaining effort that was allocated will not be recycled. 
If you don't have enough wealth for the amount of effort you are allocating, your effective effort will be reduced to the amount of wealth that you do have available. 
The building objects can be found in the city.buildings variable.

### Repair Structure
Allocating effort towards repairing structure will increase your current structure amount of your city. Current structure is capped by maximum structure and is reduced by disasters. Be careful, if your city structure falls to 0, your city will be destroyed, and the game ends! Your current population is also capped by your current structure, *not* your maximum structure, so if you're running low on population, maybe invest in repairing your city's structure.

### Regain Population
Allocating your effort towards regaining population will increase your current population amount of your city. Current population is capped by current structure and is reduced by disasters. Be careful, if your city structure falls to 0, your city will be destroyed, and the game ends! Higher population amounts will also increase the amount of effort you can allocate on a given turn, so more population means more effort towards other actions!

### Accumulate Wealth
Accumulate Wealth will increase the current amount of wealth you have. Wealth is used to upgrade structures, so make sure you have enough money before allocating people towards upgrading your structures.

### Put Out Disasters
Some disasters are long lasting annoyances to your city, that will deal constant population and structure damage over time. To deal with these, you must allocate effort towards putting these disasters out. Allocating effort towards disasters will *not* directly decrease the damage these lasting disasters do. 
For example, imagine a fire needs 100 more effort to put out, and deals 100 population damage a turn (numbers may not be accurate to the current build of the game). If you decide to allocate 99 effort towards this disaster, then the fire will need 1 more effort to put it out (to be done on a later turn) but will still deal 100 population damage. The next turn, if you allocate 1 more effort towards the same fire, then the fire will disappear and will deal 0 more damage.
The list of current disasters is provided by the take_turn disasters array argument. Note that this includes instant disasters as well as lasting, so be sure to only apply effort to lasting disasters.

###How to allocate effort
To add effort, use `actions.add_effort()`, then specify either an ActionType or an object like city or an element in the disasters array, and the amount of effort to allocate.

For example, if we wanted to generate population,
```python
actions.add_effort(ActionType.regain_population, amount)
```
If we wanted to upgrade an object, like the instant_decree_booster building,
```python
actions.add_effort(city.buildings[BuildingType.instant_decree_booster], amount)
```
If we wanted to allocate effort to put out a lasting disaster,
```python
actions.add_effort(disasters[0], amount)
```

Note that the list of current disasters is provided by the take_turn disasters argument. 
Multiple lasting disasters of the same type can exist at once. For example, a city can be under attack by three different fires at the same time. There is no upper limit to the amount of lasting disasters currently effecting a city.


The order of effort allocations are done in the following order:
1. Do Nothing
2. Upgrade City
3. Repair Structure
4. Regain Population
5. Accumulate Wealth
6. Put Out Disasters
7. Upgrade Sensors
8. Upgrade Buildings
