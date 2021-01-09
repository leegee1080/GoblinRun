import random
from src.GoblinClass import Goblin

class Fight:
    def __init__(self, currentplayer, difficultylevel):
        self.numberofGobs = random.randint(1,(currentplayer.level + difficultylevel))
        self.difficultylevel = difficultylevel
        self.currentplayer = currentplayer
        return

    def setupFight(self): 
        print("There is movement up ahead! Goblins!\nThere are {} goblin{}.".format(self.numberofGobs, "s" if self.numberofGobs != 1 else ""))
        self.counter = 0
        self.gobList = []
        self.gobString = ""
        while (self.counter < self.numberofGobs):
            self.gobList.append(Goblin(random.randint(1,(self.currentplayer.level + self.difficultylevel))))
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
        self.gobString += "(Press Enter)"
        input(self.gobString)
        print("\n")
        return

    def checkPlayerdead(self):
        if(self.currentplayer.health <= 0):
            return True
        else:
            return False
    
    def checkEnemiesdead(self):
        self.deadgobcount = 0
        for gob in self.gobList:
            if (gob.health > 0):
                break
            else:
                self.deadgobcount += 1

        if (self.deadgobcount == len(self.gobList)):
            return True
        else:
            return False
    
    def runFight(self):
        print("debug: start fight")
        while(True):
            print("~~~Your Attack!~~~")

            self.counter = 0
            self.gobString = ""
            while (self.counter < self.numberofGobs):
                self.gobString = self.gobString + "{}: The level {} {} one.".format(self.counter + 1, self.gobList[self.counter].level, self.gobList[self.counter].type.name)
                self.gobString += "\n"
                self.counter += 1
            print(self.gobString)
            self.playerPickingTarget = True
            while(self.playerPickingTarget):
                try:
                    self.playertargetInt = int(input("Which Goblin do you target? (1 to {})".format(len(self.gobList)))) -1
                    pass
                except ValueError:
                    print("Invalid Target! (Needs to be a number)")
                    continue

                try:
                    self.test = self.gobList[self.playertargetInt]
                    break
                except IndexError:
                    print("Invalid Target!")
                    continue
            
            print("You attack the level {} {} one.\n".format(self.gobList[self.playertargetInt].level, self.gobList[self.playertargetInt].type.name))
            self.gobList[self.playertargetInt].takedamage(self.currentplayer.strength)

            print("You do {} damage! The goblin has {} health left.".format(self.currentplayer.strength, self.gobList[self.playertargetInt].health))


            if(self.gobList[self.playertargetInt].health <= 0):
                print("You killed it!\n")

            if(self.checkPlayerdead()):
                print("You are dead!")
                break

            if(self.checkEnemiesdead()):
                self.playerExpEarned = 0
                for gob in self.gobList:
                    self.playerExpEarned += gob.level
                print("You killed them all!\nYou gained {} experience points!\n".format(self.playerExpEarned))
                self.currentplayer.IncreaseXP(self.playerExpEarned)
                break
            pass     
        return