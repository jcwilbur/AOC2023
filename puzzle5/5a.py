from os import read
inputStrings = []
with open('puzzle5/input.txt','r') as inputFile:
    inputStrings = inputFile.readlines()

seeds = inputStrings[0][inputStrings[0].find(":")+1:].strip()
maps = []
index = 0
maps.append([])
for line in inputStrings[3:]:
    if line[0].isnumeric():
        if len(maps[index]) == 0: maps[index] = []
        maps[index].append(line.split())
        pass
    elif line[0].isalpha():
        index += 1
        maps.append([])
locations = []
for seed in seeds.split():
    location = int(seed)
    for map in maps:
        #look up location from map table
        for mapline in map:
            startloc = int(mapline[1])
            stoploc = int(mapline[1]) + int(mapline[2]) 
            if location in range(startloc, stoploc):
                offset = location - startloc
                location =  int(mapline[0]) + offset
                break
    locations.append(location)

print(min(locations))