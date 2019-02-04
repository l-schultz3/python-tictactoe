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

def formatArray(arr):
    for i in range(len(arr)):
        arr[i] = arr[i] % 2
    return arr

def removeDuplicates(array):
    newArr = []

    for i in range(len(array)):
        tempArr = formatArray(array[i])
        matched = False
        for j in range(len(newArr)):
            try:
                if (tempArr == newArr[j]):
                    matched = True
            except:
                pass
        if matched == False:
            newArr.append(tempArr)

    return newArr

def checkThroughWin(firstGame, secondGame, thirdGame):
    for index in range(9):
        if (firstGame[index] == secondGame[index] == thirdGame[index]):
            return True
            break
    return False

def checkAngledWin(firstGame, secondGame, thirdGame):
    if (firstGame[0] == secondGame[1] == thirdGame[2]):
        return True
    elif (firstGame[0] == secondGame[4] == thirdGame[8]):
        return True
    elif (firstGame[0] == secondGame[3] == thirdGame[6]):
        return True
    elif (firstGame[1] == secondGame[4] == thirdGame[7]):
        return True
    elif (firstGame[2] == secondGame[1] == thirdGame[0]):
        return True
    elif (firstGame[2] == secondGame[4] == thirdGame[6]):
        return True
    elif (firstGame[2] == secondGame[5] == thirdGame[8]):
        return True
    elif (firstGame[3] == secondGame[4] == thirdGame[5]):
        return True
    elif (firstGame[5] == secondGame[4] == thirdGame[3]):
        return True
    elif (firstGame[6] == secondGame[3] == thirdGame[0]):
        return True
    elif (firstGame[6] == secondGame[4] == thirdGame[2]):
        return True
    elif (firstGame[6] == secondGame[7] == thirdGame[8]):
        return True
    elif (firstGame[7] == secondGame[4] == thirdGame[2]):
        return True
    elif (firstGame[8] == secondGame[7] == thirdGame[6]):
        return True
    elif (firstGame[8] == secondGame[4] == thirdGame[0]):
        return True
    elif (firstGame[8] == secondGame[5] == thirdGame[2]):
        return True

print(len(drawGames))

newDrawGames = removeDuplicates(drawGames)

print(len(newDrawGames))

for game in newDrawGames:
    print(game)

def checkForDraw():
    global newDrawGames

    for a in range(len(newDrawGames)):
        for b in range(len(newDrawGames)):
            #print(b)
            for c in range(len(newDrawGames)):
                if (not(checkThroughWin(newDrawGames[a], newDrawGames[b], newDrawGames[c]) or checkAngledWin(newDrawGames[a], newDrawGames[b], newDrawGames[c]))):
                    print(str(a, b, c))

checkForDraw()
