import random

class Loot:
    def __init__(self, currentplayer, difficultylevel):
        self.difflevel = difficultylevel
        self.currentplayer = currentplayer
        return

    def randomGenItem(self, playerlevel, difficultylevel):
        self.newItem = None

        return self.newItem