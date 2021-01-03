from GoblinClass import Goblin

#import types
from GoblinTypes import Slimy
from GoblinTypes import Tough
from GoblinTypes import Slow
from GoblinTypes import Fast
from GoblinTypes import Normal
from GoblinTypes import Dumb
from GoblinTypes import GlobalGoblinVars

#global vars
gameversion = 0.1
GoblinTypesList = GlobalGoblinVars.GlobalGoblinTypesList
GoblinBaseStats = GlobalGoblinVars.GlobalGoblinBaseStatsList

#func's
def LevelUp():
    input("You have leveled up. (Press Enter)")
    print("Spd")
    print("Hth")
    print("Str")
    val = input("Type the 3 letter stat you would like to increase: ")
    while True:
        if val == "Spd" or val == "spd":
            print("Speed increase")
            break
        if val == "Hth" or val == "hth":
            print("Health increase")
            break
        if val == "Str" or val == "str":
            print("Strengh increase")
            break
        else:
            print("Try again.")
            val = input("Type the 3 letter stat you would like to increase: ")
    return







#Game Start
print("GOBLIN RUN             ver: " + str(gameversion))

input("You enter a goblin den. (Press Enter)")
input("Time to clear them out. (Press Enter)")
input("See how far you can get. (Press Enter)")

LevelUp()
# Goblin1 = Goblin(Slimy(), 1)
# Goblin1.printStatSheet()
