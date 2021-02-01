import random
from src.FightClass import Fight
from src.WeaponsClass import Weapon
from src.ArmorClass import Armor
from src.ConsumablesClass import Consumable

class Room:
    def genRandomItem(self, playlvl, difflvl):
        newItemList = [Weapon(playlvl,difflvl), Armor(playlvl,difflvl), Consumable(playlvl,difflvl)]
        chosenItem = newItemList[random.randint(0,(len(newItemList)-1))]
        return chosenItem

    def rest(self, currentplayer, difficultylevel, extra):
        self.freehealamount = random.randint(1, currentplayer.maxHealth) / difficultylevel
        input("You find a nice place to rest (Press Enter)")
        input("You are healed {:.0f} health points! (Press Enter) \n".format(self.freehealamount))
        currentplayer.HealPlayer(self.freehealamount)
        while(True):
            playeranswer = input("Would you like to spend some money and heal more? \n (Type 'y' for yes or 'n' for no, 'stat' for your current stats, or 'bag' for your current items.)")
            if(playeranswer == "bag" or playeranswer == "Bag" or playeranswer == "BAG"):
                currentplayer.printItemList()
                continue
            if(playeranswer == "stat" or playeranswer == "Stat" or playeranswer == "STAT"):
                currentplayer.printStatSheet()
                continue
            if(playeranswer == "y" or playeranswer == "Y"):
                while(True):
                    playeranswer = input("How much would you like to heal? \n (Type a number or '0' to leave.)")
                    if playeranswer == "0":
                        break
                    try:
                        playeranswer = int(playeranswer)
                        pass
                    except ValueError:
                        print("Invalid Command! (Needs to be a number.)")
                        continue
                    if currentplayer.maxHealth >= playeranswer - currentplayer.health and playeranswer <= currentplayer.money:
                        currentplayer.HealPlayer(playeranswer)
                        currentplayer.money -= playeranswer
                    else:
                        print("You cannot heal more than your max health.")
            else:
                print("You decide to move on.\n")
                break
        return

    def lootroom(self, currentplayer, difficultylevel, lootRolls):
        self.moneygained = 0
        if(lootRolls == None or lootRolls == 0):
            self.lootRollsCounter = int(currentplayer.level / difficultylevel)
            print("\n\n------------------You find a treasure room.---------------")
        else:
            self.lootRollsCounter = lootRolls
        self.itemlist = []
        while self.lootRollsCounter > 0:
            self.moneygained += random.randint(0, (currentplayer.level/difficultylevel))
            if(random.randint(0,3) == 1):
                self.itemlist.append(self.genRandomItem(currentplayer.level, difficultylevel))
            self.lootRollsCounter -= 1
        print("You find {} gold coin{}.\n".format(self.moneygained, "s" if self.moneygained != 1 else ""))
        currentplayer.money += self.moneygained
        if(len(self.itemlist) >0):
            print("You also find {} item{}.".format(len(self.itemlist),  "s" if len(self.itemlist) != 1 else ""))
            #print itemlist
            self.itemcounter = 1
            for item in self.itemlist:
                print("{}-> {}".format(self.itemcounter, item.name))
                self.itemcounter += 1
            print("\n")
            while(True):
                self.playerinputstring = input("Which item would you like to take? (type a number from '1' to '{}') (Type 'bag' to see your stats or 'q' to leave)".format(len(self.itemlist)))
                if(self.playerinputstring == "q" or self.playerinputstring == "Q" or self.playerinputstring == "quit" or self.playerinputstring == "Quit" or self.playerinputstring == "QUIT"):
                    print("You continue on.\n")
                    break
                if(self.playerinputstring == "bag" or self.playerinputstring == "Bag" or self.playerinputstring == "BAG"):
                    self.currentplayer.printItemList()
                    continue
                try:
                    self.playertargetInt = int(self.playerinputstring) -1
                    pass
                except ValueError:
                    print("Invalid Command! (Needs to be a number or 'bag')")
                    continue
                try:
                    self.chosenitem = self.itemlist[self.playertargetInt]
                    if(self.chosenitem.cat == "w"):
                        self.tempWep = self.currentplayer.mainWeapon
                        self.currentplayer.EquipWeapon(self.chosenitem)
                        self.itemlist[self.playertargetInt] = self.tempWep
                        print("You equip up the {}{}.".format(self.chosenitem.name,"" if self.tempWep == None else (" and drop the " + self.tempWep.name)))
                    if(self.chosenitem.cat == "a"):
                        self.tempArm = self.currentplayer.mainArmor
                        self.currentplayer.DonArmor(self.chosenitem)
                        self.itemlist[self.playertargetInt] = self.tempArm
                        print("You don the {}{}.".format(self.chosenitem.name,"" if self.tempArm == None else (" and doff the " + self.tempArm.name)))
                    if(self.chosenitem.cat == "c"):
                        self.currentplayer.PickUpConsumable(self.chosenitem)
                        print("You place the {} in your bag.".format(self.chosenitem.name))
                        self.itemlist[self.playertargetInt] = None
                except IndexError:
                    print("Invalid Item!")
                    continue

                #check itemlist
                self.TempItemList = []
                for item in self.itemlist:
                    if(item != None):
                        self.TempItemList.append(item)
                self.itemlist = self.TempItemList
                #break if list is empty
                if(len(self.itemlist) <= 0):
                    print("There are no more items here.\n")
                    break
                #reprint itemlist
                self.itemcounter = 1
                print("\nStill {} item{} here.".format(len(self.itemlist),  "s" if len(self.itemlist) != 1 else ""))
                for item in self.itemlist:
                    print("{}-> {}".format(self.itemcounter, item.name))
                    self.itemcounter += 1
                print("\n")
        print("\n")
        return

    def shop(self,currentplayer, difficultylevel, extra):
        print("shop")
        return

    def fight(self, currentplayer, difficultylevel, extra):
        self.newFight = Fight(currentplayer, difficultylevel)
        self.newFight.setupFight()
        self.victoryValue = self.newFight.runFight()
        if self.victoryValue > 0:
            self.lootroom(currentplayer, difficultylevel, self.victoryValue)
        return

    def determineroomtype(self, currentplayer, difficultylevel):
        switch = [
            self.fight,
            self.fight,
            self.fight,
            self.fight,
            self.fight,
            self.fight,
            self.fight,
            self.rest,
            self.rest,
            self.rest,
            self.lootroom
            #self.shop
        ]
        self.randint = random.randint(0,len(switch)-1)
        self.func = switch[self.randint]
        #(self.randint, lambda: "Invalid Room Type!")
        self.func(currentplayer, difficultylevel, None)
        return


    def __init__(self, playerlevel, difficultylevel, currentplayer):
        self.playerlevel = playerlevel
        self.difficultylevel = difficultylevel
        self.currentplayer = currentplayer
        self.determineroomtype(currentplayer, difficultylevel)
        return
    
