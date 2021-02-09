import random

class Player:
    def __init__(self, level, agl, startingHealth, strength, currentXp, XpToLevel, startingMoney, equipWeapon, equipArmor, itemList, gobRep):
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
        self.goblinRep = gobRep
        self.PotEffects = {
            "healing" : [0, self.ApplyHealing],
            "damage boost" : [0, self.ApplyDamageBoost],
            "magic immune" : [0, self.ApplyMagImmune]
        }
        self.nextHitDamageBoost = 0
        self.isMagImmune = False
        self.gobStatusEffect = None
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
        print("------A purse with {} gold coin{}.".format("a" if int(self.money) == 1 else int(self.money), "s" if int(self.money) != 1 else ""))
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
        if(self.mainArmor != None and self.mainWeapon == None):
            self.speed = self.mainArmor.statSpecial[1] * self.agl
        if(self.mainArmor != None and self.mainWeapon != None):
            self.speed = (self.mainWeapon.statSpeed + self.agl) * self.mainArmor.statSpecial[1]
        if(self.mainArmor == None and self.mainWeapon != None):
            self.speed = self.mainWeapon.statSpeed + self.agl
        if(self.mainArmor == None and self.mainWeapon == None):
            self.speed = self.agl
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
            print("Healed " + str(int(Amount)) + " health.")
        else:
            self.health = self.maxHealth
            print("Full Health!\n")
        return
    
    def DamagePlayer(self, Amount):
        if(self.mainArmor != None):
            if(random.randint(1, 100) >= self.mainArmor.statWeaponProtectChance):
                self.tempDam = (Amount*self.mainArmor.statProtection)
                print("!!!!!!!!!!!!!!!!!The goblin hits your armor but still does {} damage!!!!!!!!!!!!!!!!!".format(int(self.tempDam)))
                self.health = self.health - int(self.tempDam)
                print("You have {} heath left.".format(int(self.health)))
                return
            else:
                print("!!!!!!!!!!!!!!!!!You dodge the goblin's attack!!!!!!!!!!!!!!!!!")
                return
        else:
            print("!!!!!!!!!!!!!!!!!The goblin hits you for full damage!!!!!!!!!!!!!!!!!")
            self.health -= int(Amount)
            print("You have {} heath left.".format(int(self.health)))
        return

    def DonArmor(self, item):
        self.mainArmor = item
        if(self.mainArmor != None):
            if(self.mainArmor.statSpecial[0] != "loose"):
                self.isMagImmune = False
            else:
                
                self.isMagImmune = True
            self.speed = self.mainArmor.statSpecial[1] * self.agl
            return
        else:
            self.speed = self.agl
            self.isMagImmune = False
        return
    
    def DoffArmor(self):
        if(self.mainArmor != None):
            print("You remove your {}.".format(self.mainArmor.name))
            self.mainArmor = None
            self.DonArmor(None)
        return

    def EquipWeapon(self, item):
        if(item != None):
            self.mainWeapon = item
            self.damage = item.statDamage + self.strength
        return
    
    def DiscardWeapon(self):
        if(self.mainWeapon != None):
            self.mainWeapon = None
            self.damage = self.strength
        return

    def PickUpConsumable(self, item):
        self.templist = self.itemList
        self.templist.append(item)
        self.itemList = self.templist
        self.templist = None
        return

    def DropItem(self, newItemList):
        self.itemList = newItemList
        return
    
    def SmitePlayer(self, spellType):
        if(self.isMagImmune):
            print("You are immune to spells.")
            return
        else:
            if(spellType[0] == "slow"):
                self.gobStatusEffect = spellType
                if(self.mainArmor != None):
                    if(random.randint(1, 100) >= self.mainArmor.statMagicProtectChance):
                        self.speed = (self.mainArmor.statSpecial[1] * self.agl) * spellType[1]
                        print("You are slowed!!")
                        return
                    else:
                        print("Your armor absorbs the spell! No effect to you!")
                        return
                else:
                    self.speed = self.agl * spellType[1]
                    print("You are slowed!!")
        return

    def PayPlayer(self, Amount):
        self.money = self.money + Amount
        print("--------You got {} gold coins.---------".format(int(Amount)))
        return

    def ChargePlayer(self, Amount):
        self.money -= Amount
        print("-------You lose {} gold coins.---------".format(int(Amount)))

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

        #update armor and wep stats
        if(self.mainWeapon != None):
            self.damage = self.mainWeapon.statDamage + self.strength
        else:
            self.damage = self.strength

        if(self.mainArmor != None):
            if(self.mainArmor.statSpecial[0] != "loose"):
                self.speed = self.mainArmor.statSpecial[1] * self.agl
                self.isMagImmune = False
            else:
                self.speed = self.agl
                self.isMagImmune = True
        else:
            self.speed = self.agl
            self.isMagImmune = False

        #print the stat sheet
        self.printStatSheet()
        return

    def IncreaseXP(self, Amount):
        self.currentXp = self.currentXp + Amount
        if (self.currentXp >= self.XpToLevel):
            self.currentXp = 0
            self.LevelUp()
            self.XpToLevel = self.XpToLevel + 2
        return

    def UsePot(self):
        if(len(self.itemList) <= 0):
            print("Your bag is empty.\n")
            return
        itemcounter = 1
        for item in self.itemList:
            print("{}-> Your {} can be used.".format(itemcounter, item.name))
            itemcounter += 1
        while(True):
            if(len(self.itemList) <= 0):
                print("Your bag is empty.\n")
                break
            playerinputstring = input("Which item would you like to use? (type a number from '1' to '{}') (Type 'q' to go back.)".format(len(self.itemList)))
            if(playerinputstring == "q" or playerinputstring == "Q" or playerinputstring == "quit" or playerinputstring == "Quit" or playerinputstring == "QUIT"):
                break
            try:
                playertargetInt = int(playerinputstring)  -1
                pass
            except ValueError:
                print("Invalid Command!")
                continue
            try:
                chosenitem = self.itemList[playertargetInt]
                if(chosenitem.cat == "c"):
                    self.ApplyPotEffect(chosenitem)
                    self.itemList[playertargetInt] = None
                    TempList = []
                    for item in self.itemList:
                        if(item != None):
                            TempList.append(item)
                    self.itemList = TempList
                    break
                else:
                    print("You can't drink that.")
            except IndexError:
                print("Invalid Item!")
                continue
        return

    def ApplyPotEffect(self, pot):
        print("You drink the {}.\n".format(pot.name))
        SelectedStat = self.PotEffects.get(pot.effect, None)
        if(SelectedStat != None):
            SelectedStat[0] += pot.statFactor
            SelectedStat[1]()
        else:
            print("ERROR line(237): effect not found")
        return
    
    def TickDownPotEffects(self):
        for item in self.PotEffects:
            if(item == "0"):
                continue
            if(self.PotEffects[item][0] > 0):
                self.PotEffects[item][0] -= 1
                self.PotEffects[item][1]()
                if(self.PotEffects[item][0] == 0):
                    print("The {} effect has worn off.".format(item))
        return

    def ApplyMagImmune(self):
        if(self.PotEffects["magic immune"][0] > 0):
            self.isMagImmune = True
            return
        if(self.mainArmor == None):
            self.isMagImmune = False
            return
        if(self.mainArmor.statSpecial[0] == "loose"):
            self.isMagImmune = True
        return
    
    def ApplyDamageBoost(self):
        self.nextHitDamageBoost = self.PotEffects["damage boost"][0]
        return

    def ApplyHealing(self):
        self.HealPlayer(self.PotEffects["healing"][0])
        return

    def dropItem(self):
        personalItemList = []
        if(self.mainWeapon != None):
            personalItemList.append(self.mainWeapon)
        if(self.mainArmor != None):
            personalItemList.append(self.mainArmor)
        for item in self.itemList:
            personalItemList.append(item)
        if(len(personalItemList) <= 0):
            print("--------Your bag is empty--------\n")
            return
        itemcounter = 1
        for item in personalItemList:
            print("{}-> Your {} can be dropped".format(itemcounter, item.name))
            itemcounter += 1
        while(True):
            playerinputstring = input("Which item would you like to drop? (type a number from '1' to '{}') (Type 'q' to go back.)".format(len(personalItemList)))
            if(playerinputstring == "q" or playerinputstring == "Q" or playerinputstring == "quit" or playerinputstring == "Quit" or playerinputstring == "QUIT"):
                break
            try:
                playertargetInt = int(playerinputstring) -1
                pass
            except ValueError:
                print("Invalid Command!")
                continue
            try:
                chosenitem = personalItemList[playertargetInt]
                if(chosenitem.cat == "w"):
                    self.DiscardWeapon()
                    print("You drop your {}.".format(chosenitem.name))
                if(chosenitem.cat == "a"):
                    self.DoffArmor()
                    print("You drop your {}.".format(chosenitem.name))
                if(chosenitem.cat == "c"):
                    print("You drop the {} from your bag.".format(chosenitem.name))
                    personalItemList[playertargetInt] = None
                    TempList = []
                    for item in personalItemList:
                        if(item != None and item.cat == "c"):
                            TempList.append(item)
                    self.DropItem(TempList)
            except IndexError:
                print("Invalid Item!")
                continue
            return