allGames = []
allWins = []
drawGames = []

def checkWin(gameToCheck):
    if ((gameToCheck[0] % 2) == (gameToCheck[1] % 2) == (gameToCheck[2] % 2) and (gameToCheck[0]) != 0 and (gameToCheck[1]) != 0 and (gameToCheck[2]) != 0):
        return True
    elif ((gameToCheck[3] % 2) == (gameToCheck[4] % 2) == (gameToCheck[5] % 2) and (gameToCheck[3]) != 0 and (gameToCheck[4]) != 0 and (gameToCheck[5]) != 0):
        return True
    elif ((gameToCheck[6] % 2) == (gameToCheck[7] % 2) == (gameToCheck[8] % 2) and (gameToCheck[6]) != 0 and (gameToCheck[7]) != 0 and (gameToCheck[8]) != 0):
        return True
    elif ((gameToCheck[0] % 2) == (gameToCheck[3] % 2) == (gameToCheck[6] % 2) and (gameToCheck[0]) != 0 and (gameToCheck[3]) != 0 and (gameToCheck[6]) != 0):
        return True
    elif ((gameToCheck[1] % 2) == (gameToCheck[4] % 2) == (gameToCheck[7] % 2) and (gameToCheck[1]) != 0 and (gameToCheck[4]) != 0 and (gameToCheck[7]) != 0):
        return True
    elif ((gameToCheck[2] % 2) == (gameToCheck[5] % 2) == (gameToCheck[8] % 2) and (gameToCheck[2]) != 0 and (gameToCheck[5]) != 0 and (gameToCheck[8]) != 0):
        return True
    elif ((gameToCheck[0] % 2) == (gameToCheck[4] % 2) == (gameToCheck[8] % 2) and (gameToCheck[0]) != 0 and (gameToCheck[4]) != 0 and (gameToCheck[8]) != 0):
        return True
    elif ((gameToCheck[2] % 2) == (gameToCheck[4] % 2) == (gameToCheck[6] % 2) and (gameToCheck[2]) != 0 and (gameToCheck[4]) != 0 and (gameToCheck[6]) != 0):
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

def checkThroughWin(firstGame, secondGame, thirdGame):
    for index in range(9):
        if (firstGame[index] % 2 == secondGame[index] % 2 == thirdGame[index] % 2 and firstGame[index] != 0 and secondGame[index] != 0 and thirdGame[index] != 0):
            return True
            break
    return False

def checkAngledWin(firstGame, secondGame, thirdGame):
    if (firstGame[0] % 2 == secondGame[1] % 2 == thirdGame[2] % 2 and firstGame[0] != 0 and secondGame[1] != 0 and thirdGame[2] != 0):
        return True
    elif (firstGame[0] % 2 == secondGame[4] % 2 == thirdGame[8] % 2 and firstGame[0] != 0 and secondGame[4] != 0 and thirdGame[8] != 0):
        return True
    elif (firstGame[0] % 2 == secondGame[3] % 2 == thirdGame[6] % 2 and firstGame[0] != 0 and secondGame[3] != 0 and thirdGame[6] != 0):
        return True
    elif (firstGame[1] % 2 == secondGame[4] % 2 == thirdGame[7] % 2 and firstGame[1] != 0 and secondGame[4] != 0 and thirdGame[7] != 0):
        return True
    elif (firstGame[2] % 2 == secondGame[1] % 2 == thirdGame[0] % 2 and firstGame[2] != 0 and secondGame[1] != 0 and thirdGame[0] != 0):
        return True
    elif (firstGame[2] % 2 == secondGame[4] % 2 == thirdGame[6] % 2 and firstGame[2] != 0 and secondGame[4] != 0 and thirdGame[6] != 0):
        return True
    elif (firstGame[2] % 2 == secondGame[5] % 2 == thirdGame[8] % 2 and firstGame[2] != 0 and secondGame[5] != 0 and thirdGame[8] != 0):
        return True
    elif (firstGame[3] % 2 == secondGame[4] % 2 == thirdGame[5] % 2 and firstGame[3] != 0 and secondGame[4] != 0 and thirdGame[5] != 0):
        return True
    elif (firstGame[5] % 2 == secondGame[4] % 2 == thirdGame[3] % 2 and firstGame[5] != 0 and secondGame[4] != 0 and thirdGame[3] != 0):
        return True
    elif (firstGame[6] % 2 == secondGame[3] % 2 == thirdGame[0] % 2 and firstGame[6] != 0 and secondGame[3] != 0 and thirdGame[0] != 0):
        return True
    elif (firstGame[6] % 2 == secondGame[4] % 2 == thirdGame[2] % 2 and firstGame[6] != 0 and secondGame[4] != 0 and thirdGame[2] != 0):
        return True
    elif (firstGame[6] % 2 == secondGame[7] % 2 == thirdGame[8] % 2 and firstGame[6] != 0 and secondGame[7] != 0 and thirdGame[8] != 0):
        return True
    elif (firstGame[7] % 2 == secondGame[4] % 2 == thirdGame[2] % 2 and firstGame[7] != 0 and secondGame[4] != 0 and thirdGame[2] != 0):
        return True
    elif (firstGame[8] % 2 == secondGame[7] % 2 == thirdGame[6] % 2 and firstGame[8] != 0 and secondGame[7] != 0 and thirdGame[6] != 0):
        return True
    elif (firstGame[8] % 2 == secondGame[4] % 2 == thirdGame[0] % 2 and firstGame[8] != 0 and secondGame[4] != 0 and thirdGame[0] != 0):
        return True
    elif (firstGame[8] % 2 == secondGame[5] % 2 == thirdGame[2] % 2 and firstGame[8] != 0 and secondGame[5] != 0 and thirdGame[2] != 0):
        return True

print(len(drawGames))

def checkForDraw():
    global drawGames

    for a in range(len(drawGames)):
        for b in range(len(drawGames)):
            print(b)
            for c in range(len(drawGames)):
                if (not(checkThroughWin(drawGames[a], drawGames[b], drawGames[c]) or checkAngledWin(drawGames[a], drawGames[b], drawGames[c]))):
                    print(str(a, b, c))

checkForDraw()
