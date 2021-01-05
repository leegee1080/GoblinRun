from src.GameManager import GlobalVarStorage
from src.GoblinClass import Goblin
from src.PlayerClass import Player

gameversion = 0.1


CurrentPlayer = Player(1,1,1,1,0,1)

#Game Start
print("GOBLIN RUN             ver: " + str(gameversion))

input("You enter a goblin den. (Press Enter)")
input("Time to clear them out. (Press Enter)")
input("See how far you can get. (Press Enter)")

CurrentPlayer.IncreaseXP(10)