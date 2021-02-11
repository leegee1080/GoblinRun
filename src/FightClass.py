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
    
    def noSpecial(self, gobTarget):
        print("You punch the level {} {} one with your fists.".format(gobTarget.level, gobTarget.type.name))
        if(self.currentplayer.nextHitDamageBoost > 0):
            print("Your damage is boosted by {} points".format(self.currentplayer.nextHitDamageBoost))
        print("You strike for {:.0f} potential damage!.\n".format(self.currentplayer.damage + self.currentplayer.nextHitDamageBoost))
        gobTarget.takedamage(self.currentplayer.damage + self.currentplayer.nextHitDamageBoost, None)
        return

    def Quick(self, gobTarget):
        print("You stab the level {} {} one with your {}.".format(gobTarget.level, gobTarget.type.name, self.currentplayer.mainWeapon.name))
        if(self.currentplayer.nextHitDamageBoost > 0):
            print("Your damage is boosted by {} points".format(self.currentplayer.nextHitDamageBoost))
        print("You combo for {:.0f} potential damage each hit!.\n".format(self.currentplayer.damage + self.currentplayer.nextHitDamageBoost))
        self.counter = self.currentplayer.mainWeapon.statSpeed
        while(self.counter > 0):
            gobTarget.takedamage(self.currentplayer.damage + self.currentplayer.nextHitDamageBoost, self.currentplayer.mainWeapon.statPierce)
            self.counter -= 1
        return

    def Sweep(self, gobTarget):
        print("You sweep the level {} {} one with your {}.".format(gobTarget.level, gobTarget.type.name, self.currentplayer.mainWeapon.name))
        if(self.currentplayer.nextHitDamageBoost > 0):
            print("Your damage is boosted by {} points".format(self.currentplayer.nextHitDamageBoost))
        print("You strike it for {:.0f} potential damage!.\n".format(self.currentplayer.damage))
        gobTarget.takedamage(self.currentplayer.damage + self.currentplayer.nextHitDamageBoost, self.currentplayer.mainWeapon.statPierce)
        self.SweepTargetList = []
        for gob in self.gobList:
            if(gob.level < gobTarget.level and gob.alive == True):
                print("A {} goblin is caught in the sweep for {:.0f} potential damage!.\n".format(gob.type.name, self.currentplayer.damage + self.currentplayer.nextHitDamageBoost))
                gob.takedamage(self.currentplayer.damage + self.currentplayer.nextHitDamageBoost, self.currentplayer.mainWeapon.statPierce)
        return

    def Heavy(self, gobTarget):
        print("You smash the level {} {} one with your {}.".format(gobTarget.level, gobTarget.type.name, self.currentplayer.mainWeapon.name))
        if(self.currentplayer.nextHitDamageBoost > 0):
            print("Your damage is boosted by {} points".format(self.currentplayer.nextHitDamageBoost))
        print("You strike it for {:.0f} potential damage!.\n".format(self.currentplayer.damage))
        gobTarget.takedamage(self.currentplayer.damage + self.currentplayer.nextHitDamageBoost, self.currentplayer.mainWeapon.statPierce)
        self.SweepTargetList = []
        for gob in self.gobList:
            if(gob.level > gobTarget.level and gob.alive == True):
                print("A {} goblin is caught in the shockwave for {:.0f} potential damage!.\n".format(gob.type.name, self.currentplayer.damage + self.currentplayer.nextHitDamageBoost))
                gob.takedamage(self.currentplayer.damage + self.currentplayer.nextHitDamageBoost, self.currentplayer.mainWeapon.statPierce)
        return

    def Long(self, gobTarget):
        print("You spear the level {} {} one with your {}.".format(gobTarget.level, gobTarget.type.name, self.currentplayer.mainWeapon.name))
        if(self.currentplayer.nextHitDamageBoost > 0):
            print("Your damage is boosted by {} points".format(self.currentplayer.nextHitDamageBoost))
        print("You hit it for {:.0f} potential damage and it is pushed back!.\n".format(self.currentplayer.damage + self.currentplayer.nextHitDamageBoost))
        gobTarget.stun(self.currentplayer.mainWeapon.statPierce)
        gobTarget.takedamage(self.currentplayer.damage + self.currentplayer.nextHitDamageBoost, self.currentplayer.mainWeapon.statPierce)
        return


    def CalculateWeaponSpecial(self, newgobTarget):
        if(self.currentplayer.mainWeapon == None):
            self.noSpecial(newgobTarget)
            return
        wepSwitch = {
            "quick": self.Quick,
            "sweep": self.Sweep,
            "heavy": self.Heavy,
            "long": self.Long
        }
        self.playWepSpecial = self.currentplayer.mainWeapon.statSpecial
        self.wepFunc = wepSwitch.get(self.playWepSpecial)
        if(self.wepFunc != None):
            self.wepFunc(newgobTarget)
        else:
            print("ERROR (Line 96) Tried to use a special that does not exist.")
        return
    
    def playerTurn(self):
        print("~~~Your Turn!~~~")
        self.currentplayer.TickDownPotEffects()
        self.counter = 0
        self.gobString = ""
        while (self.counter < self.numberofGobs):
            self.gobString = self.gobString + "{}--> The level {} {} one. {}".format(self.counter + 1, self.gobList[self.counter].level, self.gobList[self.counter].type.name, "(Dead)" if self.gobList[self.counter].health <= 0 else "")
            self.gobString += "\n"
            self.counter += 1
        print(self.gobString)
        while(True):
            self.playerinputstring = input("Which Goblin do you target? (1 to {}) (Type 'stat' to see your stats or 'bag' for your current items.)".format(len(self.gobList)))
            if(self.playerinputstring == "stat" or self.playerinputstring == "Stat" or self.playerinputstring == "STAT"):
                self.currentplayer.printStatSheet()
                continue
            if(self.playerinputstring == "bag" or self.playerinputstring == "Bag" or self.playerinputstring == "BAG"):
                self.currentplayer.printItemList()
                if(len(self.currentplayer.itemList) > 0):
                    playeranswer = input("\nWould you like to use an item?")
                    if(playeranswer == "y" or playeranswer == "Y"):
                        self.currentplayer.UsePot()
                    continue
                continue
            try:
                self.playertargetInt = int(self.playerinputstring) -1
                pass
            except ValueError:
                print("Invalid Command! (Needs to be a number or 'stat')")
                continue
            try:
                self.test = self.gobList[self.playertargetInt]
                pass
            except IndexError:
                print("Invalid Target!")
                continue
            if(self.gobList[self.playertargetInt].health > 0):
                break
            else:
                print("Target is already dead.")
                continue
        self.CalculateWeaponSpecial(self.gobList[self.playertargetInt])
        return

    def gobTurn(self, gobParam):
        gobParam.attack(self.currentplayer)
        return

    def runFight(self):
        self.turnCounter = self.TurnCounterMax
        self.isplayerturn = False
        while(True):
            print("\nTurn number {:.0f} out of {:.0f}".format(self.turnCounter, self.TurnCounterMax))
            print("-----------------------------------------------------------------------------\n")

            #check for turn counter
            if(self.turnCounter <= self.currentplayer.speed):
                self.playerTurn()
                pass
            for gob in self.gobList:
                if(self.turnCounter <= gob.speed):
                    self.gobTurn(gob)
                if(self.checkPlayerdead()):
                    print("\nThe level {} {} one strikes you with a final blow.".format(gob.level, gob.type.name))
                    return 0

           #check for deaths
            if(self.checkEnemiesdead()):
                self.playerExpEarned = 0
                for gob in self.gobList:
                    self.playerExpEarned += gob.level
                print("You killed them all!\nYou gained {} experience points!\n".format(self.playerExpEarned))
                self.currentplayer.IncreaseXP(self.playerExpEarned)
                return len(self.gobList)
            self.turnCounter -= 1   
            if(self.turnCounter < self.TurnCounterMin):
                self.turnCounter = self.TurnCounterMax
        return