"""
Created by Luke Schultz in 2018
A program to check if a three dimensional game of tic-tac-toe can end in a draw
"""

allMoves = []
allWinningMoves = []
allDrawMoves = []

def check2DWin(movesToCheck):
    if ((movesToCheck[0] % 2) == (movesToCheck[1] % 2) == (movesToCheck[2] % 2) and (movesToCheck[0]) != 0 and (movesToCheck[1]) != 0 and (movesToCheck[2]) != 0):
        return True
    elif ((movesToCheck[3] % 2) == (movesToCheck[4] % 2) == (movesToCheck[5] % 2) and (movesToCheck[3]) != 0 and (movesToCheck[4]) != 0 and (movesToCheck[5]) != 0):
        return True
    elif ((movesToCheck[6] % 2) == (movesToCheck[7] % 2) == (movesToCheck[8] % 2) and (movesToCheck[6]) != 0 and (movesToCheck[7]) != 0 and (movesToCheck[8]) != 0):
        return True
    elif ((movesToCheck[0] % 2) == (movesToCheck[3] % 2) == (movesToCheck[6] % 2) and (movesToCheck[0]) != 0 and (movesToCheck[3]) != 0 and (movesToCheck[6]) != 0):
        return True
    elif ((movesToCheck[1] % 2) == (movesToCheck[4] % 2) == (movesToCheck[7] % 2) and (movesToCheck[1]) != 0 and (movesToCheck[4]) != 0 and (movesToCheck[7]) != 0):
        return True
    elif ((movesToCheck[2] % 2) == (movesToCheck[5] % 2) == (movesToCheck[8] % 2) and (movesToCheck[2]) != 0 and (movesToCheck[5]) != 0 and (movesToCheck[8]) != 0):
        return True
    elif ((movesToCheck[0] % 2) == (movesToCheck[4] % 2) == (movesToCheck[8] % 2) and (movesToCheck[0]) != 0 and (movesToCheck[4]) != 0 and (movesToCheck[8]) != 0):
        return True
    elif ((movesToCheck[2] % 2) == (movesToCheck[4] % 2) == (movesToCheck[6] % 2) and (movesToCheck[2]) != 0 and (movesToCheck[4]) != 0 and (movesToCheck[6]) != 0):
        return True
    else: return False
	
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

def recursion(arr, lastMove):
    if (check2DWin(arr)): #if game has been won
        allMoves.append(arr)
        allWinningMoves.append(arr)
    elif (lastMove <= len(arr) - 1): #if the game has not been filled with moves
        fillNextMove(arr, lastMove + 1)
    else: #the game has ended in a draw
        allMoves.append(arr)
        allDrawMoves.append(arr)

def fillNextMove(arr, move): #given a set of moves for a game, this gives all next possible moves
    newArrs = []
    for i in range(len(arr)):
        if (arr[i] == 0):
            tempArr = arr.copy()
            tempArr[i] = move
            newArrs.append(tempArr)

    for newArr in newArrs:
        if (newArr != []):
            recursion(newArr, move)

def formatArray(arr): #converts specific value of move order into either an X (1) or an O (2)
    for i in range(len(arr)):
        arr[i] = arr[i] % 2 + 1
    return arr

def movesToGame(array): #converts arrays made up of order of moves into arrays made up of X's and O's
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

def checkForDraw(gamesToCompare):
    #creates 3D games by combining 2D games
    #then checks 3D games to see if they end in a draw
    drawFound = False

    for a in gamesToCompare:
        for b in gamesToCompare:
            for c in gamesToCompare:
                if (not(checkThroughWin(a, b, c) or checkAngledWin(a, b, c))):
                    print("Drawn game found, with combinations:" + a, b, c)
                    drawFound = True

    if not drawFound:
        print("No drawn games found")

print("generating all 2D games...")
recursion([0] * 9, 0)

drawGames = movesToGame(allDrawMoves)

print("checking for draws in 3D games...")
checkForDraw(drawGames)
                
