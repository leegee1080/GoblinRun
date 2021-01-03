class Player:
    StatSheetForPrint = []

    def __init__(self, level, speed, startingHealth, strength):
        self.level = level
        self.speed = speed
        self.health = startingHealth
        self.maxHealth = startingHealth
        self.strength = strength
    
    def printStatSheet(self):
        self.StatSheetForPrint.clear
        self.StatSheetForPrint.append("Level: " + str(self.level))
        self.StatSheetForPrint.append("Speed: " + str(self.speed))
        self.StatSheetForPrint.append("Max Health: " + str(self.maxHealth))
        self.StatSheetForPrint.append("Current Health: " + str(self.health))
        self.StatSheetForPrint.append("Strength: " + str(self.strength))
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