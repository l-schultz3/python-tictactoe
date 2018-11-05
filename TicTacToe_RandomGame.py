import random
import TicTacToe_CheckWin as check
import datetime

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

        for i in range(len(allWinningGames)):
            if (currentGame == allWinningGames[i]):
                return(True)

        if (currentGameMatches == False):
            allWinningGames.append(currentGame)
            
    else:
        pass
        #print("No winner\n")

while (numberOfAttempts < 1000):
    if (generateGame()):
        foundAMatch = True
    numberOfAttempts += 1
    print("NumberOfAttempts: ", numberOfAttempts)
    #print("Found A Match: ", foundAMatch)

winFile = open("winFile.txt", "w")
winFile.write(str(datetime.datetime.now()))

for i in range(len(allWinningGames)):
    winFile.write("\n")
    for j in range(len(allWinningGames[i])):
        winFile.write(str(allWinningGames[i][j]))
    
print(allWinningGames)

winFile.close()
    
