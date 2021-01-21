import random
from src.FightClass import Fight
from src.Items import NewItem

class Room:
    def rest(self, currentplayer, difficultylevel):
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
                    if playeranswer <= currentplayer.maxHealth - currentplayer.health:
                        currentplayer.HealPlayer(playeranswer)
                        currentplayer.money -= playeranswer;
                    else:
                        print("You cannot heal more than your max health.")
            else:
                break
        return

    def loot(self, currentplayer, difficultylevel, lootRolls):
        if(lootRolls == None):
            lootRolls = 1
        self.moneygained = 0;
        self.lootRollsCounter = lootRolls
        self.itemlist = []
        while self.lootRollsCounter > 0:
            self.moneygained += random.randint(0, (currentplayer.level/difficultylevel))
            if(random.randint(0,2) == 1):
                self.itemlist.append(NewItem(1,difficultylevel,"none"))
            self.lootRollsCounter -= 1
        print("You find {} gold coin{}.\n".format(self.moneygained, "s" if len(self.itemlist) != 1 else ""))
        currentplayer.money += self.moneygained
        if(len(self.itemlist) >0):
            print("You also find {} item{}.".format(len(self.itemlist),  "s" if len(self.itemlist) != 1 else ""))
            for item in self.itemlist:
                print(item.name)
        print("\n")
        return

    def shop(self,currentplayer, difficultylevel):
        print("shop")
        return

    def fight(self, currentplayer, difficultylevel):
        self.newFight = Fight(currentplayer, difficultylevel)
        self.newFight.setupFight()
        self.victoryValue = self.newFight.runFight()
        if self.victoryValue > 0:
            self.loot(currentplayer, difficultylevel, self.victoryValue)
        return

    def determineroomtype(self, currentplayer, difficultylevel):
        switch = [
            self.fight,
            self.fight,
            self.fight,
            self.fight,
            self.fight,
            self.rest,
            self.rest,
            self.rest,
            self.loot,
            self.shop
        ]
        self.randint = random.randint(0,len(switch)-1)
        self.func = switch[self.randint]
        #(self.randint, lambda: "Invalid Room Type!")
        self.func(currentplayer, difficultylevel)
        return


    def __init__(self, playerlevel, difficultylevel, currentplayer):
        self.playerlevel = playerlevel
        self.difficultylevel = difficultylevel
        self.currentplayer = currentplayer
        self.determineroomtype(currentplayer, difficultylevel)
        return
    
