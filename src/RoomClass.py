import random
from src.FightClass import Fight

class Room:
    def fight(self, currentplayer, difficultylevel):
        # print("fight")
        # self.currentplayer.IncreaseXP(10)
        self.newFight = Fight(currentplayer, difficultylevel)
        self.newFight.setupFight()
        self.newFight.runFight()
        return
    
    def rest(self, currentplayer, difficultylevel):
        # print("rest")
        self.freehealamount = random.randint(2,100) / difficultylevel
        input("You find a nice place to rest (Press Enter)")
        input("You are healed {:.0f} health points! (Press Enter)".format(self.freehealamount))
        self.currentplayer.HealPlayer(self.freehealamount)
        return

    def loot(self,currentplayer, difficultylevel):
        print("loot")
        return
    
    def determineroomtype(self, randNum, currentplayer, difficultylevel):
        switch = {
            0: self.fight,
            1: self.rest,
            2: self.loot
        }
        self.func = switch.get(randNum, lambda: "Invalid Room Type!")
        self.func(currentplayer, difficultylevel)
        return


    #disabled loot room type for now. just change the 1 to a 2 in the randint to turn it back on
    def __init__(self, playerlevel, difficultylevel, currentplayer):
        self.playerlevel = playerlevel
        self.difficultylevel = difficultylevel
        self.currentplayer = currentplayer
        self.randint = random.randint(0,1)
        self.determineroomtype(self.randint, currentplayer, difficultylevel)
        return
    
