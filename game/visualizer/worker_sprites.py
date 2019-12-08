import cocos
import random


class WorkerLayer(cocos.layer.Layer):
    def __init__(self, display_size, assets):
        self.size = display_size
        self.images = assets
        super().__init__()

        batch = cocos.batch.BatchNode()
        self.add(batch)

        for n in range(random.randint(0, 49)):
            x = random.randint(0, self.size[0])
            y = 100
            x = x - (x % 4)
            y = y - (y % 4)
            temp = self.images['normal'][n]
            temp.position = (x, y)
            batch.add(temp)

        for n in range(random.randint(0, 49)):
            x = random.randint(0, self.size[0])
            y = 100
            x = x - (x % 4)
            y = y - (y % 4)
            temp = self.images['hammer'][n]
            temp.position = (x, y)
            batch.add(temp)

        for n in range(random.randint(0, 49)):
            x = random.randint(0, self.size[0])
            y = 100
            x = x - (x % 4)
            y = y - (y % 4)
            temp = self.images['money'][n]
            temp.position = (x, y)
            batch.add(temp)

        for n in range(random.randint(0, 49)):
            x = random.randint(0, self.size[0])
            y = 100
            x = x - (x % 4)
            y = y - (y % 4)
            temp = self.images['pick'][n]
            temp.position = (x, y)
            batch.add(temp)

        for n in range(random.randint(0, 49)):
            x = random.randint(0, self.size[0])
            y = 100
            x = x - (x % 4)
            y = y - (y % 4)
            temp = self.images['phone'][n]
            temp.position = (x, y)
            batch.add(temp)

        self.batch = batch

