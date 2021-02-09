from src.PlayerClass import Player
from src.RoomClass import Room
from src.WeaponsClass import Weapon
from src.ArmorClass import Armor
from src.ConsumablesClass import Consumable

gameversion = 1.0
difflevel = 1
startingPlayerLevel = 1
startingPlayerAgility = 10
startingPlayerHealth = 50
startingPlayerStrength = 5
startingMoney = 20

#----------------global vars----------------
#player stat key(level, agility, startingHealth, strength, currentXp, XpToLevel, startingMoney, equipWeapon, equipArmor, itemList, gobRep) gobRep is higher the closer to '1' it gets
CurrentPlayer = Player(startingPlayerLevel,startingPlayerAgility,startingPlayerHealth,startingPlayerStrength,0,1,startingMoney,Weapon(startingPlayerLevel,difflevel),None,[Consumable(startingPlayerLevel,difflevel)],4)

def checkfornextroom():
    while(True):
        playeranswer = input("Would you like to continue? \n (Type 'y' for yes or 'n' for no, 'stat' for your current stats, or 'bag' for your current items.)")
        if(playeranswer == "bag" or playeranswer == "Bag" or playeranswer == "BAG"):
            CurrentPlayer.printItemList()
            if(len(CurrentPlayer.itemList) > 0):
                playeranswer = input("\nWould you like to use an item?")
                if(playeranswer == "y" or playeranswer == "Y"):
                    CurrentPlayer.UsePot()
                    continue
            playeranswer = input("\nWould you like to drop an item?")
            if(playeranswer == "y" or playeranswer == "Y"):
                CurrentPlayer.dropItem()
            continue
        if(playeranswer == "stat" or playeranswer == "Stat" or playeranswer == "STAT"):
            CurrentPlayer.printStatSheet()
            continue
        if(playeranswer == "y" or playeranswer == "Y" or playeranswer == "" or playeranswer == "" or playeranswer == "\\"):
            return True
        if(playeranswer == "n" or playeranswer == "N"):
            return False
        else:
            print("Please enter a valid answer.")
            continue

#Game Start
print("GOBLIN RUN             ver: " + str(gameversion))

input("You enter a goblin den. (Press Enter)")
input("Time to clear them out. \nSee how far you can get. (Press Enter)")
print("\n")
input("Before entering you check your equipment. (Press Enter)")
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