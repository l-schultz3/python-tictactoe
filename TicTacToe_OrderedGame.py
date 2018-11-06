import random
import TicTacToe_CheckWin as check
import datetime

allWinningGames = []
foundAMatch = False
numberOfAttempts = 0

def writeGameToFile(currentGame):
    print(currentGame)
    for z in range(9):
        if (z < 8):
            gameFile.write(str(currentGame[z][0]))
        else:
            gameFile.write(str(currentGame[z][0]) + "\n")

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

                        for d in range(9):
                            cleanGame(4, currentGame)
                            if (currentGame[d][0] == 5):
                                currentGame[d][0] = 0
                                currentGame[d][1] = 4

                                for e in range(9):
                                    cleanGame(5, currentGame)
                                    if (currentGame[e][0] == 5):
                                        currentGame[e][0] = 1
                                        currentGame[e][1] = 5

                                        if (check.runCheckWin == "X" or check.runCheckWin == "O"):
                                            writeGameToFile(currentGame)
                                        else:
                                            for f in range(9):
                                                cleanGame(6, currentGame)
                                                if (currentGame[f][0] == 5):
                                                    currentGame[f][0] = 0
                                                    currentGame[f][1] = 6

                                                    if (check.runCheckWin == "X" or check.runCheckWin == "O"):
                                                        writeGameToFile(currentGame)
                                                    else:
                                                        for g in range(9):
                                                            cleanGame(7, currentGame)
                                                            if (currentGame[g][0] == 5):
                                                                currentGame[g][0] = 1
                                                                currentGame[g][1] = 7

                                                                if (check.runCheckWin == "X" or check.runCheckWin == "O"):
                                                                    writeGameToFile(currentGame)
                                                                else:
                                                                    for h in range(9):
                                                                        cleanGame(8, currentGame)
                                                                        if (currentGame[h][0] == 5):
                                                                            currentGame[h][0] = 0
                                                                            currentGame[h][1] = 8

                                                                            if (check.runCheckWin == "X" or check.runCheckWin == "O"):
                                                                                writeGameToFile(currentGame)
                                                                            else:
                                                                                for i in range(9):
                                                                                    cleanGame(9, currentGame)
                                                                                    if (currentGame[i][0] == 5):
                                                                                        currentGame[i][0] = 1
                                                                                        currentGame[i][1] = 9

                                                                                        writeGameToFile(currentGame)

def cleanGame(move, currentGame):
    for j in range(9):
        if (currentGame[j][1] >= move):
            currentGame[j] = [5, 0]

gameFile = open("showGames/gameFile.txt", "w")

generateGame()

gameFile.close()
