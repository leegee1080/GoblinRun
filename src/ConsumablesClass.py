import random as ran
from src.ConsumablesTypes import ConsumablesGlobalVars
from src.Items import ModList

class Consumable:
    def __init__(self, playlvl, difflvl):
        self.cat = "c"
        self.type = ConsumablesGlobalVars.GlobalConsumableTypesList[ran.randint(0, len(ConsumablesGlobalVars.GlobalConsumableTypesList)-1)]
        self.effect = self.type.statSpecial
        self.chosenmod = ModList(playlvl, difflvl)
        self.mod = [self.chosenmod.newchosenmod[0], self.chosenmod.newchosenmod[1]]
        self.name = self.mod[0] + " " + self.type.name
        self.statFactor = (self.type.Factor + ConsumablesGlobalVars.ConsumableBaseFactor) * self.mod[1]
        self.moneyvalue = (self.type.moneyvalue + ConsumablesGlobalVars.ConsumableBasemoneyvalue) * self. mod[1]
    
    def printStatSheet(self):
        print("Type: " + self.name)
        print("Factor: " + str(self.chosenmod.newchosenmod[0]))
        print("Value: " + str(self.moneyvalue))
        return