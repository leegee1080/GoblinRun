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
        self.speed = GlobalGoblinVars.GlobalGoblinBaseStatsList["Spe"] + self.type.statSpeed * (level/2)
        self.health = GlobalGoblinVars.GlobalGoblinBaseStatsList["Hea"] + self.type.statHealth * (level/2)
        self.armor = GlobalGoblinVars.GlobalGoblinBaseStatsList["Arm"] + self.type.statArmor
        self.damage = GlobalGoblinVars.GlobalGoblinBaseStatsList["Dam"] + self.type.statDamage * (level/2)
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
        self.tempDam = (amount*self.armor)
        print("The goblin takes {}.".format(int(self.tempDam)))
        self.health -= self.tempDam
        if (self.health <= 0):
            print("You killed it!\n")
            self.alive = False
