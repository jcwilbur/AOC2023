from os import read
#declare a list to hold raw input
inputStrings = []
with open('puzzle1/input.txt','r') as inputFile:
   #one line to automatically separate each line into its own entry in the list
    inputStrings = inputFile.readlines()


numArray = []
for line in inputStrings:
    number = ""
    #find first number
    for element in line:
        if(element.isdigit()):
            number = number + element
            break
   
   #find last number
    for element in line[ : :-1]:
        if(element.isdigit()):
            number = number + element
            break
    numArray.append(int(number))

#sum array
total = 0
for a in numArray:
    total += a

print(total)