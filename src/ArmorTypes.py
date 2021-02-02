#lower the protection number the better
#protect chances are out of 100

class Leather:
    def __init__(self):
        self.name = "Leather Vest"
        self.statProtection = 0.7
        self.statMagicProtectChance = 30
        self.statWeaponProtectChance = 30
        self.moneyvalue = 10
        self.statSpecial = ("light", 1.4)
        #x1.3 to player speed

class Plate:
    def __init__(self):
        self.name = "Chest Plate"
        self.statProtection = 0.3
        self.statMagicProtectChance = 10
        self.statWeaponProtectChance = 20
        self.moneyvalue = 20
        self.statSpecial = ("heavy", 0.9)
        #x0.9 to player speed

class Chain:
    def __init__(self):
        self.name = "Chain Shirt"
        self.statProtection = 0.5
        self.statMagicProtectChance = 20
        self.statWeaponProtectChance = 25
        self.moneyvalue = 15
        self.statSpecial = ("medium", 1.1)
        #x1.1 to player speed

class Cloth:
    def __init__(self):
        self.name = "Cloth Tunic"
        self.statProtection = 0.9
        self.statMagicProtectChance = 100
        self.statWeaponProtectChance = 10
        self.moneyvalue = 5
        self.statSpecial = ("loose", 1)
        #immune to gob applied stat effects

#Global Vars including Typelist
class ArmorGlobalVars:
    ArmorBaseProtection = 0
    ArmorBaseMagicProtectChance = 0
    ArmorBaseProtectChance = 0
    ArmorBasemoneyvalue = 0
    GlobalArmorTypesList = [Leather(), Plate(), Chain(), Cloth()]