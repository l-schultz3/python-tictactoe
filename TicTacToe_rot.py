allGames = []
allWins = []
drawGames = []
xWins = []
oWins = []
ind = 0
convertedWins = []

movesToWin = [0] * 5

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

winningFirstMoves = [0] * 9
losingFirstMoves = [0] * 9

def checkFirstMoves(arr, index, arrayToWrite):
    for i in range(len(arr)):
        if (arr[i] == index):
            arrayToWrite[i] += 1

def checkWin(gameToCheck):
    if ((gameToCheck[0] % 2) == (gameToCheck[1] % 2) == (gameToCheck[2] % 2) and (gameToCheck[0]) != 0 and (gameToCheck[1]) != 0 and (gameToCheck[2]) != 0):
        wins["top horizontal"] += 1
        return (gameToCheck[0] % 2) + 1
    elif ((gameToCheck[3] % 2) == (gameToCheck[4] % 2) == (gameToCheck[5] % 2) and (gameToCheck[3]) != 0 and (gameToCheck[4]) != 0 and (gameToCheck[5]) != 0):
        wins["middle horizontal"] += 1
        return (gameToCheck[3] % 2) + 1
    elif ((gameToCheck[6] % 2) == (gameToCheck[7] % 2) == (gameToCheck[8] % 2) and (gameToCheck[6]) != 0 and (gameToCheck[7]) != 0 and (gameToCheck[8]) != 0):
        wins["bottom horizontal"] += 1
        return (gameToCheck[6] % 2) + 1
    elif ((gameToCheck[0] % 2) == (gameToCheck[3] % 2) == (gameToCheck[6] % 2) and (gameToCheck[0]) != 0 and (gameToCheck[3]) != 0 and (gameToCheck[6]) != 0):
        wins["left vertical"] += 1
        return (gameToCheck[0] % 2) + 1
    elif ((gameToCheck[1] % 2) == (gameToCheck[4] % 2) == (gameToCheck[7] % 2) and (gameToCheck[1]) != 0 and (gameToCheck[4]) != 0 and (gameToCheck[7]) != 0):
        wins["middle vertical"] += 1
        return (gameToCheck[1] % 2) + 1
    elif ((gameToCheck[2] % 2) == (gameToCheck[5] % 2) == (gameToCheck[8] % 2) and (gameToCheck[2]) != 0 and (gameToCheck[5]) != 0 and (gameToCheck[8]) != 0):
        wins["right vertical"] += 1
        return (gameToCheck[2] % 2) + 1
    elif ((gameToCheck[0] % 2) == (gameToCheck[4] % 2) == (gameToCheck[8] % 2) and (gameToCheck[0]) != 0 and (gameToCheck[4]) != 0 and (gameToCheck[8]) != 0):
        wins["backward diagonal"] += 1
        return (gameToCheck[0] % 2) + 1
    elif ((gameToCheck[2] % 2) == (gameToCheck[4] % 2) == (gameToCheck[6] % 2) and (gameToCheck[2]) != 0 and (gameToCheck[4]) != 0 and (gameToCheck[6]) != 0):
        wins["forward diagonal"] += 1
        return (gameToCheck[2] % 2) + 1
    else: return False

def recursion(arr, n):
    if (checkWin(arr) == 2):
        allGames.append(arr)
        allWins.append(arr)
        xWins.append(arr)
    elif (checkWin(arr) == 1):
        allGames.append(arr)
        allWins.append(arr)
        oWins.append(arr)
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

def checkMovesToWin(wins):
    for game in wins:
        usedSpace = 0
        for i in range(len(game)):
            if game[i] != 0:
                usedSpace += 1
        movesToWin[usedSpace - 5] += 1
                
            

recursion([0, 0, 0, 0, 0, 0, 0, 0, 0], 0)
for game in xWins:
    checkFirstMoves(game, 1, winningFirstMoves)

for game in oWins:
    checkFirstMoves(game, 1, losingFirstMoves)

checkMovesToWin(allWins)

def printStats():
    global allGames, allWins, xWins, oWins, wins, winningFirstMoves

    print(len(allGames), "total number of games")
    print(len(allWins), "total number of winning games")
    print("", len(drawGames), "total number of drawn games")
    print(len(xWins), "total number of games won by X")
    print("", len(oWins), "total number of games won by O")
    print(winningFirstMoves)
    print(losingFirstMoves)
    print(movesToWin)

def convertGame(game):
    newGame = []
    for i in range(len(game)):
        newGame.append(game[i] % 2)
    return newGame

for i in range(len(allWins)):
    convertedWins.append(convertGame(allWins[i]))    

def checkRot(master, check):
    global ind
    child1 = [master[2], master[5], master[8], master[1], master[4], master[7], master[0], master[3], master[6]]
    child2 = [master[8], master[7], master[6], master[5], master[4], master[3], master[2], master[1], master[0]]
    child3 = [master[6], master[3], master[0], master[7], master[4], master[1], master[8], master[5], master[1]]
    
    if (check == master or check == child1 or check == child2 or check == child3):
        return True
    else:
        return False

for i in range(len(convertedWins)):
    """
        check entire array for match before any action completed
    """
    for j in range(len(convertedWins)):
        if (i != j):
            if (checkRot(convertedWins[i], convertedWins[j]) == False)
            checkRot(convertedWins[i], convertedWins[j])
            print(ind)

print(ind)

#printStats()

