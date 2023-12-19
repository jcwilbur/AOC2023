from os import read
#declare a list to hold raw input
inputStrings = []
with open('puzzle3/test.txt','r') as inputFile:
   #one line to automatically separate each line into its own entry in the list
    inputStrings = inputFile.readlines()

class Number:
    def __init__(self, number, firstX, lastX, y, isPart) -> None:
        self.number = number
        self.firstX = firstX
        self.lastX = lastX
        self.y = y
        self.isPart = isPart

def checkForParts(xIn, yIn, numSet):
    for num in numSet:
        if num.y >= yIn - 1 and num.y <= yIn +1:
            #checkforx axis neighbor
            if xIn in range(num.firstX, num.lastX ):
                num.isPart = True

numbers = []
yAxis = 0
for line in inputStrings:
    #extract the numbers
    tempNum = ""
    previousX = 0
    for linechar in line:
     if str.isnumeric(linechar):
        tempNum = tempNum +linechar
     elif not tempNum == "":
        value = int(tempNum)
        tempFirstX = str.find(line,tempNum,previousX)
        tempLastX = tempFirstX + len(tempNum) -1
        tempY = yAxis
        previousX = tempLastX
        numbers.append(Number(value,tempFirstX, tempLastX, tempY,False))
        tempNum = ""
    
    #check for Symbols. Go character by character - no need for splits because they're always only one character long
    #turn Numbers into parts on current line and previous line
    yAxis = yAxis +1

yIndex = 0
for line in inputStrings:
    xIndex = 0
    for linechar in line:
        if (not linechar.isalnum() and not linechar == "." and not linechar == "\n"):
            print(linechar + " " + str(xIndex) + " " + str(yIndex))
            checkForParts(xIndex, yIndex, numbers)
        xIndex = xIndex + 1
    yIndex = yIndex + 1


sum = 0

for number in numbers:
    if number.isPart:
        sum += number.number
