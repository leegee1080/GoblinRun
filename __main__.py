from src.GameManager import GlobalVarStorage
from src.PlayerClass import Player
from src.RoomClass import Room
from src.Items import NewItem
# from src.GoblinClass import Goblin
# from src.FightClass import Fight

gameversion = 0.5
difflevel = 1

#----------------global vars----------------
#player stat key(level, speed, startingHealth, strength, currentXp, XpToLevel, startingMoney, equipWeapon, equiparmor, itemList)
CurrentPlayer = Player(1,10,50,5,0,1,0,NewItem(1,difflevel,"weapon"), NewItem(1,difflevel,"armor"),[])

def checkfornextroom():
    while(True):
        playeranswer = input("Would you like to continue? \n (Type 'y' for yes or 'n' for no, 'stat' for your current stats, or 'bag' for your current items.)")
        if(playeranswer == "bag" or playeranswer == "Bag" or playeranswer == "BAG"):
            CurrentPlayer.printItemList()
            continue
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
input("Before entering you check your equipment. (Press Enter)")
CurrentPlayer.printStatSheet()
CurrentPlayer.printItemList()
print("\n")



newroom = Room(CurrentPlayer.level,difflevel,CurrentPlayer)
while(True):
    if(CurrentPlayer.health <=0):
        print("\n\nYour bones are added to the pile of other adventurers.\nMaybe in the next life you will get farther.")
        break
    if(checkfornextroom()):
        newroom = Room(CurrentPlayer.level,difflevel,CurrentPlayer)
    else:
        print("\n\nYou run back the way you came.\nYou escape the goblin cave.")
        break

input("----->Thanks for playing (Press Enter)")