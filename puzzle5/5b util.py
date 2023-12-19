from os import read
inputStrings = []
with open('puzzle5/input.txt','r') as inputFile:
    inputStrings = inputFile.readlines()

seedStrings = inputStrings[0][inputStrings[0].find(":")+1:].strip().split()
seedRanges = []
for x in range(0,len(seedStrings),2):
    startIndex = int(seedStrings[x])
    stopIndex = startIndex + int(seedStrings[x+1]) -1
    tempSeeds = range(startIndex, stopIndex)
    newRange = [startIndex, stopIndex]
    seedRanges.append(newRange)
    print("Range added: " + str(newRange))

maps = []
index = 0
maps.append([])
for line in inputStrings[3:]:
    if line[0].isnumeric():
        if len(maps[index]) == 0: maps[index] = []
        maps[index].append([int(n) for n in line.split()])
        pass
    elif line[0].isalpha():
        index += 1
        maps.append([])

#find lowest possible seed number
lowestSeedNum = min(seedRanges, key=lambda obj:obj[0])[0]
highestSeedNum = max(seedRanges, key=lambda obj:obj[0])[0]
print("Lowest possible seed number " + str(lowestSeedNum))
print("Highest possible seed number: " + str(highestSeedNum))

totalDecrement = 0
for map in maps:
    #find largest decrement in step
    largestDecrement = 0
    for line in map:
        temp = line[1] - line[0]
        if temp > largestDecrement: largestDecrement = temp
    print("largest decrement for map: " + str(largestDecrement))
    totalDecrement += largestDecrement

print("total max decrement: " + str(totalDecrement))

print("lowest possible location is" + str(lowestSeedNum - totalDecrement))