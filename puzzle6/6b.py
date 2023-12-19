from os import read
inputStrings = []
with open('puzzle6/input.txt','r') as inputFile:
    inputStrings = inputFile.readlines()

time = int(inputStrings[0].split(":")[1:][0].strip().replace(" ",""))
distance = int(inputStrings[1].split(":")[1:][0].strip().replace(" ",""))

margin = 0
def calcDistanceTraveled(holdTime, raceTime):
    speed = holdTime
    distanceTravled = speed * (raceTime-holdTime)
    return distanceTravled

#find first win
firstWinOption = 0
for option in range(time):
    if calcDistanceTraveled(option,time) > distance:
        firstWinOption = option
        break

#find last win
lastWinOption = 0
for option in range(time,0,-1):
    if calcDistanceTraveled(option,time) > distance:
        lastWinOption = option
        break

print(lastWinOption - firstWinOption + 1)