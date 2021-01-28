class Player:

    def __init__(self, level, agl, startingHealth, strength, currentXp, XpToLevel, startingMoney, equipWeapon, equipArmor, itemList):
        self.level = level
        self.agl = agl
        self.health = startingHealth
        self.maxHealth = startingHealth
        self.strength = strength
        self.currentXp = currentXp
        self.XpToLevel = XpToLevel
        self.money = startingMoney
        self.mainWeapon = equipWeapon
        self.mainArmor = equipArmor
        self.itemList = itemList
        self.speed = agl
        self.damage = strength
        self.isImmune = False
        if (self.mainWeapon != None):
            self.EquipWeapon(equipWeapon)
        if (self.mainArmor != None):
            self.DonArmor(equipArmor)

    
    def printStatSheet(self):
        print("--------------Player Stats-------------")
        print("----------Level: " + str(self.level))
        print("----------Speed: " + str(int(self.speed)))
        print("---------Health: {}/{}".format(int(self.health), int(self.maxHealth)))
        print("-------Strength: " + str(self.strength))
        if (self.mainWeapon != None):
            print("-----Wielding a {}.".format(self.mainWeapon.name))
        if (self.mainArmor != None):
            print("------Wearing a {}.".format(self.mainArmor.name))
        print("{} out of {} experience till next level.".format(self.currentXp, self.XpToLevel))
        print("---------------------------------------\n")
        return
    
    def printItemList(self):
        if (self.mainWeapon != None):
            print("-----Wielding a {}.".format(self.mainWeapon.name))
        if (self.mainArmor != None):
            print("------Wearing a {}.".format(self.mainArmor.name))
        print("------A purse with {} gold coin{}.".format("a" if self.money == 1 else self.money, "s" if self.money != 1 else ""))
        print("In your Bag:")
        for i in self.itemList:
            print("A {}.".format(i.name))
        print("---------------------------------------\n")
    
    def increaseStrength(self, Amount):
        self.strength = self.strength + Amount
        print("----------Strength went up!------------")
        return
    
    def increaseAgl(self, Amount):
        self.agl = self.agl + Amount
        print("----------Agility went up!---------------")
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
        else:
            self.health = self.maxHealth
            print("Full Health!\n")
        return
    
    def DamagePlayer(self, Amount):
        if(self.mainArmor != None):
            self.health = self.health - (Amount/self.mainArmor.statProtection)
        else:
            self.health -= Amount
        return

    def DonArmor(self, item):
        self.mainArmor = item
        return

    def EquipWeapon(self, item):
        self.mainWeapon = item
        self.damage = item.statDamage + self.strength
        return

    def PickUpConsumable(self, item):
        print("!DEBUG picked up item: " + self.item.name)
        self.templist = self.itemList
        self.templist.append(item)
        self.itemList = self.templist
        self.templist = None
        return

    def PayPlayer(self, Amount):
        self.money = self.money + Amount
        print("--------You got {} gold coins!---------".format(Amount))
        return

    def LevelUp(self):
        input("----------You have leveled up!---------- (Press Enter)")
        print("-----> Type 'Agl' For Agility")
        print("-----> Type 'Hth' For Max Health")
        print("-----> Type 'Str' For Strength")
        val = input("Type the 3 letter stat you would like to increase: ")
        print("---------------------------------------")
        while True:
            if val == "Agl" or val == "agl":
                self.increaseAgl(5)
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
        if(self.mainWeapon != None):
            self.damage = self.mainWeapon.statDamage + self.strength
        else:
            self.damage = self.strength

        if(self.mainArmor != None):
            if(self.mainArmor.statSpecial(0) != "loose"):
                self.speed = self.mainArmor.statSpecial(1) * self.agl
                self.isImmune = False
            else:
                self.speed = self.agl
                self.isImmune = True
        else:
            self.speed = self.agl
            self.isImmune = False

        self.printStatSheet()
        return

    def IncreaseXP(self, Amount):
        self.currentXp = self.currentXp + Amount
        if (self.currentXp >= self.XpToLevel):
            self.currentXp = 0
            self.LevelUp()
            self.XpToLevel = self.XpToLevel + 2
        return