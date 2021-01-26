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


class NewItem:
    #0 == name, 1 == stat boost
    ModSwitcher = [
    ("Poor", 0.5),
    ("Normal", 1),
    ("Expert", 2),
    ("Masterwork", 4),
    ("Legendary", 8)
    ]


    GlobalItemList = [
        # Dagger(),
        # Sword(),
        # Spear(),
        # Axe(),
        # Leather(),
        # Plate(),
        # Chain(),
        # Cloth(),
        #HealthPot(),
        #DamagePot(),
        #ImmuPot()
        ]


    def randomGenItem(self, playlvl, difflvl, cat):
        self.catlist = []
        self.newItem = None
        self.name = ""
        if str(cat) != "none":
            for i in self.GlobalItemList:
                if i.cat == cat:
                    self.catlist.append(i)
        else:
            for i in self.GlobalItemList:
                    self.catlist.append(i)

        self.diff = difflvl * 10
        self.ranlower = math.floor(playlvl/self.diff)
        if(self.ranlower > (len(self.ModSwitcher)-1)):
            self.ranlower = (len(self.ModSwitcher)-1)

        self.ranupper = round(playlvl/self.diff + self.ranlower)
        if(self.ranupper > (len(self.ModSwitcher)-1)):
            self.ranupper = (len(self.ModSwitcher)-1)

        self.chosenmod = self.ModSwitcher[random.randint(self.ranlower, self.ranupper)]
        self.newItem = self.catlist[random.randint(0,len(self.catlist)-1)]

        self.newItem.applymod(self.chosenmod)
        return 

    def __init__(self, currentplayerlevel, difficultylevel, category):
        self.randomGenItem(currentplayerlevel, difficultylevel, category)

        #apply the stats to this object to make them printable
        self.name = self.newItem.modName
        return