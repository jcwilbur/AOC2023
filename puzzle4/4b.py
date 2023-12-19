from os import read
inputStrings = []
with open('puzzle4/input.txt','r') as inputFile:
    inputStrings = inputFile.readlines()

cardCounts = [1] * len(inputStrings)
index = 0
for line in inputStrings:
    for x in range(cardCounts[index]):
        matches = 0
        line = line[line.find(":")+1:].strip()
        game = line.split("|")
        winningNums = game[0].split()
        myNums = game[1].split()
        for num in myNums:
            if num in winningNums:
                matches = matches + 1
        for y in range(matches):
            cardCounts[index+y+1] = cardCounts[index+y+1] + 1
    index = index + 1

score = 0
for num in cardCounts:
    score = score + num
print(score)