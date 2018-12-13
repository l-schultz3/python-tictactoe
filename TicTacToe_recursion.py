allGames = []
allWins = []
xWins = []
oWins = []

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

def checkFirstMoves(arr):
    for i in range(len(arr)):
        if (arr[i] == 1):
            winningFirstMoves[i] += 1

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
            

recursion([0, 0, 0, 0, 0, 0, 0, 0, 0], 0)
for game in xWins:
    checkFirstMoves(game)

print(len(allGames))
print(len(allWins))
print(winningFirstMoves)
print(wins)

"""for game in allGames:
    print(game)"""

