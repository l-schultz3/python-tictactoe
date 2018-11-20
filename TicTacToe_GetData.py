import random
import TicTacToe_CheckWin as check
import datetime

print("running...")

allWinningGames = [[]]
foundAMatch = False
numberOfAttempts = 0
onlyWinningGames = True
numberOfFirstMoves = [0, 0, 0, 0, 0, 0, 0, 0, 0]

def writeGameToFile(currentGame):
    #print(currentGame)
    #allWinningGames.append(currentGame)
    #gameFile.write(str(currentGame) + ",\n")
    pass

def checkWin(currentGame):
    checkCurrentGame = [5, 5, 5, 5, 5, 5, 5, 5, 5]
    for i in range(9):
        checkCurrentGame[i] = currentGame[i][0]
        #print(checkCurrentGame)
    if (check.checkWin(checkCurrentGame, 3) or check.checkWin(checkCurrentGame, 0)):
        writeGameToFile(currentGame)
        #print("true")
        return(True)

def cleanGame(move, currentGame):
    for j in range(9):
        if (currentGame[j][1] >= move):
            currentGame[j] = [5, 0]

def checkBestMove():
    """print(allWinningGames[0][1])
    print(allWinningGames[0][2])"""
    """for index in range(len(allWinningGames)):
        if (allWinningGames[index] != [[5, 0], [5, 0], [5, 0], [5, 0], [5, 0], [5, 0], [5, 0], [5, 0], [1, 1]]):
            print(index)"""
    #print(allWinningGames[1])
    for index in range(len(allWinningGames)):
        for i in range(9):
            if (allWinningGames[index][i][1] == 1):
                numberOfFirstMoves[i] += 1

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

                                        if (checkWin(currentGame)):
                                            #writeGameToFile(currentGame)
                                            allWinningGames.append(currentGame)
                                        else:
                                            for f in range(9):
                                                cleanGame(6, currentGame)
                                                if (currentGame[f][0] == 5):
                                                    currentGame[f][0] = 0
                                                    currentGame[f][1] = 6

                                                    if (checkWin(currentGame)):
                                                        #writeGameToFile(currentGame)
                                                        allWinningGames.append(currentGame)
                                                    else:
                                                        for g in range(9):
                                                            cleanGame(7, currentGame)
                                                            if (currentGame[g][0] == 5):
                                                                currentGame[g][0] = 1
                                                                currentGame[g][1] = 7

                                                                if (checkWin(currentGame)):
                                                                    #writeGameToFile(currentGame)
                                                                    allWinningGames.append(currentGame)
                                                                else:
                                                                    for h in range(9):
                                                                        cleanGame(8, currentGame)
                                                                        if (currentGame[h][0] == 5):
                                                                            currentGame[h][0] = 0
                                                                            currentGame[h][1] = 8

                                                                            if (checkWin(currentGame)):
                                                                                #writeGameToFile(currentGame)
                                                                                allWinningGames.append(currentGame)
                                                                            else:
                                                                                for i in range(9):
                                                                                    cleanGame(9, currentGame)
                                                                                    if (currentGame[i][0] == 5):
                                                                                        currentGame[i][0] = 1
                                                                                        currentGame[i][1] = 9

                                                                                        if (checkWin(currentGame)): 
                                                                                            #writeGameToFile(currentGame)
                                                                                            allWinningGames.append(currentGame)
                                                                                            #print(currentGame)
                                                                                        

generateGame()

#print(allWinningGames)

checkBestMove()

print(numberOfFirstMoves)

print("completed...")