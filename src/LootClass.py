import random
from src.Items import GlobalItemVars

class Loot:
    def __init__(self, currentplayer, difficultylevel):
        self.difflevel = difficultylevel
        self.currentplayer = currentplayer
        return

    def randomGenItem(self, playerlevel, difficultylevel):
        self.newItem = None
        self.chosenmod = None
        #diff = diff * 10
        #ranlower = playerlevel/difficultylevel
        #ranupper = playerlevel/difficultylevel + ranlower
        #self.chosenmod = allmods(ranint(ranlower, ranupper)) both rounded up
        return self.newItem