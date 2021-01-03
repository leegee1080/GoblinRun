from GoblinClass import Goblin
from PlayerClass import Player

# if __name__ == "__main__":
#     # execute only if run as a script
#     main()


#global vars
gameversion = 0.1
CurrentPlayer = Player(1,1,1,1)

#func's
def LevelUp():
    input("You have leveled up. (Press Enter)")
    print("Spd")
    print("Hth")
    print("Str")
    val = input("Type the 3 letter stat you would like to increase: ")
    while True:
        if val == "Spd" or val == "spd":
            CurrentPlayer.increaseSpeed(1)
            break
        if val == "Hth" or val == "hth":
            CurrentPlayer.increaseHealth(1)
            break
        if val == "Str" or val == "str":
            CurrentPlayer.increaseStrength(1)
            break
        else:
            print("Try again.")
            val = input("Type the 3 letter stat you would like to increase: ")
    CurrentPlayer.increaseLevel(1)
    return







#Game Start
print("GOBLIN RUN             ver: " + str(gameversion))

input("You enter a goblin den. (Press Enter)")
input("Time to clear them out. (Press Enter)")
input("See how far you can get. (Press Enter)")

LevelUp()

# Goblin1 = Goblin("Slimy", 1)
# Goblin1.printStatSheet()
CurrentPlayer.printStatSheet()
