from src.GameManager import GlobalVarStorage
from src.PlayerClass import Player
from src.RoomClass import Room
# from src.GoblinClass import Goblin
# from src.FightClass import Fight

gameversion = 0.5

#----------------global vars----------------
#player stat key(level, speed, startingHealth, strength, currentXp, XpToLevel)
CurrentPlayer = Player(1,10,50,5,0,1)

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
input("Time to clear them out. \nSee how far you can get. (Press Enter)")
print("\n")



newroom = Room(CurrentPlayer.level,1,CurrentPlayer)
while(True):
    if(CurrentPlayer.health <=0):
        print("\n\nYour bones are added to the pile of other adventurers.\nMaybe in the next life you will get farther.")
        break
    if(checkfornextroom()):
        newroom = Room(CurrentPlayer.level,1,CurrentPlayer)
    else:
        print("\n\nYou run back the way you came.\nYou escape the goblin cave.")
        break

input("----->Thanks for playing (Press Enter)")