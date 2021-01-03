class Player:
    StatSheetForPrint = []

    def __init__(self, type, level, speed, health, strength):
        self.type = type
        self.level = level
        self.speed = speed
        self.health = health
        self.strength = strength
    
    def printStatSheet(self):
        self.StatSheetForPrint.clear
        self.StatSheetForPrint.append("Type: " + self.type.name)
        self.StatSheetForPrint.append("Level: " + str(self.level))
        self.StatSheetForPrint.append("Level: " + str(self.speed))
        self.StatSheetForPrint.append("Level: " + str(self.health))
        self.StatSheetForPrint.append("Level: " + str(self.strength))
        print(self.StatSheetForPrint)
        return