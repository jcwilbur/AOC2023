from os import read
inputStrings = []
with open('puzzle4/input.txt','r') as inputFile:
    inputStrings = inputFile.readlines()

score = 0
for line in inputStrings:
    matches = 0
    line = line[line.find(":")+1:].strip()
    game = line.split("|")
    winningNums = game[0].split()
    myNums = game[1].split()
    for num in myNums:
        if num in winningNums:
            matches = matches + 1
    if(matches >0):
        score = score + (2**(matches-1))


print(score)