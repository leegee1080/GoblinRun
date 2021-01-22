import math
import random

#Items
class HealthPot:
    def __init__(self):
        self.cat = "potion"
        self.name = "Health Potion"
        self.Factor = 1
        self.moneyvalue = 10
        self.statSpecial = "healing"
    def applymod(self, mod):
        self.mod = [mod[0], mod[1]]
        self.modName = mod[0] + " " + self.name
        self.Factor *= mod[1]
        self.moneyvalue *= mod[1]

class DamagePot:
    def __init__(self):
        self.cat = "potion"
        self.name = "Strength Potion"
        self.Factor = 1
        self.moneyvalue = 10
        self.statSpecial = "damage"
    def applymod(self, mod):
        self.mod = [mod[0], mod[1]]
        self.modName = mod[0] + " " + self.name
        self.Factor *= mod[1]
        self.moneyvalue *= mod[1]

class ImmuPot:
    def __init__(self):
        self.cat = "potion"
        self.name = "Immunity Potion"
        self.Factor = 1
        self.moneyvalue = 10
        self.statSpecial = "immune"
    def applymod(self, mod):
        self.mod = [mod[0], mod[1]]
        self.modName = mod[0] + " " + self.name
        self.Factor *= mod[1]
        self.moneyvalue *= mod[1]
#Items End

class ModList:
    ModSwitcher = [
    ("Poor", 0.5),
    ("Normal", 1),
    ("Expert", 2),
    ("Masterwork", 4),
    ("Legendary", 8)
    ]
    
    def __init__(self, playlvl, difflvl):
        self.chosenmod = None
        self.diff = difflvl * 10
        self.ranlower = math.floor(playlvl/self.diff)
        if(self.ranlower > (len(self.ModSwitcher)-1)):
            self.ranlower = (len(self.ModSwitcher)-1)

        self.ranupper = round(playlvl/self.diff + self.ranlower)
        if(self.ranupper > (len(self.ModSwitcher)-1)):
            self.ranupper = (len(self.ModSwitcher)-1)

        self.chosenmod = self.ModSwitcher[random.randint(self.ranlower, self.ranupper)]


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
        HealthPot(),
        DamagePot(),
        ImmuPot()
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