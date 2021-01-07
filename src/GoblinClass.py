# from GoblinTypes import Slimy
# from GoblinTypes import Tough
# from GoblinTypes import Slow
# from GoblinTypes import Fast
# from GoblinTypes import Normal
# from GoblinTypes import Dumb
import random
from src.GoblinTypes import GlobalGoblinVars
# from GoblinTypes import *

class Goblin:
    def __init__(self, level):
        self.type = GlobalGoblinVars.GlobalGoblinTypesList[random.randint(0, len(GlobalGoblinVars.GlobalGoblinTypesList)-1)]
        self.level = level
        self.speed = GlobalGoblinVars.GlobalGoblinBaseStatsList["Spe"] + self.type.statSpeed + level
        self.health = GlobalGoblinVars.GlobalGoblinBaseStatsList["Arm"] + self.type.statSpeed + level
        self.armor = GlobalGoblinVars.GlobalGoblinBaseStatsList["Hea"] + self.type.statSpeed + level
        self.damage = GlobalGoblinVars.GlobalGoblinBaseStatsList["Dam"] + self.type.statSpeed + level
        self.effect = self.type.appliedEffect
        self.alive = True

    
    def printStatSheet(self):
        print("Type: " + self.type.name)
        print("Level: " + str(self.level))
        print("Speed: " + str(self.speed))
        print("Armor: " + str(self.armor))
        print("Health: " + str(self.health))
        print("Damage: " + str(self.damage))
        print("Effect: " + str(self.effect))
        return

    def takedamage(self, amount):
        self.health -= amount
        if (self.health <= 0):
            self.alive = False
