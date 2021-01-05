from src.GameManager import GlobalVarStorage
from src.GoblinClass import Goblin
from src.PlayerClass import Player
from src.RoomClass import Room
from src.FightClass import Fight

gameversion = 0.1


CurrentPlayer = Player(1,1,1,1,0,1)

#Game Start
print("GOBLIN RUN             ver: " + str(gameversion))

# input("You enter a goblin den. (Press Enter)")
# input("Time to clear them out. (Press Enter)")
# input("See how far you can get. (Press Enter)")

# CurrentPlayer.IncreaseXP(10)

newroom = Room(CurrentPlayer.level,1)