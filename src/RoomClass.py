import random

class Room:
    def fight(self,currentplayer):
        print("fight")
        self.currentplayer.IncreaseXP(10)
        return
    
    def rest(self, currentplayer):
        print("rest")
        input("You find a nice place to rest (Press Enter)")
        input("You are healed to full! (Press Enter)")
        self.currentplayer.HealPlayer(1000000000000)
        return

    def loot(self,currentplayer):
        print("loot")
        return
    
    def determineroomtype(self, argument, currentplayer):
        switch = {
            0: self.fight,
            1: self.rest,
            2: self.loot
        }
        self.func = switch.get(argument, lambda: "Invalid Room Type!")
        self.func(currentplayer)
        return


    #disabled loot room type for now. just change the 1 to a 2 in the randint to turn it back on
    def __init__(self, playerlevel, difficultylevel, currentplayer):
        self.playerlevel = playerlevel
        self.difficultylevel = difficultylevel
        self.currentplayer = currentplayer
        self.randint = random.randint(0,1)
        self.determineroomtype(self.randint, currentplayer)
        return
    
