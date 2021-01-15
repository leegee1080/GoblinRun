import math
import random


#Weapons
class Dagger:
    def __init__(self):
        self.cat = "weapon"
        self.name = "Dagger"
        self.statSpeed = 4
        self.statPierce = 3
        self.statDamage = 1
        self.statSpecial = "quick"
        #one attack per dagger speed
    def applymod(self, mod):
        self.mod = [mod[0], mod[1]]
        self.name = mod[0] + " " + self.name
        self.statSpeed *= mod[1]
        self.statPierce *= mod[1]
        self.statDamage *= mod[1]

class Sword:
    def __init__(self):
        self.cat = "weapon"
        self.name = "Sword"
        self.statSpeed = 3
        self.statPierce = 3
        self.statDamage = 4
        self.statSpecial = "sweep"
        #attack hits all gobs lower level than the gob hit
    def applymod(self, mod):
        self.mod = [mod[0], mod[1]]
        self.name = mod[0] + " " + self.name
        self.statSpeed *= mod[1]
        self.statPierce *= mod[1]
        self.statDamage *= mod[1]

class Axe:
    def __init__(self):
        self.cat = "weapon"
        self.name = "Axe"
        self.statSpeed = 2
        self.statPierce = 3
        self.statDamage = 5
        self.statSpecial = "heavy"
        #attack hits all gobs higher level than the gob hit
    def applymod(self, mod):
        self.mod = [mod[0], mod[1]]
        self.name = mod[0] + " " + self.name
        self.statSpeed *= mod[1]
        self.statPierce *= mod[1]
        self.statDamage *= mod[1]

class Spear:
    def __init__(self):
        self.cat = "weapon"
        self.name = "Spear"
        self.statSpeed = 3
        self.statPierce = 5
        self.statDamage = 2
        self.statSpecial = "long"
        #avoid the next number of attacks equal to the pierce stat on this weapon
    def applymod(self, mod):
        self.mod = [mod[0], mod[1]]
        self.name = mod[0] + " " + self.name
        self.statSpeed *= mod[1]
        self.statPierce *= mod[1]
        self.statDamage *= mod[1]
#Weapons End


#Armor
class Leather:
    def __init__(self):
        self.cat = "armor"
        self.name = "Leather Armor"
        self.statProtection = 2
        self.statMagicProtectChance = 3
        self.statWeaponProtectChance = 5
        self.statSpecial = "light"
        #x1.3 to player speed
    def applymod(self, mod):
        self.mod = [mod[0], mod[1]]
        self.name = mod[0] + " " + self.name
        self.statProtection *= mod[1]
        self.statMagicProtectChance *= mod[1]
        self.statWeaponProtectChance *= mod[1]

class Plate:
    def __init__(self):
        self.cat = "armor"
        self.name = "Plate Chest Piece"
        self.statProtection = 6
        self.statMagicProtectChance = 1
        self.statWeaponProtectChance = 2
        self.statSpecial = "heavy"
        #x0.9 to player speed
    def applymod(self, mod):
        self.mod = [mod[0], mod[1]]
        self.name = mod[0] + " " + self.name
        self.statProtection *= mod[1]
        self.statMagicProtectChance *= mod[1]
        self.statWeaponProtectChance *= mod[1]

class Chain:
    def __init__(self):
        self.cat = "armor"
        self.name = "Chain Shirt"
        self.statProtection = 4
        self.statMagicProtectChance = 2
        self.statWeaponProtectChance = 4
        self.statSpecial = "medium"
        #x1.1 to player speed
    def applymod(self, mod):
        self.mod = [mod[0], mod[1]]
        self.name = mod[0] + " " + self.name
        self.statProtection *= mod[1]
        self.statMagicProtectChance *= mod[1]
        self.statWeaponProtectChance *= mod[1]

class Cloth:
    def __init__(self):
        self.cat = "armor"
        self.name = "Cloth Tunic"
        self.statProtection = 1
        self.statMagicProtectChance = 9
        self.statWeaponProtectChance = 0
        self.statSpecial = "loose"
        #immune to gob applied stat effects
    def applymod(self, mod):
        self.mod = [mod[0], mod[1]]
        self.name = mod[0] + " " + self.name
        self.statProtection *= mod[1]
        self.statMagicProtectChance *= mod[1]
        self.statWeaponProtectChance *= mod[1]
#Armor End


#Items
class HealthPot:
    def __init__(self):
        self.cat = "potion"
        self.name = "Health Potion"
        self.Factor = 1
        self.statSpecial = "healing"
    def applymod(self, mod):
        self.mod = [mod[0], mod[1]]
        self.name = mod[0] + " " + self.name
        self.Factor *= mod[1]

class DamagePot:
    def __init__(self):
        self.cat = "potion"
        self.name = "Strength Potion"
        self.Factor = 1
        self.statSpecial = "damage"
    def applymod(self, mod):
        self.mod = [mod[0], mod[1]]
        self.name = mod[0] + " " + self.name
        self.Factor *= mod[1]

class ImmuPot:
    def __init__(self):
        self.cat = "potion"
        self.name = "Immunity Potion"
        self.Factor = 1
        self.statSpecial = "immune"
    def applymod(self, mod):
        self.mod = [mod[0], mod[1]]
        self.name = mod[0] + " " + self.name
        self.Factor *= mod[1]
#Items End



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
        Dagger(),
        Sword(),
        Spear(),
        Axe(),
        Leather(),
        Plate(),
        Chain(),
        Cloth(),
        HealthPot(),
        DamagePot(),
        ImmuPot()
        ]

    def randomGenItem(self, playlvl, difflvl, cat):
        self.catlist = []

        if str(cat) != "none":
            for i in self.GlobalItemList:
                if i.cat == cat:
                    self.catlist.append(i)


        self.diff = difflvl * 10
        self.ranlower = math.floor(playlvl/self.diff)
        if(self.ranlower > (len(self.ModSwitcher)-1)):
            self.ranlower = (len(self.ModSwitcher)-1)

        self.ranupper = round(playlvl/self.diff + self.ranlower)
        if(self.ranupper > (len(self.ModSwitcher)-1)):
            self.ranupper = (len(self.ModSwitcher)-1)

        self.chosenmod = self.ModSwitcher[random.randint(self.ranlower, self.ranupper)]
        self.newItem = self.GlobalItemList[random.randint(0,len(self.GlobalItemList)-1)]

        self.newItem.applymod(self.chosenmod)
        return 

    def __init__(self, currentplayerlevel, difficultylevel, category):
        self.randomGenItem(currentplayerlevel, difficultylevel, category)

        #apply the stats to this object to make them printable
        self.name = self.newItem.name
        return