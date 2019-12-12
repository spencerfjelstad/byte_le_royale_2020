import cocos
import pyglet
import os
import shutil
from zipfile import ZipFile
from PIL import Image
import numpy as np
import random
from game.visualizer.colors import *

# Extract all images from launcher.pyz and save them in a temp directory
if not os.path.exists(".temp"):
    os.mkdir(".temp")
with ZipFile("launcher.pyz",'r') as archive:
    name_list = archive.namelist()
    for fileName in name_list:
        if fileName.endswith('.png'):
            archive.extract(fileName, ".temp")

# Color replacer
def replace_colors(filename, start_colors, end_colors):
    im = Image.open(filename)
    data = np.array(im)
    for i in range(len(start_colors)):
        r1,g1,b1 = start_colors[i]
        red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
        mask = (red == r1) & (green == g1) & (blue == b1)
        data[:,:,:3][mask] = end_colors[i]
    img = Image.fromarray(data)
    if not os.path.exists('tempic'):
        os.mkdir('tempic')
    img.save("tempic/tempimage.png")
    pic = pyglet.image.load("tempic/tempimage.png")
    shutil.rmtree("tempic")
    return(pic)

# Populates a dictionary with all the sprites required for the visualizer
def load(temp):
    assets = temp
    plains = cocos.sprite.Sprite("game/visualizer/assets/location_assets/location_plains.png")
    assets['location'] = {
        "0": plains
    }

    # City assets
    city_0 = cocos.sprite.Sprite("game/visualizer/assets/city_assets/city_level0.png")
    city_1 = cocos.sprite.Sprite("game/visualizer/assets/city_assets/city_level1.png")
    city_2 = cocos.sprite.Sprite("game/visualizer/assets/city_assets/city_level2.png")
    city_3 = cocos.sprite.Sprite("game/visualizer/assets/city_assets/city_level3.png")
    assets['city'] = {
        "0": city_0,
        "1": city_1,
        "2": city_2,
        "3": city_3
    }

    # Disaster assets
    dis_fire = cocos.sprite.Sprite("game/visualizer/assets/disaster_assets/fire.png")
    dis_tornado = cocos.sprite.Sprite("game/visualizer/assets/disaster_assets/tornado.png")
    dis_blizzard = cocos.sprite.Sprite("game/visualizer/assets/disaster_assets/blizzard.png")
    dis_earthquake = cocos.sprite.Sprite("game/visualizer/assets/disaster_assets/earthquake.png")
    dis_monster = cocos.sprite.Sprite("game/visualizer/assets/disaster_assets/monster.png")
    dis_ufo = cocos.sprite.Sprite("game/visualizer/assets/disaster_assets/ufo.png")
    assets['disaster'] = {
        "fire": dis_fire,
        "tornado": dis_tornado,
        "blizzard": dis_blizzard,
        "earthquake": dis_earthquake,
        "monster": dis_monster,
        "ufo": dis_ufo
    }

    # Forecast assets
    assets['forecast'] = {}
    assets['forecast']['fire'] = list()
    assets['forecast']['tornado'] = list()
    assets['forecast']['blizzard'] = list()
    assets['forecast']['earthquake'] = list()
    assets['forecast']['monster'] = list()
    assets['forecast']['ufo'] = list()
    assets['forecast']['clear'] = list()
    for i in range(5):
        fore_fire = cocos.sprite.Sprite("game/visualizer/assets/forecast_assets/tape_fire.png")
        fore_tornado = cocos.sprite.Sprite("game/visualizer/assets/forecast_assets/tape_tornado.png")
        fore_blizzard = cocos.sprite.Sprite("game/visualizer/assets/forecast_assets/tape_blizzard.png")
        fore_earthquake = cocos.sprite.Sprite("game/visualizer/assets/forecast_assets/tape_earthquake.png")
        fore_monster = cocos.sprite.Sprite("game/visualizer/assets/forecast_assets/tape_monster.png")
        fore_ufo = cocos.sprite.Sprite("game/visualizer/assets/forecast_assets/tape_ufo.png")
        fore_clear = cocos.sprite.Sprite("game/visualizer/assets/forecast_assets/tape_clear.png")
        assets['forecast']['fire'].append(fore_fire)
        assets['forecast']['tornado'].append(fore_tornado)
        assets['forecast']['blizzard'].append(fore_blizzard)
        assets['forecast']['earthquake'].append(fore_earthquake)
        assets['forecast']['monster'].append(fore_monster)
        assets['forecast']['ufo'].append(fore_ufo)
        assets['forecast']['clear'].append(fore_clear)


    # Sensor assets
    assets['sensor'] = {
        "0":{},
        "1":{},
        "2":{},
        "3":{},
        "4":{},
        "5":{},
    }
    sensor_colors = {
        0 : COLOR.red,
        1 : COLOR.black,
        2 : COLOR.blue,
        3 : COLOR.brown,
        4 : COLOR.green,
        5 : COLOR.gray,
    }
    for i in range(6):
        sensor = replace_colors("game/visualizer/assets/sensor_assets/fire_alarm.png",[COLOR.red],[sensor_colors[i]])
        sensor_grid = pyglet.image.ImageGrid(sensor, 1, 2)
        level_0 = cocos.sprite.Sprite(pyglet.image.Animation.from_image_sequence(sensor_grid[0::], 0.1))
        level_1 = cocos.sprite.Sprite(pyglet.image.Animation.from_image_sequence(sensor_grid[0::], 0.1))
        level_2 = cocos.sprite.Sprite(pyglet.image.Animation.from_image_sequence(sensor_grid[0::], 0.1))
        level_3 = cocos.sprite.Sprite(pyglet.image.Animation.from_image_sequence(sensor_grid[0::], 0.1))
        assets['sensor'][str(i)].update({"0": level_0})
        assets['sensor'][str(i)].update({"1": level_1})
        assets['sensor'][str(i)].update({"2": level_2})
        assets['sensor'][str(i)].update({"3": level_3})


    # Decree assets
    decree_0 = cocos.sprite.Sprite("game/visualizer/assets/decree_assets/anti_fire_dogs.png")
    decree_1 = cocos.sprite.Sprite("game/visualizer/assets/decree_assets/paperweights.png")
    decree_2 = cocos.sprite.Sprite("game/visualizer/assets/decree_assets/snow_shovels.png")
    decree_3 = cocos.sprite.Sprite("game/visualizer/assets/decree_assets/rubber_boots.png")
    decree_4 = cocos.sprite.Sprite("game/visualizer/assets/decree_assets/fishing_hook.png")
    decree_5 = cocos.sprite.Sprite("game/visualizer/assets/decree_assets/cheese.png")
    decree_default = cocos.sprite.Sprite("game/visualizer/assets/decree_assets/decree_default.png")
    assets['decree'] = {
        "-1": decree_default,
        "0": decree_0,
        "1": decree_1,
        "2": decree_2,
        "3": decree_3,
        "4": decree_4,
        "5": decree_5
    }

    # Worker assets
    wrkr_colors = [[255, 255, 255], [169, 169, 169], [120, 120, 120], [67, 67, 67], [88, 88, 88]]
    skin_colors = [COLOR.russet,COLOR.peru,COLOR.fawn,COLOR.apricot,COLOR.white]
    shirt_1_colors = [COLOR.red,COLOR.magenta,COLOR.blue,COLOR.cyan,COLOR.lime,COLOR.yellow,COLOR.silver]
    shirt_2_colors = [COLOR.maroon,COLOR.olive,COLOR.green,COLOR.purple,COLOR.teal,COLOR.navy]
    pants_colors = [COLOR.khaki,COLOR.denim,COLOR.denim2,COLOR.gray]
    shoe_colors = [COLOR.brown,COLOR.cocoa,COLOR.black]

    assets['worker'] = {}
    assets['worker']['normal'] = list()
    assets['worker']['hammer'] = list()
    assets['worker']['money'] = list()
    assets['worker']['pick'] = list()
    assets['worker']['phone'] = list()
    wrkr_total = 100
    for i in range(wrkr_total):
        wrkr = replace_colors("game/visualizer/assets/worker.png",wrkr_colors,[random.choice(skin_colors),
                                                                               random.choice(shirt_1_colors),
                                                                               random.choice(shirt_2_colors),
                                                                               random.choice(pants_colors),
                                                                               random.choice(shoe_colors)])
        wrkr_grid = pyglet.image.ImageGrid(wrkr, 1, 48)
        if i < wrkr_total/5:
            wrkr_normal = pyglet.image.Animation.from_image_sequence(wrkr_grid[0:15:], 0.1, loop=True)
            sprite = cocos.sprite.Sprite(wrkr_normal)
            assets['worker']['normal'].append(sprite)
        elif i < wrkr_total*2/5:
            wrkr_hammer = pyglet.image.Animation.from_image_sequence(wrkr_grid[16:23:], 0.1, loop=True)
            sprite = cocos.sprite.Sprite(wrkr_hammer)
            assets['worker']['hammer'].append(sprite)
        elif i < wrkr_total*3/5:
            wrkr_money = pyglet.image.Animation.from_image_sequence(wrkr_grid[24:31:], 0.1, loop=True)
            sprite = cocos.sprite.Sprite(wrkr_money)
            assets['worker']['money'].append(sprite)
        elif i < wrkr_total*4/5:
            wrkr_pick = pyglet.image.Animation.from_image_sequence(wrkr_grid[32:39:], 0.1, loop=True)
            sprite = cocos.sprite.Sprite(wrkr_pick)
            assets['worker']['pick'].append(sprite)
        else:
            wrkr_phone = pyglet.image.Animation.from_image_sequence(wrkr_grid[40:47:], 0.1, loop=True)
            sprite = cocos.sprite.Sprite(wrkr_phone)
            assets['worker']['phone'].append(sprite)
    return assets


shutil.rmtree(".temp")
