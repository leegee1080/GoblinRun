import random

class Room:
    def fight(self):
        print("fight")
        return
    
    def rest(self):
        print("rest")
        return

    def loot(self):
        print("loot")
        return
    
    def determineroomtype(self, argument):
        switch = {
            0: self.fight,
            1: self.rest,
            2: self.loot
        }
        self.func = switch.get(argument, lambda: "Invalid Room Type!")
        self.func()
        return


    def __init__(self, playerlevel, difficultylevel):
        self.playerlevel = playerlevel
        self.difficultylevel = difficultylevel
        self.randint = random.randint(0,2)
        self.determineroomtype(self.randint)
        return
    
