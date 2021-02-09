class HealthPot:
    def __init__(self):
        self.name = "Health Potion"
        self.Factor = 1
        self.moneyvalue = 10
        self.statSpecial = "healing"

class DamagePot:
    def __init__(self):
        self.name = "Strength Potion"
        self.Factor = 1
        self.moneyvalue = 10
        self.statSpecial = "damage boost"

class MagImmuPot:
    def __init__(self):
        self.name = "Magic Immunity Potion"
        self.Factor = 1
        self.moneyvalue = 10
        self.statSpecial = "magic immune"

#Global Vars including Typelist
class ConsumablesGlobalVars:
    ConsumableBaseFactor = 0
    ConsumableBasemoneyvalue = 0
    GlobalConsumableTypesList = [HealthPot(), DamagePot(), MagImmuPot()]
