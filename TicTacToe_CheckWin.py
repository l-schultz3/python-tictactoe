#currentGame = [1, 1, 1, 1, 0, 0, 0, 1, 0] #x

def checkWin(currentGame, value, playerToWin):
    if currentGame[0] + currentGame[1] + currentGame[2] == value:
        return(True)
    elif currentGame[3] + currentGame[4] + currentGame[5] == value:
        return(True)
    elif currentGame[6] + currentGame[7] + currentGame[8] == value:
        return(True)
    elif currentGame[0] + currentGame[3] + currentGame[6] == value:
        return(True)
    elif currentGame[1] + currentGame[4] + currentGame[7] == value:
        return(True)
    elif currentGame[2] + currentGame[5] + currentGame[8] == value:
        return(True)
    elif currentGame[0] + currentGame[4] + currentGame[8] == value:
        return(True)
    elif currentGame[2] + currentGame[4] + currentGame[6] == value:
        return(True)

def runCheckWin(currentGame):
    numberOfMoves = 9

    for i in range(len(currentGame)):
        if currentGame[i] == 5:
            numberOfMoves-=1

    if numberOfMoves % 2 == 1:
        if (checkWin(currentGame, 3, "X")):
            return("X")
    else:
        if (checkWin(currentGame, 0, "O")):
            return("O")

