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
        self.statSpecial = "damage"

class ImmuPot:
    def __init__(self):
        self.name = "Immunity Potion"
        self.Factor = 1
        self.moneyvalue = 10
        self.statSpecial = "immune"

#Global Vars including Typelist
class ConsumablesGlobalVars:
    ConsumableBaseFactor = 0
    ConsumableBasemoneyvalue = 0
    GlobalConsumableTypesList = [HealthPot(), DamagePot(), ImmuPot()]