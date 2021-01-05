class Player:
    StatSheetForPrint = []

    def __init__(self, level, speed, startingHealth, strength, currentXp, XpToLevel):
        self.level = level
        self.speed = speed
        self.health = startingHealth
        self.maxHealth = startingHealth
        self.strength = strength
        self.currentXp = currentXp
        self.XpToLevel = XpToLevel
    
    def printStatSheet(self):
        self.StatSheetForPrint.clear
        self.StatSheetForPrint.append("Level: " + str(self.level))
        self.StatSheetForPrint.append("Speed: " + str(self.speed))
        self.StatSheetForPrint.append("Max Health: " + str(self.maxHealth))
        self.StatSheetForPrint.append("Current Health: " + str(self.health))
        self.StatSheetForPrint.append("Strength: " + str(self.strength))
        self.StatSheetForPrint.append("Experience: {} out of {} till next level.".format(self.currentXp, self.XpToLevel))
        print(self.StatSheetForPrint)
        return
    
    def increaseStrength(self, Amount):
        self.strength = self.strength + Amount
        print("Strength went up!")
        return
    
    def increaseSpeed(self, Amount):
        self.speed = self.speed + Amount
        print("Speed went up!")
        return

    def increaseHealth(self, Amount):
        self.maxHealth = self.maxHealth + Amount
        print("Max Health went up!")
        return

    def increaseLevel(self, Amount):
        self.level = self.level + Amount
        print("Level went up!")
        return
    
    def HealPlayer(self, Amount):
        healthDif = self.maxHealth - self.health
        if Amount <= healthDif:
            self.health = self.health + Amount
            print("Healed: " + str(Amount))
        else:
            self.health = self.maxHealth
            print("Full Health!")
        return
    
    def DamagePlayer(self, Amount):
        self.health = self.health - Amount
        if self.health <= 0:
            print("player dead")
        return
    
    def LevelUp(self):
        input("You have leveled up. (Press Enter)")
        print("Spd")
        print("Hth")
        print("Str")
        val = input("Type the 3 letter stat you would like to increase: ")
        while True:
            if val == "Spd" or val == "spd":
                self.increaseSpeed(1)
                break
            if val == "Hth" or val == "hth":
                self.increaseHealth(1)
                break
            if val == "Str" or val == "str":
                self.increaseStrength(1)
                break
            else:
                print("Try again.")
                val = input("Type the 3 letter stat you would like to increase: ")
        self.increaseLevel(1)
        self.printStatSheet()
        return

    def IncreaseXP(self, Amount):
        self.currentXp = self.currentXp + Amount
        if (self.currentXp >= self.XpToLevel):
            self.currentXp = 0
            self.LevelUp()
            self.XpToLevel = self.XpToLevel + 2
        return