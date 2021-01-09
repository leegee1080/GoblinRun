import random
from src.GoblinClass import Goblin

class Fight:
    def __init__(self, currentplayer, difficultylevel):
        self.numberofGobs = random.randint(1,(currentplayer.level + difficultylevel))
        self.difficultylevel = difficultylevel
        self.currentplayer = currentplayer
        return

    def findTurnCounterMaximums(self, goblistParam, currentplayerParam):
        self.TurnCounterMax = currentplayerParam.speed
        self.TurnCounterMin = currentplayerParam.speed
        for gob in goblistParam:
            if(gob.speed > self.TurnCounterMax):
                self.TurnCounterMax = gob.speed
            if(gob.speed < self.TurnCounterMin):
                self.TurnCounterMin = gob.speed
        #input("DEBUG turncountermax: {}, turncountermin: {}".format(self.TurnCounterMax, self.TurnCounterMin))
        return

    def setupFight(self): 
        print("\nThere is movement up ahead! Goblins!\nThere {} {} goblin{}.".format("are" if self.numberofGobs != 1 else "is", self.numberofGobs, "s" if self.numberofGobs != 1 else ""))
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
        self.findTurnCounterMaximums(self.gobList, self.currentplayer)
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
    
    def playerTurn(self):
        print("~~~Your Turn!~~~")
        self.counter = 0
        self.gobString = ""
        while (self.counter < self.numberofGobs):
            self.gobString = self.gobString + "{}--> The level {} {} one. {}".format(self.counter + 1, self.gobList[self.counter].level, self.gobList[self.counter].type.name, "(Dead)" if self.gobList[self.counter].health <= 0 else "")
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
        return

    def gobTurn(self, gobParam):
        if (gobParam.health <= 0):
            return
        else:
            print("\n~~~Level {} {} one attacks!~~~\n".format(gobParam.level, gobParam.type.name))
            self.currentplayer.DamagePlayer(gobParam.damage)
            return

    def runFight(self):
        self.turnCounter = self.TurnCounterMax
        self.whichgobturn = None
        self.isplayerturn = False
        while(True):
            if(self.turnCounter == self.currentplayer.speed):
                self.isplayerturn = True
                self.whichgobturn = None
            else:
                self.isplayerturn = False       
            for gob in self.gobList:
                if(self.turnCounter == gob.speed):
                    self.whichgobturn = gob
                    break
            #print("DEBUG turncounter: {}, playerspeed: {}, chosen gob speed: {}".format(self.turnCounter, self.currentplayer.speed, "None" if self.whichgobturn is None else self.whichgobturn.speed))
            if (self.isplayerturn):
                self.playerTurn()
            if((self.isplayerturn is False) and (self.whichgobturn is not None)):
                self.gobTurn(self.whichgobturn)

            if(self.checkPlayerdead()):
                print("\nThe level {} {} one strikes you with a final blow.".format(self.whichgobturn.level, self.whichgobturn.type.name))
                break

            if(self.checkEnemiesdead()):
                self.playerExpEarned = 0
                for gob in self.gobList:
                    self.playerExpEarned += gob.level
                print("You killed them all!\nYou gained {} experience points!\n".format(self.playerExpEarned))
                self.currentplayer.IncreaseXP(self.playerExpEarned)
                break
            self.turnCounter -= 1   
            if(self.turnCounter < self.TurnCounterMin):
                self.turnCounter = self.TurnCounterMax
        return