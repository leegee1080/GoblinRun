from GoblinClass import Goblin
from PlayerClass import Player

# if __name__ == "__main__":
#     # execute only if run as a script
#     main()


#global vars
gameversion = 0.1
CurrentPlayer = Player(1,1,1,1,0,1)











#Game Start
print("GOBLIN RUN             ver: " + str(gameversion))

input("You enter a goblin den. (Press Enter)")
input("Time to clear them out. (Press Enter)")
input("See how far you can get. (Press Enter)")

CurrentPlayer.IncreaseXP(10)

# Goblin1 = Goblin("Slimy", 1)
# Goblin1.printStatSheet()
