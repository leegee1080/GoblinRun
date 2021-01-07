import random
from src.GoblinClass import Goblin

class Fight:
    def __init__(self, currentplayer, difficultylevel):
        self.numberofGobs = random.randint(1,3) * difficultylevel * currentplayer.level
        self.difficultylevel = difficultylevel
        self.currentplayer = currentplayer
        return

    def setupFight(self): 
        print("There is movement up ahead! Goblins!\nThere are {} goblin{}.".format(self.numberofGobs, "s" if self.numberofGobs != 1 else ""))
        self.counter = 0
        self.gobList = []
        self.gobString = ""
        while (self.counter < self.numberofGobs):
            self.gobList.append(Goblin(random.randint(1,3) * self.difficultylevel * self.currentplayer.level))
            self.gobString = self.gobString + "{} level {} {} one".format("A" if self.counter == 0 else "a", self.gobList[self.counter].level, self.gobList[self.counter].type.name)
            self.counter += 1
            if(self.counter == (self.numberofGobs-1) and self.numberofGobs > 1):
                self.gobString = self.gobString +" and "
                continue
            elif (self.counter < self.numberofGobs):
                self.gobString = self.gobString +", "
                continue
            else:
                self.gobString = self.gobString +"."
                break
        print(self.gobString)
        return
    
    def runFight(self):
        # while(True):
        print("fight")
        return


    pass