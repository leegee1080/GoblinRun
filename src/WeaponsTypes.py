class Dagger:
    def __init__(self):
        self.name = "Light Dagger"
        self.statSpeed = 4
        self.statPierce = 3
        self.statDamage = 1
        self.moneyvalue = 10
        self.statSpecial = "quick"
        #one attack per dagger speed

class Sword:
    def __init__(self):
        self.name = "Two-Handed Sword"
        self.statSpeed = 3
        self.statPierce = 3
        self.statDamage = 4
        self.moneyvalue = 10
        self.statSpecial = "sweep"
        #attack hits all gobs lower level than the gob hit

class Axe:
    def __init__(self):
        self.name = "Heavy Axe"
        self.statSpeed = 2
        self.statPierce = 3
        self.statDamage = 5
        self.moneyvalue = 10
        self.statSpecial = "heavy"
        #attack hits all gobs higher level than the gob hit

class Spear:
    def __init__(self):
        self.name = "Long Spear"
        self.statSpeed = 3
        self.statPierce = 5
        self.statDamage = 2
        self.moneyvalue = 10
        self.statSpecial = "long"
        #avoid the next number of attacks equal to the pierce stat on this weapon

#Global Vars including Typelist
class WeaponGlobalVars:
    WeaponBaseSpeed = 0
    WeaponBasePierce = 0
    WeaponBaseDamage = 0
    WeaponBasemoneyvalue = 0
    GlobalWeaponTypesList = [Dagger(), Sword(), Axe(), Spear()]