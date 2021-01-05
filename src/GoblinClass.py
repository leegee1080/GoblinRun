# from GoblinTypes import Slimy
# from GoblinTypes import Tough
# from GoblinTypes import Slow
# from GoblinTypes import Fast
# from GoblinTypes import Normal
# from GoblinTypes import Dumb
from src.GoblinTypes import GlobalGoblinVars
# from GoblinTypes import *

class Goblin:
    StatSheetForPrint = []

    def __init__(self, newtype, level):
        self.type = GlobalGoblinVars.GlobalGoblinTypesList[newtype]
        self.level = level
        self.speed = GlobalGoblinVars.GlobalGoblinBaseStatsList["Spe"] + self.type.statSpeed + level
        self.health = GlobalGoblinVars.GlobalGoblinBaseStatsList["Arm"] + self.type.statSpeed + level
        self.armor = GlobalGoblinVars.GlobalGoblinBaseStatsList["Hea"] + self.type.statSpeed + level
        self.damage = GlobalGoblinVars.GlobalGoblinBaseStatsList["Dam"] + self.type.statSpeed + level
        self.effect = self.type.appliedEffect

    
    def printStatSheet(self):
        self.StatSheetForPrint.clear
        self.StatSheetForPrint.append("Type: " + self.type.name)
        self.StatSheetForPrint.append("Level: " + str(self.level))
        self.StatSheetForPrint.append("Speed: " + str(self.speed))
        self.StatSheetForPrint.append("Armor: " + str(self.armor))
        self.StatSheetForPrint.append("Health: " + str(self.health))
        self.StatSheetForPrint.append("Damage: " + str(self.damage))
        self.StatSheetForPrint.append("Effect: " + str(self.effect))
        print(self.StatSheetForPrint)
        return