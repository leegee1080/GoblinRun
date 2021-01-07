from src.GameManager import GlobalVarStorage
from src.PlayerClass import Player
from src.RoomClass import Room
# from src.GoblinClass import Goblin
# from src.FightClass import Fight

gameversion = 0.1

#global vars
CurrentPlayer = Player(1,1,1,1,0,1)

def checkfornextroom():
    while(True):
        playeranswer = input("Would you like to continue? \n (Type 'y' for yes or 'n' for no, or 'stat' for your current stats.)")
        if(playeranswer == "stat" or playeranswer == "Stat" or playeranswer == "STAT"):
            CurrentPlayer.printStatSheet()
            continue
        if(playeranswer == "y" or playeranswer == "Y" or playeranswer == ""):
            return True
        else:
            return False

#Game Start
print("GOBLIN RUN             ver: " + str(gameversion))

input("You enter a goblin den. (Press Enter)")
input("Time to clear them out. (Press Enter)")
input("See how far you can get. (Press Enter)")


newroom = Room(CurrentPlayer.level,1,CurrentPlayer)
while(True):
    if(checkfornextroom()):
        newroom = Room(CurrentPlayer.level,1,CurrentPlayer)
        pass
    else:
        print("You run back the way you came.\n You escape the goblin cave.")
        input("Thanks for playing (Press Enter)")
        break
