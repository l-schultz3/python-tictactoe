allGames = []
allWins = []
drawGames = []
xWins = []
oWins = []

wins = {
        "2d": 0,
        "3d": 0
    }

def check2dWin(gameToCheck, dis):
    base = 9 * dis
    if ((gameToCheck[0+base] % 2) == (gameToCheck[1+base] % 2) == (gameToCheck[2+base] % 2) and (gameToCheck[0+base]) != 0 and (gameToCheck[1+base]) != 0 and (gameToCheck[2+base]) != 0):
        wins["2d"] += 1
        return True
    elif ((gameToCheck[3+base] % 2) == (gameToCheck[4+base] % 2) == (gameToCheck[5+base] % 2) and (gameToCheck[3+base]) != 0 and (gameToCheck[4+base]) != 0 and (gameToCheck[5+base]) != 0):
        wins["2d"] += 1
        return True
    elif ((gameToCheck[6+base] % 2) == (gameToCheck[7+base] % 2) == (gameToCheck[8+base] % 2) and (gameToCheck[6+base]) != 0 and (gameToCheck[7+base]) != 0 and (gameToCheck[8+base]) != 0):
        wins["2d"] += 1
        return True
    elif ((gameToCheck[0+base] % 2) == (gameToCheck[3+base] % 2) == (gameToCheck[6+base] % 2) and (gameToCheck[0+base]) != 0 and (gameToCheck[3+base]) != 0 and (gameToCheck[6+base]) != 0):
        wins["2d"] += 1
        return True
    elif ((gameToCheck[1+base] % 2) == (gameToCheck[4+base] % 2) == (gameToCheck[7+base] % 2) and (gameToCheck[1+base]) != 0 and (gameToCheck[4+base]) != 0 and (gameToCheck[7+base]) != 0):
        wins["2d"] += 1
        return True
    elif ((gameToCheck[2+base] % 2) == (gameToCheck[5+base] % 2) == (gameToCheck[8+base] % 2) and (gameToCheck[2+base]) != 0 and (gameToCheck[5+base]) != 0 and (gameToCheck[8+base]) != 0):
        wins["2d"] += 1
        return True
    elif ((gameToCheck[0+base] % 2) == (gameToCheck[4+base] % 2) == (gameToCheck[8+base] % 2) and (gameToCheck[0+base]) != 0 and (gameToCheck[4+base]) != 0 and (gameToCheck[8+base]) != 0):
        wins["2d"] += 1
        return True
    elif ((gameToCheck[2+base] % 2) == (gameToCheck[4+base] % 2) == (gameToCheck[6+base] % 2) and (gameToCheck[2+base]) != 0 and (gameToCheck[4+base]) != 0 and (gameToCheck[6+base]) != 0):
        wins["2d"] += 1
        return True
    else:
        return False

def checkThroughWin(gameToCheck):
    for i in range(9):
        if ((gameToCheck[index] % 2) == (gameToCheck[index + 9] % 2) == (gameToCheck[index + 18] % 2) and ((gameToCheck[index]) != 0 and (gameToCheck[index + 9]) != 0 and (gameToCheck[index + 18]) != 0)):
            wins["3d"] += 1
            return True
    else: return False


def checkWin(gameToCheck):
    if (check2dWin(gameToCheck, 0) or checkThroughWin(gameToCheck)):
        return True
    else: return False

def recursion(arr, n):
    if (checkWin(arr)):
        allGames.append(arr)
        allWins.append(arr)
    elif (n <= 8):        
        fillNextMove(arr, n + 1)
    else:
        allGames.append(arr)
        drawGames.append(arr)

def fillNextMove(arr, move):
    newArrs = []
    for i in range(len(arr)):
        if (arr[i] == 0):
            tempArr = arr.copy()
            tempArr[i] = move
            newArrs.append(tempArr)

    for newArr in newArrs:
        if (newArr != []):
            recursion(newArr, move)

recursion([0] * 9, 0)

def printStats():
    global allGames, allWins, xWins, oWins, wins, winningFirstMoves

    print(len(allGames), "total number of games")
    print(len(allWins), "total number of winning games")
    print(len(drawGames), "total number of drawn games")

printStats()

