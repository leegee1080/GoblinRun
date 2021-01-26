import math
import random

class ModList:
    ModSwitcher = [
    ("Poor", 0.5),
    ("Normal", 1),
    ("Expert", 2),
    ("Masterwork", 4),
    ("Legendary", 8)
    ]
    
    def __init__(self, playlvl, difflvl):
        self.newchosenmod = None
        self.diff = difflvl * 10
        self.ranlower = math.floor(playlvl/self.diff)
        if(self.ranlower > (len(self.ModSwitcher)-1)):
            self.ranlower = (len(self.ModSwitcher))

        self.ranupper = round(playlvl/self.diff + self.ranlower)
        if(self.ranupper > (len(self.ModSwitcher)-1)):
            self.ranupper = (len(self.ModSwitcher))

        self.newchosenmod = self.ModSwitcher[random.randint(self.ranlower, self.ranupper)]