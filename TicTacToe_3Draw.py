"""
Created by Luke Schultz in 2018

A program to check if a game of three dimensional tic-tac-toe can end in a draw

A game of three dimensional is best understood as a combination of three two dimensional games,
stacked on top of each other. With this definition, it becomes much simpler to extend work into the third dimension.
When talking about a three dimensional game, I use the terms plane index, and dimensional index.
Plane index refers to the positioning in the second dimension, running from 0 to 8, with 0 at the top left,
and 8 at the bottom right. Dimensional index refers to the position in the stack of two dimensional games,
running from 0 to 2, with 0 being the top, and 2 being the bottom.

To find out if a specific game ends in a draw, you need to rule out all the possible ways on winning.
There are three main methods of winning a game of three dimensional tic-tac-toe.
The first way is with all the winning tiles on the same plane,
which would be done in the exact same way as a two dimensional game.
The second way is with the same plane index, but a different dimensional index,
a simpler explanation of this would be three tiles stacked on top of each other,
to form three in a row. The third method of winning is a combination of the two listed prior.
Three tiles in a row, but with both a different plane index and a different dimensional index.
This is best visualized as forming the same lines as a two dimensional win, but going through all three layers.

This code works by first generating all possible combinations of moves that create a two dimensional game.
All of the combinations of moves that end in a draw are then converted into games,
meaning they are represented by “X”s and “O”s (2s and 1s respectively in the code)
instead of the orders of moves (this is important because it greatly decreased the number of comparisons made, speeding up the code).
All of those drawn games are then combined in every possible way,
and are checked for the other two methods of winning. Every game ends in a win.
"""

allMoves = []
allWinningMoves = []
allDrawMoves = []

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
        allMoves.append(arr)
        allWinningMoves.append(arr)
    elif (n <= 8):        
        fillNextMove(arr, n + 1)
    else:
        allMoves.append(arr)
        allDrawMoves.append(arr)

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

def formatArray(arr):
    for i in range(len(arr)):
        arr[i] = arr[i] % 2 + 1
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

def checkForDraw(gamesToCompare):
    drawFound = False

    for a in gamesToCompare:
        for b in gamesToCompare:
            for c in gamesToCompare:
                if (not(checkThroughWin(a, b, c) or checkAngledWin(a, b, c))):
                    print("Drawn game found, with combinations:" + a, b, c)
                    drawFound = True

    if not drawFound:
        print("No drawn games found")

recursion([0] * 9, 0)

drawGames = removeDuplicates(allDrawMoves)

checkForDraw(drawGames)
                
