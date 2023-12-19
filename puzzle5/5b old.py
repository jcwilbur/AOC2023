from os import read
inputStrings = []
with open('puzzle5/test.txt','r') as inputFile:
    inputStrings = inputFile.readlines()

seedStrings = inputStrings[0][inputStrings[0].find(":")+1:].strip().split()
seedRanges = []
for x in range(0,len(seedStrings),2):
    startIndex = int(seedStrings[x])
    stopIndex = startIndex + int(seedStrings[x+1])
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
#sort the final map by final location
maps[0] = sorted(maps[0], key=lambda map: map[0])
#loop through all maplines of final location map
for line in maps[0]:
    #loop through each location of this mapline
    for x in range(line[0],line[0]+line[2]):
        #find corresponding seed number of this final location
        location = x
        for map in maps[1:]:
        #look up location from map table
            for mapline in map:
                startloc = int(mapline[0])
                stoploc = int(mapline[0]) + int(mapline[2]) 
                if location in range(startloc, stoploc):
                    offset = location - startloc
                    location =  int(mapline[1]) + offset
                    break
        #check if this seed number is in the input
        for possibleRange in seedRanges:
            if location in possibleRange:
                print(x)
                break
            
