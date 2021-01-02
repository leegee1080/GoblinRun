class Goblin:
    StatSheet = []
    def __init__(self, type, level):
        self.type = type
        self.level = level
    
    def printStatSheet(self):
        self.StatSheet.clear
        self.StatSheet.append("Type: " + self.type.name)
        self.StatSheet.append("Level: " + str(self.level))
        print(self.StatSheet)
        return