import random
from src.FightClass import Fight

class Room:
    def rest(self, currentplayer, difficultylevel):
        #maybe spend gold for more health
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

    def loot(self,currentplayer, difficultylevel, lootRolls):
        print("loot")
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
    
