# __all__ = ['GlobalGoblinVars']

class WeaponMods:
        ModDict = {
            "Rusty": 0,
            "Normal": 1,
            "Sharp": 2,
            "Masterwork": 3,
            "Legendary": 4
        }


class Dagger:
    def __init__(self):
        self.name = "Dagger"
        self.statSpeed = 4
        self.statPierce = 6
        self.statDamage = 3
        self.statSpecial = "Quick"


class Sword:
    def __init__(self):
        self.name = "Sword"
        self.statSpeed = 3
        self.statPierce = 8
        self.statDamage = 8
        self.statSpecial = "Sweep"


class Axe:
    def __init__(self):
        self.name = "Axe"
        self.statSpeed = 8
        self.statPierce = 3
        self.statDamage = 3
        self.statSpecial = "Heavy"


class Spear:
    def __init__(self):
        self.name = "Spear"
        self.statSpeed = 0
        self.statPierce = 5
        self.statDamage = 5
        self.statSpecial = "Long"


#Global Vars including Typelist
class GlobalItemVars:
    WeaponBaseSpeed = 0
    WeaponBasePierce = 0
    WeaponBaseDamage = 1
    GlobalWeaponTypesList = [Dagger(), Sword(), Axe(), Spear()]
