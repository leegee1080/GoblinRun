   
#Weapons
class Dagger:
    def __init__(self):
        self.name = "Dagger"
        self.statSpeed = 4
        self.statPierce = 3
        self.statDamage = 3
        self.statSpecial = "Quick"
        #at one attack per dagger speed


class Sword:
    def __init__(self):
        self.name = "Sword"
        self.statSpeed = 3
        self.statPierce = 3
        self.statDamage = 4
        self.statSpecial = "Sweep"
        #attack hits all gobs lower level than the gob hit


class Axe:
    def __init__(self):
        self.name = "Axe"
        self.statSpeed = 2
        self.statPierce = 3
        self.statDamage = 5
        self.statSpecial = "Heavy"
        #attack hits all gobs higher level than the gob hit


class Spear:
    def __init__(self):
        self.name = "Spear"
        self.statSpeed = 3
        self.statPierce = 5
        self.statDamage = 2
        self.statSpecial = "Long"
        #avoid the next number of attacks equal to the pierce stat on this weapon
#Weapons End

#Armor
class Leather:
    def __init__(self):
        self.name = "Leather"
        self.statProtection = 2
        self.statMagicProtectChance = 3
        self.statWeaponProtectChance = 5
        self.statSpecial = "Light"
        #x1.3 to player speed

class Plate:
    def __init__(self):
        self.name = "Plate"
        self.statProtection = 6
        self.statMagicProtectChance = 1
        self.statWeaponProtectChance = 2
        self.statSpecial = "Heavy"
        #x0.9 to player speed

class Chain:
    def __init__(self):
        self.name = "Chain"
        self.statProtection = 4
        self.statMagicProtectChance = 2
        self.statWeaponProtectChance = 4
        self.statSpecial = "Medium"
        #x1.1 to player speed

class Cloth:
    def __init__(self):
        self.name = "Cloth"
        self.statProtection = 1
        self.statMagicProtectChance = 9
        self.statWeaponProtectChance = 0
        self.statSpecial = "Loose"
        #immune to gob applied stat effects
#Armor End


class GlobalItemVars:

    #1 == name, 2 == stat boost
    ModSwitcher = [
    {1: "Rusty", 2: 0},
    {1: "Normal", 2: 1},
    {1: "Sharp", 2: 2},
    {1: "Masterwork", 2: 3},
    {1: "Legendary", 2: 4}
    ]

    WeaponBaseSpeed = 0
    WeaponBasePierce = 0
    WeaponBaseDamage = 1

    ArmorBaseProtection = 1
    ArmorBaseMagicProtectChance = 0
    ArmorBaseWeaponProtectChance = 0

    GlobalItemList = [
        Dagger(),
        Sword(),
        Spear(),
        Axe(),
        Leather(),
        Plate(),
        Chain(),
        Cloth()
        ]