import random
import TicTacToe_CheckWin as check

allWinningGames = []
foundAMatch = False
numberOfAttempts = 0

def generateGame():
    currentGameMatches = False
    currentGame = [5, 5, 5, 5, 5, 5, 5, 5, 5]
    gameWon = False
    numberOfMoves = 1 #starts at one for easy placement starting with x

    while gameWon == False:
        indexToPlace = random.randint(0, 8)
        if (currentGame[indexToPlace] == 5):
            currentGame[indexToPlace] = numberOfMoves % 2
            numberOfMoves+=1

        if (check.runCheckWin(currentGame) == "X" or check.runCheckWin(currentGame) == "O"):
            gameWon = True

        if (numberOfMoves == 9):
            break

    if (gameWon):
        """print(currentGame[0], currentGame[1], currentGame[2])
        print(currentGame[3], currentGame[4], currentGame[5])
        print(currentGame[6], currentGame[7], currentGame[8])
        print("\n")"""

        try:
            for i in range(len(allWinningGames)):
                if (currentGame == allWinnningGames[i]):
                    currentGameMatches = True
                    print("SAME")
        except:
            pass

        if (currentGameMatches == False):
            allWinningGames.append(currentGame)
        else:
            foundAMatch = True
            
        #print(allWinningGames)
    else:
        pass
        #print("No winner\n")

while (foundAMatch == False):
    generateGame()
    numberOfAttempts += 1
    print("\n", numberOfAttempts)
    
print(allWinningGames)
    
