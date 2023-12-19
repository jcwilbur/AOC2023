from os import read
inputStrings = []
with open('puzzle6/input.txt','r') as inputFile:
    inputStrings = inputFile.readlines()

times = [int(n) for n in inputStrings[0].split()[1:]]
distances = [int(n) for n in inputStrings[1].split()[1:]]

margins = [0]*len(times)
def calcDistanceTraveled(holdTime, raceTime):
    speed = holdTime
    distanceTravled = speed * (raceTime-holdTime)
    return distanceTravled

for x in range(len(times)):
    for option in range(times[x]):
        if calcDistanceTraveled(option,times[x]) > distances[x]:
            margins[x] +=1

answer = 1
for margin in margins:
    answer *= margin
print(answer)