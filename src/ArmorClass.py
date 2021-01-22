import random
from src.ArmorTypes import ArmorGlobalVars
from src.Items import ModList

class Weapon:
    def __init__(self, playlvl, difflvl):
        self.type = ArmorGlobalVars.GlobalArmorTypesList[random.randint(0, len(ArmorGlobalVars.GlobalArmorTypesList)-1)]
        self.chosenmod = ModList(playlvl, difflvl)
        self.mod = [self.chosenmod[0], self.chosenmod[1]]
        self.name = self.mod[0] + " " + self.type.name
        self.statProtection = (self.type.statProtection + ArmorGlobalVars.ArmorBaseProtection) * self.mod[1]
        self.statWeaponProtectChance = (self.type.statWeaponProtectChance + ArmorGlobalVars.ArmorBaseProtectChance) * self.mod[1]
        self.statMagicProtectChance = (self.type.statMagicProtectChance + ArmorGlobalVars.ArmorBaseMagicProtectChance) * self.mod[1]
        self.moneyvalue = (self.type.moneyvalue + ArmorGlobalVars.ArmorBasemoneyvalue) * self. mod[1]
        self.statSpecial = self.type.statSpecial
    
    def printStatSheet(self):
        print("Type: " + self.name)
        print("Protection: " + str(self.statProtection))
        print("WeaponProtectChance: " + str(self.statWeaponProtectChance))
        print("MagicProtectChance: " + str(self.statMagicProtectChance))
        print("Effect: " + str(self.statSpecial))
        print("Value: " + str(self.moneyvalue))
        return