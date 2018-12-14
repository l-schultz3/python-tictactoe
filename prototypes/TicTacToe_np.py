# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 13:04:55 2018

@author: l.schultz3
"""

print("running...")

allGames = np.array([[[None, 0], [None, 0], [None, 0], [None, 0], [None, 0], [None, 0], [None, 0], [None, 0], [None, 0]]])
winningGames = np.array([[[]]])
#winningFirstMoves = np.array([0] * 9

wins = {
        "top horizontal": 0,
        "middle horizontal": 0,
        "bottom horizontal": 0,
        "left vertical": 0,
        "middle vertical": 0,
        "right vertical": 0,
        "backward diagonal": 0,
        "forward diagonal": 0
    }

def checkWin(gameToCheck):
    if (gameToCheck[0][0][0] == gameToCheck[0][1][0] == gameToCheck[0][2][0] and gameToCheck[0][0][0] != None):
        wins["top horizontal"] += 1
        return "top horizontal"
    elif (gameToCheck[0][3][0] == gameToCheck[0][4][0] == gameToCheck[0][5][0] and gameToCheck[0][3][0] != None):
        wins["middle horizontal"] += 1
        return "middle horizontal"
    elif (gameToCheck[0][6][0] == gameToCheck[0][7][0] == gameToCheck[0][8][0] and gameToCheck[0][6][0] != None):
        wins["bottom horizontal"] += 1
        return "bottom horizontal"
    elif (gameToCheck[0][0][0] == gameToCheck[0][3][0] == gameToCheck[0][6][0] and gameToCheck[0][0][0] != None):
        wins["left vertical"] += 1
        return "left vertical"
    elif (gameToCheck[0][1][0] == gameToCheck[0][4][0] == gameToCheck[0][7][0] and gameToCheck[0][1][0] != None):
        wins["middle vertical"] += 1
        return "middle vertical"
    elif (gameToCheck[0][2][0] == gameToCheck[0][5][0] == gameToCheck[0][8][0] and gameToCheck[0][2][0] != None):
        wins["right vertical"] += 1
        return "right vertical"
    elif (gameToCheck[0][0][0] == gameToCheck[0][4][0] == gameToCheck[0][8][0] and gameToCheck[0][0][0] != None):
        wins["backward diagonal"] += 1
        return "backward diagonal"
    elif (gameToCheck[0][2][0] == gameToCheck[0][4][0] == gameToCheck[0][6][0] and gameToCheck[0][2][0] != None):
        wins["forward diagonal"] += 1
        return "forward diagonal"
    else: return False

def cleanGame(gameToClean, moveNumber):
    for j in range(9):
        if (gameToClean[0][j][1] >= moveNumber):
            gameToClean[0][j] = [None, 0]
            
def generateGames():
    global allGames
    global winningGames
    currentGame= np.array([[[None, 0], [None, 0], [None, 0], [None, 0], [None, 0], [None, 0], [None, 0], [None, 0], [None, 0]]])

    for a in range(9):
        if (a == 0):
            print("generating games.", end="")
        elif (a == 8):
            print(".")
        else:
            print(".", end="")
        cleanGame(currentGame, 1)
        currentGame[0][a] = [1, 1]
        for b in range(9):
            cleanGame(currentGame, 2)
            if (currentGame[0][b][0] == None and currentGame[0][b][1] == 0):
                currentGame[0][b] = [0, 2]
                for c in range(9):
                    cleanGame(currentGame, 3)
                    if (currentGame[0][c][0] == None and currentGame[0][c][1] == 0):
                        currentGame[0][c] = [1, 3]
                        for d in range(9):
                            cleanGame(currentGame, 4)
                            if (currentGame[0][d][0] == None and currentGame[0][d][1] == 0):
                                currentGame[0][d] = [0, 4]
                                for e in range(9):
                                    cleanGame(currentGame, 5)
                                    if (currentGame[0][e][0] == None and currentGame[0][e][1] == 0):
                                        currentGame[0][e] = [1, 5]
                                        if (checkWin(currentGame) != False):
                                            winningGames = np.append(winningGames, currentGame, axis=0)
                                            allGames.append(currentGame)
                                        else:
                                            for f in range(9):
                                                cleanGame(currentGame, 6)
                                                if (currentGame[0][f][0] == None and currentGame[0][f][1] == 0):
                                                    currentGame[0][f] = [0, 6]
                                                    if (checkWin(currentGame) != False):
                                                        winningGames.append(currentGame)
                                                        allGames.append(currentGame)
                                                    else:
                                                        for g in range(9):
                                                            cleanGame(currentGame, 7)
                                                            if (currentGame[0][g][0] == None and currentGame[0][g][1] == 0):
                                                                currentGame[0][g] = [1, 7]
                                                                if (checkWin(currentGame) != False):
                                                                    winningGames = np.append(winningGames, currentGame, axis=0)
                                                                    print(winningGames)
                                                                    allGames.append(currentGame)
                                                                else:
                                                                    for h in range(9):
                                                                        cleanGame(currentGame, 8)
                                                                        if (currentGame[0][h][0] == None and currentGame[0][h][1] == 0):
                                                                            currentGame[0][h] = [0, 8]
                                                                            if (checkWin(currentGame) != False):
                                                                                winningGames.append(currentGame)
                                                                                allGames.append(currentGame)
                                                                            else:
                                                                                for i in range(9):
                                                                                    cleanGame(currentGame, 9)
                                                                                    if (currentGame[0][i][0] == None and currentGame[0][i][1] == 0):
                                                                                        currentGame[0][i] = [1, 9]
                                                                                        allGames.append(currentGame)
                                                                                        if (checkWin(currentGame) != False):
                                                                                            winningGames.append(currentGame)
                                                                                            
generateGames()

print("Number of Possible Games:", len(allGames))
print("Number of Winning  Games:", len(winningGames), "\n")

print("completed...")