from game.client.user_client import UserClient
from game.utils.oop import *
from game.common.enums import *

import random
import sys

class Client(UserClient):
    # Variables and info you want to save between turns go here
    @overrides(UserClient)
    def __init__(self):
        super().__init__()

    @overrides(UserClient)
    def team_name(self):
        return "Communist Russia"

    @overrides(UserClient)
    def city_name(self):
        cities = ["Moscow", "Saint Petersburg", "Novosibirsk", "Yekaterinburg", "Nizhny Novgorod", "Kazan",
                  "Chelyabinsk", "Omsk", "Samara", "Rostov-on-Don", "Ufa", "Krasnoyarsk", "Perm", "Voronezh",
                  "Volgograd", "Krasnodar", "Saratov", "Tyumen", "Izhevsk", "Barnaul", "Ulyanovsk", "Irkutsk",
                  "Khabarovsk", "Yaroslavl", "Vladivostok", "Makhachkala", "Tomsk", "Orenburg", "Kemerovo", "Ryazan",
                  "Astrakhan", "Penza", "Lipetsk", "Kirov", "Cheboksary", "Tula", "Kaliningrad", "Balashikha", "Kursk",
                  "Stavropol", "Ulan-Ude", "Tver", "Ivanovo", "Bryansk", "Belgorod", "Surgut", "Vladimir",
                  "Arkhangelsk", "Chita", "Kaluga", "Smolensk", "Kurgan", "Cherepovets", "Oryol", "Saransk",
                  "Vologda", "Yakutsk", "Vladikavkaz", "Murmansk", "Grozny", "Tambov", "Petrozavodsk", "Kostroma",
                  "Yoshkar-Ola", "Syktyvkar", "Nalchik", "Blagoveshchensk", "Veliky Novgorod", "Pskov",
                  "Yuzhno-Sakhalinsk", "Abakan", "Petropavlovsk-Kamchatsky", "Maykop", "Cherkessk", "Nazran",
                  "Kyzyl", "Novy Urengoy", "Elista", "Khanty-Mansiysk", "Gatchina", "Magadan", "Birobidzhan",
                  "Gorno-Altaysk"]

        return random.choice(cities)

    # This is where your AI will decide what to do
    @overrides(UserClient)
    def take_turn(self, actions, city, disasters):
        actions.add_effort("Mandatory labor for everyone", sys.maxsize)

        glorious_fire_sensor = city.sensors[SensorType.fire_alarm]
        glorious_effort_allocation = ((2**11)-(23*89))  # complex algorithms
        actions.add_effort(glorious_fire_sensor, glorious_effort_allocation)

    @overrides(UserClient)
    def set_decree(self, my_decree):
        return "everyone to the gulag"
