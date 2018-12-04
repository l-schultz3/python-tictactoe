print("running...")

allGames = []
winningGames = []

#Will my code ever work? ~ Luke
def checkWin(gameToCheck):
    if (gameToCheck[0][0] == gameToCheck[1][0] == gameToCheck[2][0] and gameToCheck[0][0] != None): return "top horizontal"
    elif (gameToCheck[3][0] == gameToCheck[4][0] == gameToCheck[5][0] and gameToCheck[3][0] != None): return "middle horizontal"
    elif (gameToCheck[6][0] == gameToCheck[7][0] == gameToCheck[8][0] and gameToCheck[6][0] != None): return "bottom horizontal"
    elif (gameToCheck[0][0] == gameToCheck[3][0] == gameToCheck[6][0] and gameToCheck[0][0] != None): return "left vertical"
    elif (gameToCheck[1][0] == gameToCheck[4][0] == gameToCheck[7][0] and gameToCheck[1][0] != None): return "middle vertical"
    elif (gameToCheck[2][0] == gameToCheck[5][0] == gameToCheck[8][0] and gameToCheck[2][0] != None): return "right vertical"
    elif (gameToCheck[0][0] == gameToCheck[4][0] == gameToCheck[8][0] and gameToCheck[0][0] != None): return "backward diagonal"
    elif (gameToCheck[2][0] == gameToCheck[4][0] == gameToCheck[6][0] and gameToCheck[2][0] != None): return "forward diagonal"
    else: return False

def cleanGame(gameToClean, moveNumber):
    for j in range(9):
        if (gameToClean[j][1] >= moveNumber):
            gameToClean[j] = [None, 0]

def generateGames():
    global allGames
    global winningGames
    currentGame= [[None, 0], [None, 0], [None, 0], [None, 0], [None, 0], [None, 0], [None, 0], [None, 0], [None, 0]]

    for a in range(9):
        cleanGame(currentGame, 1)
        currentGame[a] = [1, 1]
        for b in range(9):
            cleanGame(currentGame, 2)
            if (currentGame[b] == [None, 0]):
                currentGame[b] = [0, 2]
                for c in range(9):
                    cleanGame(currentGame, 3)
                    if (currentGame[c] == [None, 0]):
                        currentGame[c] = [1, 3]
                        for d in range(9):
                            cleanGame(currentGame, 4)
                            if (currentGame[b] == [None, 0]):
                                currentGame[d] = [0, 4]
                                for e in range(9):
                                    cleanGame(currentGame, 5)
                                    if (currentGame[e] == [None, 0]):
                                        currentGame[e] = [1, 5]
                                        print(currentGame)
                                        if (checkWin(currentGame) != False):
                                            print(True)
#                                        allGames.append(currentGame)
                                            winningGames.append(currentGame)
                                        else:
                                            for f in range(9):
                                                cleanGame(currentGame, 6)
                                                if (currentGame[f] == [None, 0]):
                                                    currentGame[f] = [0, 6]
                                                    if (checkWin(currentGame) != False):
#                                                    allGames.append(currentGame)
                                                        winningGames.append(currentGame)
                                                    else:
                                                        for g in range(9):
                                                            cleanGame(currentGame, 7)
                                                            if (currentGame[g] == [None, 0]):
                                                                currentGame[g] = [1, 7]
                                                                if (checkWin(currentGame) != False):
#                                                                allGames.append(currentGame)
                                                                    winningGames.append(currentGame)
                                                                else:
                                                                    for h in range(9):
                                                                        cleanGame(currentGame, 8)
                                                                        if (currentGame[h] == [None, 0]):
                                                                            currentGame[h] = [0, 8]
                                                                            if (checkWin(currentGame) != False):
#                                                                            allGames.append(currentGame)
                                                                                winningGames.append(currentGame)
                                                                            else:
                                                                                for i in range(9):
                                                                                    cleanGame(currentGame, 9)
                                                                                    if (currentGame[i] == [None, 0]):
                                                                                        currentGame[i] = [1, 9]
                                                                                        print(currentGame)
#                                                                                    allGames.append(currentGame)
                                                                                    #print(len(allGames))
                                                                                        if (checkWin(currentGame) != False):
                                                                                            winningGames.append(currentGame)
                                                                                            print(currentGame)
                                                                                        else:
                                                                                            print(currentGame)
generateGames()

print(len(allGames))
print(len(winningGames))

print("completed...")
