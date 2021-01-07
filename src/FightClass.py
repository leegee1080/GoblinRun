import random

class Fight:
    def __init__(self, currentplayer, difficultylevel):
        self.numberofGobs = random.randint(1,3) * difficultylevel * currentplayer.level
        print(str(self.numberofGobs))
        return

    def setupFight(self):
        print("There is movement up ahead! Goblins!")
        return
    
    def runFight(self):
        
        return


    pass