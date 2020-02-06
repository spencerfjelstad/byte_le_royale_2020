# API

- [Action](#action)
- [Building](#building)
- [City](#city)
- [Disaster](#disaster)
- [LastingDisaster](#lastingdisaster)
- [Sensor](#sensor)

## Action
The Action object is used by the client to make effort allocations or setting the decree.

#### object_type
Backend value that distinguishes different objects apart from each other (city, sensors, buildings, etc.)

#### add_effort(self, action, amount)

The add_effort function will let you distribute your population.

The action parameter can either be an ActionType enum or a 
City, Building, LastingDisaster, or Sensor object.
ActionType enums acceptable: 
* none
* repair_structure
* regain_population
* accumulate_wealth
* upgrade_city

The amount parameter is the number of people that you want to work towards your given action. 
Note that allocating more people than your city has available will truncate the amount down 
to what your city can offer.

#### clear_actions(self)
This function will remove all current effort allocations this turn.

#### delete_index_actions(self, index)
This function will remove the effort allocation at the given index.

#### get_allocation_list(self)
This function will return a *copy* of the current allocations. Adding new effort allocations
will make your *copy* outdated.

#### get_decree(self)
Returns the current decree that has been set for the current turn. If no decree has been set, 
then this function will return None.

#### set_decree(self, decree)
Sets the decree for this turn. If this function is called twice, the second decree will be used. 
The decree parameter will only accept values from the DecreeType enum:
* none
* anti_fire_dogs
* paperweights
* snow_shovels
* rubber_boots
* fishing_hook
* cheese

## Building
#### building_type
The type of the current building, of BuildingType. This can be one of six different buildings.
* police_station
* gelato_shop
* big_canoe
* mint
* billboard
* printer

#### object_type
Backend value that distinguishes different objects apart from each other (city, sensors, buildings, etc.)

#### level
Current level of the building. This will start at level zero.

#### effort_remaining
Remaining effort required to level up this building to the next level. When the building is maxed out, this value will remain at 0.

## City

#### city_name
The name of your city that will be displayed to the visualizer.

#### city_type
The selected city type that is selected at the start of the game for a starting boost.

#### object_type
Backend value that distinguishes different objects apart from each other (city, sensors, buildings, etc.)

#### structure
Current structure of the city. This will never be higher than max_structure and never lower than 0.

#### max_structure
Max possible structure achievable by the city. When the city levels up, this max_structure value will be increased.

#### population
Current population of the city. This will never be higher than structure and never lower than 0.

#### gold
Current gold value available in the city. This will slowly accumulate over time, or effort can be allocated towards getting more.

#### sensors
A dictionary of the six sensors in your city. The keys will be of SensorType and the values will be the Sensor objects.

#### buildings
A dictionary of the buildings in your city. The keys will be of BuildingType and the values will be the Building objects.

#### level
Current level of the city. This will start at level zero.

#### effort_remaining
Remaining effort required to level up this city to the next level. When the city is maxed out, this value will remain at 0.

## Disaster

#### status
This value will indicate whether the disaster is DisasterStatus.dead or DisasterStatus.live. When disasters become
'dead', they will be removed from the game. This will occur when the instant disaster's turn ends or the lasting
disaster's effort_remaining hits 0.

#### type
Indicates which DisasterType this current disaster is. This can be fire, blizzard, tornado, earthquake, monster, or ufo.

#### population_damage
How much population damage the disaster does. This has no effect on the city's structure.

#### structure_damage
How much structure damage the disaster does. This has no effect on the city's population. (Unless your city would have
more population than structure, which in this case, would make you lose the excess population.)

#### object_type
Backend value that distinguishes different objects apart from each other (city, sensors, buildings, etc.)

#### level
Current level of the disaster. This will start at level zero, but will be higher at later turns, increasing damage.

## LastingDisaster
The LastingDisaster object will include all values found in the Disaster object. 
(Note: Instant disasters inherit directly from Disaster.)

#### newly_spawned
This will be True the turn the disaster appears, and will be turned False immediately by the end of the turn.

#### initial_effort
Initial effort is the starting amount of effort required to put out the disaster. This will remain the same until the
disaster gets put out.

#### effort_remaining
Effort remaining to be put into a disaster until it gets put out. Once this value hits 0, the disaster is 'put out' 
and will be removed from the game.

## Sensor

#### sensor_type
Indicates which SensorType this current sensor is. Each sensor in the city will be of a different type. 

#### object_type
Backend value that distinguishes different objects apart from each other (city, sensors, buildings, etc.)

#### level
Current level of the sensor. This will start at level zero, and can go up to turn three.

#### effort_remaining
The amount of effort remaining until the sensor gets upgraded. Once the sensor is max level, this value will be zero.

#### sensor_results
This value is the next turn's chance of the associated disaster. This value will not match up exactly with the 
disaster's real odds, but will be close to the actual value, depending on the sensor's level. 
