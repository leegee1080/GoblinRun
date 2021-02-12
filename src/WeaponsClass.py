import random
from src.WeaponsTypes import WeaponGlobalVars
from src.Items import ModList

class Weapon:
    def __init__(self, playlvl, difflvl):
        self.cat = "w"
        self.type = WeaponGlobalVars.GlobalWeaponTypesList[random.randint(0, len(WeaponGlobalVars.GlobalWeaponTypesList)-1)]
        self.chosenmod = ModList(playlvl, difflvl)
        self.mod = [self.chosenmod.newchosenmod[0], self.chosenmod.newchosenmod[1]]
        self.name = self.mod[0] + " " + self.type.name
        self.statSpeed = (self.type.statSpeed + WeaponGlobalVars.WeaponBaseSpeed) * self.mod[1]
        self.statPierce = (self.type.statPierce + WeaponGlobalVars.WeaponBasePierce) * self.mod[1]
        self.statDamage = (self.type.statDamage + WeaponGlobalVars.WeaponBaseDamage) * self.mod[1]
        self.moneyvalue = (self.type.moneyvalue + WeaponGlobalVars.WeaponBasemoneyvalue) * self. mod[1]
        self.statSpecial = self.type.statSpecial
    
    def __str__(self):
        return f"Type: {self.name}\nSpeed: {self.statSpeed}\nPierce: {self.statPierce}\nDamage: {self.statDamage}\nEffect: {self.statSpecial}\nValue: {self.moneyvalue}"

    # def printStatSheet(self):
    #     print("Type: " + self.name)
    #     print("Speed: " + str(self.statSpeed))
    #     print("Pierce: " + str(self.statPierce))
    #     print("Damage: " + str(self.statDamage))
    #     print("Effect: " + str(self.statSpecial))
    #     print("Value: " + str(self.moneyvalue))
    #     return