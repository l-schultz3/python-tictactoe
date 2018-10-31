import random
import TicTacToe_CheckWin as check

def generateGame():
    currentGame = [5, 5, 5, 5, 5, 5, 5, 5, 5]
    gameFinished = False
    numberOfMoves = 1 #starts at one for easy placement starting with x

    while gameFinished == False:
        indexToPlace = random.randint(0, 8)
        if (currentGame[indexToPlace] == 5):
            currentGame[indexToPlace] = numberOfMoves % 2
            numberOfMoves+=1

        if (check.runCheckWin(currentGame) == True):
            gameFinished = True

        """gameFull = True
        for i in range(9):
            if (currentGame[i] == 2):
                gameFull = False"""

    print(currentGame[0], currentGame[1], currentGame[2])
    print(currentGame[3], currentGame[4], currentGame[5])
    print(currentGame[6], currentGame[7], currentGame[8])
    print("\n")

    #return currentGame

for i in range(1):
    generateGame()
    
#hi luke, im bored, a lot, like rly, ALOT
