import random
import TicTacToe_CheckWin as check
import datetime

allWinningGames = []
foundAMatch = False
numberOfAttempts = 0

def generateGame():
    currentGameMatches = False
    currentGame = [[5, 0], [5, 0], [5, 0], [5, 0], [5, 0], [5, 0], [5, 0], [5, 0], [5, 0]]
    gameWon = False
    numberOfMoves = 1 #starts at one for easy placement starting with x

    for a in range(9):
        cleanGame(1, currentGame)
        
        currentGame[a][0] = 1
        currentGame[a][1] = 1
        for b in range(9):
            cleanGame(2, currentGame)
            if (currentGame[b][0] == 5):
                currentGame[b][0] = 0
                currentGame[b][1] = 2

                for c in range(9):
                    cleanGame(3, currentGame)
                    if (currentGame[c][0] == 5):
                        currentGame[c][0] = 1
                        currentGame[c][1] = 3
                        print(currentGame)
                        gameFile.write("\n")
                        for i in range(9):
                            if (i == 0):
                                gameFile.write("{" + str(currentGame[i][0]) + ", ")
                            elif (i < 8):
                                gameFile.write(str(currentGame[i][0]) + ", ")
                            else:
                                gameFile.write(str(currentGame[i][0]) + "}, ")

def cleanGame(move, currentGame):
    for j in range(9):
        if (currentGame[j][1] >= move):
            currentGame[j] = [5, 0]

gameFile = open("gameFile.txt", "w")

generateGame()

gameFile.close()
