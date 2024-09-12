import random

def prizefn():
    prize = random.randint(1,3)

    if prize == 1:
        return "1,000,000 Dollars"
    elif prize == 2:
        return "1 year subscription to Elle Magazine"
    else:
        return "Brand new Rolls Royce"

gameRange = input("What range of numbers do you want your game to be : ")
gameRange = int(gameRange)

playerturns = input("How many tries for the game : ")
playerturns = int(playerturns)

magicNum = random.randint(1,gameRange)
playerGuess = -1


print(magicNum)

while (playerGuess!=magicNum) and (playerturns >-1 ):
    print("You have " + str(playerturns) + " turns , good luck!")
    playerGuess = input("What is your guess for the magic number : ")
    playerGuess = int(playerGuess)

