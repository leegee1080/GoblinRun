from src.PlayerClass import Player
from src.RoomClass import Room
from src.WeaponsClass import Weapon
from src.ArmorClass import Armor
from src.ConsumablesClass import Consumable

gameVersion = 1.0
diffLevel = 1
startingPlayerLevel = 1
startingPlayerAgility = 10
startingPlayerHealth = 50
startingPlayerStrength = 5
startingMoney = 20

#----------------global vars----------------
#player stat key(level, agility, startingHealth, strength, currentXp, XpToLevel, startingMoney, equipWeapon, equipArmor, itemList, gobRep) gobRep is higher the closer to '1' it gets
currentPlayer = Player(startingPlayerLevel,startingPlayerAgility,startingPlayerHealth,startingPlayerStrength,0,1,startingMoney,Weapon(startingPlayerLevel,diffLevel),None,[Consumable(startingPlayerLevel,diffLevel)],4)

def checkForNextRoom():
    while(True):
        playerAnswer = input("Would you like to continue? \n (Type 'y' for yes or 'n' for no, 'stat' for your current stats, or 'bag' for your current items.)")
        if(playerAnswer == "bag" or playerAnswer == "Bag" or playerAnswer == "BAG"):
            currentPlayer.printItemList()
            if(len(currentPlayer.itemList) > 0):
                playerAnswer = input("\nWould you like to use an item?")
                if(playerAnswer == "y" or playerAnswer == "Y"):
                    currentPlayer.UsePot()
                    continue
            playerAnswer = input("\nWould you like to drop an item?")
            if(playerAnswer == "y" or playerAnswer == "Y"):
                currentPlayer.dropItem()
            continue
        if(playerAnswer == "stat" or playerAnswer == "Stat" or playerAnswer == "STAT"):
            currentPlayer.printStatSheet()
            continue
        if(playerAnswer == "y" or playerAnswer == "Y" or playerAnswer == "" or playerAnswer == "" or playerAnswer == "\\"):
            return True
        if(playerAnswer == "n" or playerAnswer == "N"):
            return False
        else:
            print("Please enter a valid answer.")
            continue

#Game Start
print("GOBLIN RUN             ver: " + str(gameVersion))

input("You enter a goblin den. (Press Enter)")
input("Time to clear them out. \nSee how far you can get. (Press Enter)")
print("\n")
input("Before entering you check your equipment. (Press Enter)")
currentPlayer.printItemList()
print("\n")



newRoom = Room(currentPlayer.level,diffLevel,currentPlayer)
while(True):
    if(currentPlayer.health <=0):
        print("\n\nYour bones are added to the pile of other adventurers.\nMaybe in the next life you will get farther.")
        break
    if(checkForNextRoom()):
        newRoom = Room(currentPlayer.level,diffLevel,currentPlayer)
    else:
        print("\n\nYou run back the way you came.\nYou escape the goblin cave.")
        break

input("----->Thanks for playing (Press Enter)")