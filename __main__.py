from src.PlayerClass import Player
from src.RoomClass import Room
from src.WeaponsClass import Weapon
from src.ArmorClass import Armor
from src.ConsumablesClass import Consumable

gameversion = 0.8
difflevel = 1
startingPlayerLevel = 1
startingPlayerAgility = 10
startingPlayerHealth = 50
startingPlayerStrength = 5
startingMoney = 20

#----------------global vars----------------
#player stat key(level, agility, startingHealth, strength, currentXp, XpToLevel, startingMoney, equipWeapon, equiparmor, itemList, gobRep) gobRep is higher the closer to '1' it gets
CurrentPlayer = Player(startingPlayerLevel,startingPlayerAgility,startingPlayerHealth,startingPlayerStrength,0,1,startingMoney,None,None,[],4)

def dropItem():
    personalItemList = []
    if(CurrentPlayer.mainWeapon != None):
        personalItemList.append(CurrentPlayer.mainWeapon)
    if(CurrentPlayer.mainArmor != None):
        personalItemList.append(CurrentPlayer.mainArmor)
    for item in CurrentPlayer.itemList:
        personalItemList.append(item)
    if(len(personalItemList) <= 0):
        print("--------Your bag is empty--------\n")
        return
    itemcounter = 1
    for item in personalItemList:
        print("{}-> Your {} can be dropped".format(itemcounter, item.name))
        itemcounter += 1
    while(True):
        playerinputstring = input("Which item would you like to drop? (type a number from '1' to '{}') (Type 'q' to go back.)".format(len(personalItemList)))
        if(playerinputstring == "q" or playerinputstring == "Q" or playerinputstring == "quit" or playerinputstring == "Quit" or playerinputstring == "QUIT"):
            break
        try:
            playertargetInt = int(playerinputstring) -1
            pass
        except ValueError:
            print("Invalid Command!")
            continue
        try:
            chosenitem = personalItemList[playertargetInt]
            if(chosenitem.cat == "w"):
                CurrentPlayer.DiscardWeapon()
                print("You drop your {}.".format(chosenitem.name))
                CurrentPlayer.PayPlayer(int(chosenitem.moneyvalue / CurrentPlayer.goblinRep))
            if(chosenitem.cat == "a"):
                CurrentPlayer.DoffArmor()
                print("You drop your {}.".format(chosenitem.name))
                CurrentPlayer.PayPlayer(int(chosenitem.moneyvalue / CurrentPlayer.goblinRep))
            if(chosenitem.cat == "c"):
                print("You drop the {} from your bag.".format(chosenitem.name))
                CurrentPlayer.PayPlayer(int(chosenitem.moneyvalue / CurrentPlayer.goblinRep))
                personalItemList[playertargetInt] = None
                TempList = []
                for item in personalItemList:
                    if(item != None and item.cat == "c"):
                        TempList.append(item)
                CurrentPlayer.DropItem(TempList)
        except IndexError:
            print("Invalid Item!")
            continue
        return

def checkfornextroom():
    while(True):
        playeranswer = input("Would you like to continue? \n (Type 'y' for yes or 'n' for no, 'stat' for your current stats, or 'bag' for your current items.)")
        if(playeranswer == "bag" or playeranswer == "Bag" or playeranswer == "BAG"):
            CurrentPlayer.printItemList()
            playeranswer = input("\nWould you like to drop an item?")
            if(playeranswer == "y" or playeranswer == "Y"):
                dropItem()
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