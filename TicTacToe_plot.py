from matplotlib import pyplot as plt
import numpy as np

allGames = []
allWins = []
drawGames = []
xWins = []
oWins = []

movesToWin = [0] * 5

wins = {
        "top horizontal": 0,
        "middle horizontal": 0,
        "bottom horizontal": 0,
        "left vertical": 0,
        "middle vertical": 0,
        "right vertical": 0,
        "backward diagonal": 0,
        "forward diagonal": 0,
        "cross": 0,
        "tee": 0,
        "arrow": 0
    }

winningFirstMoves = [0] * 9
losingFirstMoves = [0] * 9

def checkFirstMoves(arr, index, arrayToWrite):
    for i in range(len(arr)):
        if (arr[i] == index):
            arrayToWrite[i] += 1

def checkWin(gameToCheck):
    if ((gameToCheck[0] % 2) == (gameToCheck[2] % 2) == (gameToCheck[4] % 2) == (gameToCheck[6] % 2) == (gameToCheck[8] % 2) and (gameToCheck[0]) != 0 and (gameToCheck[2]) != 0 and (gameToCheck[4]) != 0 and (gameToCheck[6]) != 0 and (gameToCheck[8]) != 0):
        wins["cross"] += 1
        return (gameToCheck[0] % 2) + 1
    elif ((gameToCheck[1] % 2) == (gameToCheck[3] % 2) == (gameToCheck[4] % 2) == (gameToCheck[5] % 2) == (gameToCheck[7] % 2) and (gameToCheck[1]) != 0 and (gameToCheck[3]) != 0 and (gameToCheck[4]) != 0 and (gameToCheck[5]) != 0 and (gameToCheck[7]) != 0):
        wins["cross"] += 1
        return (gameToCheck[0] % 2) + 1
    elif ((gameToCheck[0] % 2) == (gameToCheck[1] % 2) == (gameToCheck[2] % 2) == (gameToCheck[4] % 2) == (gameToCheck[7] % 2) and (gameToCheck[0]) != 0 and (gameToCheck[1]) != 0 and (gameToCheck[2]) != 0 and (gameToCheck[4]) != 0 and (gameToCheck[7]) != 0):
        wins["tee"] += 1
        return (gameToCheck[0] % 2) + 1
    elif ((gameToCheck[1] % 2) == (gameToCheck[4] % 2) == (gameToCheck[6] % 2) == (gameToCheck[7] % 2) == (gameToCheck[8] % 2) and (gameToCheck[1]) != 0 and (gameToCheck[4]) != 0 and (gameToCheck[6]) != 0 and (gameToCheck[7]) != 0 and (gameToCheck[8]) != 0):
        wins["tee"] += 1
        return (gameToCheck[1] % 2) + 1
    elif ((gameToCheck[0] % 2) == (gameToCheck[3] % 2) == (gameToCheck[6] % 2) == (gameToCheck[4] % 2) == (gameToCheck[5] % 2) and (gameToCheck[0]) != 0 and (gameToCheck[3]) != 0 and (gameToCheck[6]) != 0 and (gameToCheck[4]) != 0 and (gameToCheck[5]) != 0):
        wins["tee"] += 1
        return (gameToCheck[0] % 2) + 1
    elif ((gameToCheck[2] % 2) == (gameToCheck[5] % 2) == (gameToCheck[8] % 2) == (gameToCheck[4] % 2) == (gameToCheck[3] % 2) and (gameToCheck[2]) != 0 and (gameToCheck[5]) != 0 and (gameToCheck[8]) != 0 and (gameToCheck[4]) != 0 and (gameToCheck[3]) != 0):
        wins["tee"] += 1
        return (gameToCheck[2] % 2) + 1
    elif ((gameToCheck[0] % 2) == (gameToCheck[1] % 2) == (gameToCheck[2] % 2) == (gameToCheck[4] % 2) == (gameToCheck[6] % 2) and (gameToCheck[0]) != 0 and (gameToCheck[1]) != 0 and (gameToCheck[2]) != 0 and (gameToCheck[4]) != 0 and (gameToCheck[6]) != 0):
        wins["arrow"] += 1
        return (gameToCheck[0] % 2) + 1
    elif ((gameToCheck[0] % 2) == (gameToCheck[1] % 2) == (gameToCheck[2] % 2) == (gameToCheck[4] % 2) == (gameToCheck[8] % 2) and (gameToCheck[0]) != 0 and (gameToCheck[1]) != 0 and (gameToCheck[2]) != 0 and (gameToCheck[4]) != 0 and (gameToCheck[8]) != 0):
        wins["arrow"] += 1
        return (gameToCheck[0] % 2) + 1
    elif ((gameToCheck[0] % 2) == (gameToCheck[4] % 2) == (gameToCheck[6] % 2) == (gameToCheck[7] % 2) == (gameToCheck[8] % 2) and (gameToCheck[0]) != 0 and (gameToCheck[4]) != 0 and (gameToCheck[6]) != 0 and (gameToCheck[7]) != 0 and (gameToCheck[8]) != 0):
        wins["arrow"] += 1
        return (gameToCheck[0] % 2) + 1
    elif ((gameToCheck[2] % 2) == (gameToCheck[4] % 2) == (gameToCheck[6] % 2) == (gameToCheck[7] % 2) == (gameToCheck[8] % 2) and (gameToCheck[2]) != 0 and (gameToCheck[4]) != 0 and (gameToCheck[6]) != 0 and (gameToCheck[7]) != 0 and (gameToCheck[8]) != 0):
        wins["arrow"] += 1
        return (gameToCheck[2] % 2) + 1
    elif ((gameToCheck[0] % 2) == (gameToCheck[1] % 2) == (gameToCheck[2] % 2) and (gameToCheck[0]) != 0 and (gameToCheck[1]) != 0 and (gameToCheck[2]) != 0):
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
    elif ((gameToCheck[2] % 2) == (gameToCheck[4] % 2) == (gameToCheck[6] % 2) and (gameToCheck[2]) != 0 and (gameToCheck[4]) != 0 and (gameToCheck[6]) != 0):
        wins["forward diagonal"] += 1
        return (gameToCheck[2] % 2) + 1
    elif ((gameToCheck[0] % 2) == (gameToCheck[4] % 2) == (gameToCheck[8] % 2) and (gameToCheck[0]) != 0 and (gameToCheck[4]) != 0 and (gameToCheck[8]) != 0):
        wins["backward diagonal"] += 1
        return (gameToCheck[0] % 2) + 1
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
    print(wins)

printStats()

def winsVsMoves():
    plt.bar([5, 6, 7, 8, 9], movesToWin)
    
    plt.yticks(np.arange(0, len(allWins) + 1, step=len(allWins)/8))
    plt.title('Wins vs Moves')
    plt.ylabel('Amount of Wins')
    plt.xlabel('Number of Moves')
    
    plt.show()

def winsVsMovesSummative():
    summativeMovesToWin = movesToWin.copy()
    
    for i in range(len(summativeMovesToWin)):
        if i > 0:
            summativeMovesToWin[i] += summativeMovesToWin[i - 1]
    
    plt.bar([5, 6, 7, 8, 9], summativeMovesToWin)
    
    plt.yticks(np.arange(0, len(allWins) + 1, step=len(allWins)/8))
    plt.title('Wins vs Moves Summative')
    plt.ylabel('Amount of Wins')
    plt.xlabel('Number of Moves')
    
    plt.show()

def firstMoves():
    firstMoveNames = ["corner", "edge", "center"]
    firstMoveValues = [winningFirstMoves[0], winningFirstMoves[1], winningFirstMoves[4]]
    
    plt.bar(firstMoveNames, firstMoveValues)
    plt.title("Number of X Wins based on First Move")
    plt.show()
    
def totalVsSpecific():
    p1 = plt.bar(1, len(allGames))
    p2 = plt.bar(2, len(allWins))
    p3 = plt.bar(2, len(drawGames), bottom=len(allWins))

    plt.title('Number of Games')
    plt.xticks([])
    plt.legend((p1[0], p2[0], p3[0]), ("Total Games", "Winning Games", "Drawn Games"))
    
    plt.show()
    
def waysOfWinning():
    winningValues = [wins["top horizontal"], wins["left vertical"], wins["forward diagonal"], wins["cross"], wins["tee"], wins["arrow"]]
    winningNames = ["horizontal", "vertical", "diagonal", "cross", "tee", "arrow"]
    
    plt.bar(winningNames, winningValues, 0.7)
    
    plt.title('Wins')
    plt.ylabel('Number of Wins')
    
    plt.show()

winsVsMoves()
winsVsMovesSummative()
firstMoves()
totalVsSpecific()
waysOfWinning()