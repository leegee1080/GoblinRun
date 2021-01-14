   
#Weapons
class Dagger:
    def __init__(self, mod):
        self.cat = "weapon"
        self.name = "Dagger"
        self.statSpeed = 4
        self.statPierce = 3
        self.statDamage = 1
        self.statSpecial = "quick"
        #at one attack per dagger speed
        self.mod = [mod(0), mod(1)]
        self.name += mod(0)
        self.statSpeed *= mod(1)
        self.statPierce *= mod(1)
        self.statDamage *= mod(1)

class Sword:
    def __init__(self, mod):
        self.cat = "weapon"
        self.name = "Sword"
        self.statSpeed = 3
        self.statPierce = 3
        self.statDamage = 4
        self.statSpecial = "sweep"
        #attack hits all gobs lower level than the gob hit
        self.mod = [mod(0), mod(1)]
        self.name += mod(0)
        self.statSpeed *= mod(1)
        self.statPierce *= mod(1)
        self.statDamage *= mod(1)

class Axe:
    def __init__(self, mod):
        self.cat = "weapon"
        self.name = "Axe"
        self.statSpeed = 2
        self.statPierce = 3
        self.statDamage = 5
        self.statSpecial = "heavy"
        #attack hits all gobs higher level than the gob hit
        self.mod = [mod(0), mod(1)]
        self.name += mod(0)
        self.statSpeed *= mod(1)
        self.statPierce *= mod(1)
        self.statDamage *= mod(1)

class Spear:
    def __init__(self, mod):
        self.cat = "weapon"
        self.name = "Spear"
        self.statSpeed = 3
        self.statPierce = 5
        self.statDamage = 2
        self.statSpecial = "long"
        #avoid the next number of attacks equal to the pierce stat on this weapon
        self.mod = [mod(0), mod(1)]
        self.name += mod(0)
        self.statSpeed *= mod(1)
        self.statPierce *= mod(1)
        self.statDamage *= mod(1)
#Weapons End


#Armor
class Leather:
    def __init__(self, mod):
        self.cat = "armor"
        self.name = "Leather"
        self.statProtection = 2
        self.statMagicProtectChance = 3
        self.statWeaponProtectChance = 5
        self.statSpecial = "light"
        #x1.3 to player speed
        self.mod = [mod(0), mod(1)]
        self.name += mod(0)
        self.statProtection *= mod(1)
        self.statMagicProtectChance *= mod(1)
        self.statWeaponProtectChance *= mod(1)

class Plate:
    def __init__(self, mod):
        self.cat = "armor"
        self.name = "Plate"
        self.statProtection = 6
        self.statMagicProtectChance = 1
        self.statWeaponProtectChance = 2
        self.statSpecial = "heavy"
        #x0.9 to player speed
        self.mod = [mod(0), mod(1)]
        self.name += mod(0)
        self.statProtection *= mod(1)
        self.statMagicProtectChance *= mod(1)
        self.statWeaponProtectChance *= mod(1)

class Chain:
    def __init__(self, mod):
        self.cat = "armor"
        self.name = "Chain"
        self.statProtection = 4
        self.statMagicProtectChance = 2
        self.statWeaponProtectChance = 4
        self.statSpecial = "medium"
        #x1.1 to player speed
        self.mod = [mod(0), mod(1)]
        self.name += mod(0)
        self.statProtection *= mod(1)
        self.statMagicProtectChance *= mod(1)
        self.statWeaponProtectChance *= mod(1)

class Cloth:
    def __init__(self, mod):
        self.cat = "armor"
        self.name = "Cloth"
        self.statProtection = 1
        self.statMagicProtectChance = 9
        self.statWeaponProtectChance = 0
        self.statSpecial = "loose"
        #immune to gob applied stat effects
        self.mod = [mod(0), mod(1)]
        self.name += mod(0)
        self.statProtection *= mod(1)
        self.statMagicProtectChance *= mod(1)
        self.statWeaponProtectChance *= mod(1)
#Armor End


#Items
class HealthPot:
    def __init__(self, mod):
        self.cat = "potion"
        self.name = "Health Potion"
        self.Factor = 1
        self.statSpecial = "healing"
        self.mod = [mod(0), mod(1)]
        self.name += mod(0)
        self.Factor *= mod(1)

class DamagePot:
    def __init__(self, mod):
        self.cat = "potion"
        self.name = "Strength Potion"
        self.Factor = 1
        self.statSpecial = "damage"
        self.mod = [mod(0), mod(1)]
        self.name += mod(0)
        self.Factor *= mod(1)

class ImmuPot:
    def __init__(self, mod):
        self.cat = "potion"
        self.name = "Immunity Potion"
        self.Factor = 1
        self.statSpecial = "immune"
        self.mod = [mod(0), mod(1)]
        self.name += mod(0)
        self.Factor *= mod(1)
#Items End



class GlobalItemVars:

    #0 == name, 1 == stat boost
    ModSwitcher = (
    ("Poor", 0.5),
    ("Normal", 1),
    ("Expert", 2),
    ("Masterwork", 4),
    ("Legendary", 8)
    )

    GlobalItemList = (
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
        )