class Leather:
    def __init__(self):
        self.name = "Leather Vest"
        self.statProtection = 2
        self.statMagicProtectChance = 3
        self.statWeaponProtectChance = 5
        self.moneyvalue = 10
        self.statSpecial = "light"
        #x1.3 to player speed

class Plate:
    def __init__(self):
        self.name = "Chest Plate"
        self.statProtection = 6
        self.statMagicProtectChance = 1
        self.statWeaponProtectChance = 2
        self.moneyvalue = 20
        self.statSpecial = "heavy"
        #x0.9 to player speed

class Chain:
    def __init__(self):
        self.name = "Chain Shirt"
        self.statProtection = 4
        self.statMagicProtectChance = 2
        self.statWeaponProtectChance = 4
        self.moneyvalue = 15
        self.statSpecial = "medium"
        #x1.1 to player speed

class Cloth:
    def __init__(self):
        self.name = "Cloth Tunic"
        self.statProtection = 1
        self.statMagicProtectChance = 9
        self.statWeaponProtectChance = 0
        self.moneyvalue = 5
        self.statSpecial = "loose"
        #immune to gob applied stat effects

#Global Vars including Typelist
class ArmorGlobalVars:
    ArmorBaseProtection = 0
    ArmorBaseMagicProtectChance = 0
    ArmorBaseProtectChance = 0
    ArmorBasemoneyvalue = 0
    GlobalArmorTypesList = [Leather(), Plate(), Chain(), Cloth()]