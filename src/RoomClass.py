import random
from src.FightClass import Fight

class Room:
    def fight(self, currentplayer, difficultylevel):
        # print("fight")
        # self.currentplayer.IncreaseXP(10)
        self.newFight = Fight(currentplayer, difficultylevel)
        self.newFight.setupFight()
        self.newFight.runFight()
        #earn treasure/gold
        return
    
    def rest(self, currentplayer, difficultylevel):
        #maybe spend gold for more health
        self.freehealamount = random.randint(2,100) / difficultylevel
        input("You find a nice place to rest (Press Enter)")
        input("You are healed {:.0f} health points! (Press Enter)".format(self.freehealamount))
        self.currentplayer.HealPlayer(self.freehealamount)
        return

    def loot(self,currentplayer, difficultylevel):
        print("loot")
        return

    #disabled loot room type for now. just change the 5 to a 6 in the randint to turn it back on
    def determineroomtype(self, currentplayer, difficultylevel):
        self.randint = random.randint(0,5)
        switch = {
            0: self.fight,
            1: self.fight,
            2: self.fight,
            3: self.fight,
            4: self.fight,
            5: self.rest,
            6: self.loot
        }
        self.func = switch.get(self.randint, lambda: "Invalid Room Type!")
        self.func(currentplayer, difficultylevel)
        return


    def __init__(self, playerlevel, difficultylevel, currentplayer):
        self.playerlevel = playerlevel
        self.difficultylevel = difficultylevel
        self.currentplayer = currentplayer
        self.determineroomtype(currentplayer, difficultylevel)
        return
    
