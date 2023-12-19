from os import read
#declare a list to hold raw input
inputStrings = []
with open('puzzle1/input.txt','r') as inputFile:
   #one line to automatically separate each line into its own entry in the list
    inputStrings = inputFile.readlines()

def replaceNumberStrings(strInput):
        workingString = strInput
        #workingString = workingString.replace("zero", "0")
        workingString = workingString.replace("one", "o1e")
        workingString = workingString.replace("two", "t2o")
        workingString = workingString.replace("three", "t3e")
        workingString = workingString.replace("four", "f4r")
        workingString = workingString.replace("five", "f5e")
        workingString = workingString.replace("six", "s6x")
        workingString = workingString.replace("seven", "s7n")
        workingString = workingString.replace("eight", "e8t")
        workingString = workingString.replace("nine", "n9e")
        return workingString

numArray1 = []
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
    numArray1.append(int(number))

numArray2 = []
for line in inputStrings:
    line = replaceNumberStrings(line)
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
    numArray2.append(int(number))

for i in range(0,len(numArray1)):
    if numArray1[i] != numArray2[i]:
        pass

#sum array
total = 0
for a in numArray2:
    total += a

print(total)


