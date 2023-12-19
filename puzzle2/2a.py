from os import read
#declare a list to hold raw input
inputStrings = []
with open('puzzle2/input.txt','r') as inputFile:
   #one line to automatically separate each line into its own entry in the list
    inputStrings = inputFile.readlines()

maxValues = (12,13,14)

class Game:
    def __init__(self, index, reds, greens, blues):
        self.index = index
        self.reds = reds
        self.greens = greens
        self.blues = blues

    def isValid(self):
        if(max(self.reds) <= maxValues[0] and max(self.greens) <= maxValues[1] and max(self.blues) <=maxValues[2]):
            return True
        else:
            return False
        
gameList = []
for line in inputStrings:
    #parse lines into Game objects
    index = 0
    reds = []
    greens = []
    blues = []
    templine = line.split(":")
    index = int(templine[0][5:])
    draws = templine[1].split(";")
    for draw in draws:
        sets = draw.split(",")
        for set in sets:
            split = set.split()
            num = int(split[0])
            color = split[1]
            match color:
                case "red":
                    reds.append(num)
                case "green":
                    greens.append(num)
                case "blue":
                    blues.append(num)
                case _:
                    raise Exception
    gameList.append(Game(index, reds, greens, blues))
            
sumOfValidGames = 0

for game in gameList:
    if game.isValid():
        sumOfValidGames += game.index

print(sumOfValidGames)