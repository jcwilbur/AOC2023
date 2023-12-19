from os import read
inputStrings = []
with open('puzzle5/test.txt','r') as inputFile:
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


print(seeds)