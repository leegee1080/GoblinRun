import random
from src.ConsumablesTypes import ConsumablesGlobalVars
from src.Items import ModList

class Weapon:
    def __init__(self, playlvl, difflvl):
        self.type = ConsumablesGlobalVars.GlobalConsumableTypesList[random.randint(0, len(ConsumablesGlobalVars.GlobalConsumableTypesList)-1)]
        self.chosenmod = ModList(playlvl, difflvl)
        self.mod = [self.chosenmod[0], self.chosenmod[1]]
        self.name = self.mod[0] + " " + self.type.name
        self.statFactor = (self.type.Factor + ConsumablesGlobalVars.ConsumableBaseFactor) * self.mod[1]
        self.moneyvalue = (self.type.moneyvalue + ConsumablesGlobalVars.ConsumableBasemoneyvalue) * self. mod[1]
    
    def printStatSheet(self):
        print("Type: " + self.name)
        print("Factor: " + str(self.statSpeed))
        print("Value: " + str(self.moneyvalue))
        return