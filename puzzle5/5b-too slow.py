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

maps.reverse()
#loop through all possible ending locations, starting with zero, until you find a match
#todo, there's probably a better min location, depending on the max difference between column 1 and column 2, that could skip a lot of numbers
location = 0
found = False
OGlocation = 0
#i kept the max value of the last run here so I could restart not from zero if I needed to pause the program
OGlocation = 40000000
while not found: 
    print("Tracing back seed number for location " + str(OGlocation))
    location = OGlocation
    #find corresponding seed number of this final location
    for map in maps:
    #look up location from map table
        for mapline in map:
            startloc = int(mapline[0])
            stoploc = int(mapline[0]) + int(mapline[2]) 
            if location in range(startloc, stoploc):
                offset = location - startloc
                location =  int(mapline[1]) + offset
                break
    #check if this seed number is in the input
    print("Checking for seed " + str(location))
    for possibleRange in seedRanges:
        if location in range(possibleRange[0], possibleRange[1]):
            print("valid location found: " + str(OGlocation))
            found = True
    OGlocation += 1
            
