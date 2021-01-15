class Player:

    def __init__(self, level, speed, startingHealth, strength, currentXp, XpToLevel, startingMoney, equipWeapon, equipArmor, itemList):
        self.level = level
        self.speed = speed
        self.health = startingHealth
        self.maxHealth = startingHealth
        self.strength = strength
        self.currentXp = currentXp
        self.XpToLevel = XpToLevel
        self.money = startingMoney
        self.mainWeapon = equipWeapon
        self.mainArmor = equipArmor
        self.itemList = itemList
    
    def printStatSheet(self):
        print("--------------Player Stats-------------")
        print("----------Level: " + str(self.level))
        print("----------Speed: " + str(self.speed))
        print("---------Health: {}/{}".format(self.health, self.maxHealth))
        print("-------Strength: " + str(self.strength))
        print("-----Wielding a {}.".format(self.mainWeapon.name))
        print("------Wearing a {}.".format(self.mainArmor.name))
        print("{} out of {} experience till next level.".format(self.currentXp, self.XpToLevel))
        print("---------------------------------------\n")
        return
    
    def printItemList(self):
        print("-----Wielding a {}.".format(self.mainWeapon.name))
        print("------Wearing a {}.".format(self.mainArmor.name))
        print("----In your Bag:")
        for i in self.itemList:
            print("A {}.".format(i.name))
        print("")
    
    def increaseStrength(self, Amount):
        self.strength = self.strength + Amount
        print("----------Strength went up!------------")
        return
    
    def increaseSpeed(self, Amount):
        self.speed = self.speed + Amount
        print("----------Speed went up!---------------")
        return

    def increaseHealth(self, Amount):
        self.maxHealth = self.maxHealth + Amount
        print("----------Max Health went up!----------")
        return

    def increaseLevel(self, Amount):
        self.level = self.level + Amount
        print("----------Level went up!---------------")
        return
    
    def HealPlayer(self, Amount):
        healthDif = self.maxHealth - self.health
        if Amount <= healthDif:
            self.health = self.health + Amount
            # print("Healed: " + str(Amount) + "\n")
        else:
            self.health = self.maxHealth
            print("Full Health!\n")
        return
    
    def DamagePlayer(self, Amount):
        self.health = self.health - Amount
        #if self.health <= 0:
            #print("DEBUG: player dead")
        return
    
    def PayPlayer(self, Amount):
        self.money = self.money + Amount
        print("--------You got {} gold coins!---------".format(Amount))
        return

    def LevelUp(self):
        input("----------You have leveled up!---------- (Press Enter)")
        print("-----> Type 'Spd' For Speed")
        print("-----> Type 'Hth' For Max Health")
        print("-----> Type 'Str' For Strength")
        val = input("Type the 3 letter stat you would like to increase: ")
        print("---------------------------------------")
        while True:
            if val == "Spd" or val == "spd":
                self.increaseSpeed(5)
                break
            if val == "Hth" or val == "hth":
                self.increaseHealth(10)
                break
            if val == "Str" or val == "str":
                self.increaseStrength(5)
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