from os import read
#declare a list to hold raw input
inputStrings = []
with open('puzzle2/input.txt','r') as inputFile:
   #one line to automatically separate each line into its own entry in the list
    inputStrings = inputFile.readlines()

class Game:
    def __init__(self, index, reds, greens, blues):
        self.index = index
        self.reds = reds
        self.greens = greens
        self.blues = blues
    
    def calcPower(self):
        return max(self.reds) * max(self.greens) * max(self.blues)
        
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

answer = 0

for game in gameList:
    answer += game.calcPower()

print(answer)