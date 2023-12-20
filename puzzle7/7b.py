from os import read
inputStrings = []
with open('puzzle7/input.txt','r') as inputFile:
    inputStrings = inputFile.readlines()

def cardValue(card, position):
    faceValue = 0
    match card:
        case "A":
            faceValue = 14
        case "K":
            faceValue = 13
        case "Q": 
            faceValue = 12
        case "J":
            faceValue = 1
        case "T":
            faceValue = 10
        case _ :
            faceValue = int(card)
    
    positionalValue = 0
    match position:
        case 0:
            positionalValue =100000000
        case 1:
            positionalValue = 1000000
        case 2: 
            positionalValue = 10000
        case 3:
            positionalValue = 100
        case 4:
            positionalValue = 1
    
    return faceValue * positionalValue

def isFiveOfAKind(hand):
    workingHand = hand
    workingHand = workingHand.replace("J","")
    jokers = hand.count("J")
    maxCount = 0
    for card in workingHand:
        if hand.count(card) > maxCount:
            maxCount = hand.count(card)
    if maxCount + jokers == 5:
        return True
    return False

def isFourOfAKind(hand):
    workingHand = hand
    workingHand = workingHand.replace("J","")
    jokers = hand.count("J")
    maxCount = 0
    for card in workingHand:
        if hand.count(card) > maxCount:
            maxCount = hand.count(card)
    if maxCount + jokers == 4:
        return True
    return False

def isFullHouse(hand):
    workingHand = hand
    workingHand = workingHand.replace("J","")
    jokers = hand.count("J")
    maxCount = 0
    for card in workingHand:
        if hand.count(card) > maxCount:
            maxCount = hand.count(card)
            countedVal = card
    if maxCount + jokers == 3:
        workingHand = workingHand.replace(countedVal,"")
        secondCount = 0
        for card in workingHand:
            count = 0
            if workingHand.count(card) > secondCount:
                secondCount = hand.count(card)
        if secondCount ==2:
            return True
    return False

def isThreeOfAKind(hand):
    workingHand = hand
    workingHand = workingHand.replace("J","")
    jokers = hand.count("J")
    maxCount = 0
    for card in workingHand:
        if hand.count(card) > maxCount:
            maxCount = hand.count(card)
    if maxCount + jokers == 3:
        return True
    return False

def isTwoPair(hand):
    workingHand = hand
    workingHand = workingHand.replace("J","")
    jokers = hand.count("J")
    maxCount = 0
    for card in workingHand:
        if hand.count(card) > maxCount:
            maxCount = hand.count(card)
            countedVal = card
    if maxCount + jokers == 2:
        workingHand = workingHand.replace(countedVal,"")
        secondCount = 0
        for card in workingHand:
            count = 0
            if workingHand.count(card) > secondCount:
                secondCount = hand.count(card)
        if secondCount ==2:
            return True
    return False

def isOnePair(hand):
    workingHand = hand
    workingHand = workingHand.replace("J","")
    jokers = hand.count("J")
    maxCount = 0
    for card in workingHand:
        if hand.count(card) > maxCount:
            maxCount = hand.count(card)
    if maxCount + jokers == 2:
        return True
    return False

def calcHandValue(hand):
    value = 0
    if(isFiveOfAKind(hand)):
        value += 600000000000
    elif(isFourOfAKind(hand)):
        value += 500000000000
    elif(isFullHouse(hand)):
        value += 400000000000
    elif(isThreeOfAKind(hand)):
        value += 300000000000
    elif(isTwoPair(hand)):
        value += 200000000000
    elif(isOnePair(hand)):
        value += 100000000000
    for x in range(len(hand)):
        value += cardValue(hand[x],x)
    return value

hands = []
for line in inputStrings:
    hand = line.split()
    hand.append(calcHandValue(hand[0]))
    hands.append(hand)

hands.sort(key=lambda n: n[2])

answer = 0
for x in range(len(hands)):
    answer += int(hands[x][1]) * (x+1)

print(answer)
