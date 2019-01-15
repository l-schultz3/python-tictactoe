import datetime

allGames = 0
allWins = 0
drawGames = 0
xWins = 0
oWins = 0

wins = {
        "2d": 0,
        "3d": 0
    }

gameFile = open("dataFile.txt", "w")
gameFile.write(str(datetime.datetime.now))

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
	
def check3dWin(gameToCheck):
	if ((gameToCheck[0] % 2) == (gameToCheck[10] % 2) == (gameToCheck[20] % 2) and (gameToCheck[0]) != 0 and (gameToCheck[10]) != 0 and (gameToCheck[20]) != 0):
        wins["3d"] += 1
        return True
	if ((gameToCheck[0] % 2) == (gameToCheck[13] % 2) == (gameToCheck[26] % 2) and (gameToCheck[0]) != 0 and (gameToCheck[13]) != 0 and (gameToCheck[26]) != 0):
        wins["3d"] += 1
        return True
	if ((gameToCheck[0] % 2) == (gameToCheck[12] % 2) == (gameToCheck[24] % 2) and (gameToCheck[0]) != 0 and (gameToCheck[12]) != 0 and (gameToCheck[24]) != 0):
        wins["3d"] += 1
        return True
	if ((gameToCheck[1] % 2) == (gameToCheck[13] % 2) == (gameToCheck[25] % 2) and (gameToCheck[1]) != 0 and (gameToCheck[13]) != 0 and (gameToCheck[25]) != 0):
        wins["3d"] += 1
        return True
	if ((gameToCheck[2] % 2) == (gameToCheck[10] % 2) == (gameToCheck[18] % 2) and (gameToCheck[2]) != 0 and (gameToCheck[10]) != 0 and (gameToCheck[18]) != 0):
        wins["3d"] += 1
        return True
	if ((gameToCheck[2] % 2) == (gameToCheck[13] % 2) == (gameToCheck[24] % 2) and (gameToCheck[2]) != 0 and (gameToCheck[13]) != 0 and (gameToCheck[24]) != 0):
        wins["3d"] += 1
        return True
	if ((gameToCheck[2] % 2) == (gameToCheck[14] % 2) == (gameToCheck[26] % 2) and (gameToCheck[2]) != 0 and (gameToCheck[14]) != 0 and (gameToCheck[26]) != 0):
        wins["3d"] += 1
        return True
	if ((gameToCheck[3] % 2) == (gameToCheck[13] % 2) == (gameToCheck[23] % 2) and (gameToCheck[3]) != 0 and (gameToCheck[13]) != 0 and (gameToCheck[23]) != 0):
        wins["3d"] += 1
        return True
	if ((gameToCheck[5] % 2) == (gameToCheck[13] % 2) == (gameToCheck[21] % 2) and (gameToCheck[5]) != 0 and (gameToCheck[13]) != 0 and (gameToCheck[21]) != 0):
        wins["3d"] += 1
        return True
	if ((gameToCheck[6] % 2) == (gameToCheck[12] % 2) == (gameToCheck[18] % 2) and (gameToCheck[6]) != 0 and (gameToCheck[12]) != 0 and (gameToCheck[18]) != 0):
        wins["3d"] += 1
        return True
	if ((gameToCheck[6] % 2) == (gameToCheck[13] % 2) == (gameToCheck[20] % 2) and (gameToCheck[6]) != 0 and (gameToCheck[13]) != 0 and (gameToCheck[20]) != 0):
        wins["3d"] += 1
        return True
	if ((gameToCheck[6] % 2) == (gameToCheck[16] % 2) == (gameToCheck[26] % 2) and (gameToCheck[6]) != 0 and (gameToCheck[16]) != 0 and (gameToCheck[26]) != 0):
        wins["3d"] += 1
        return True
	if ((gameToCheck[7] % 2) == (gameToCheck[13] % 2) == (gameToCheck[19] % 2) and (gameToCheck[7]) != 0 and (gameToCheck[13]) != 0 and (gameToCheck[19]) != 0):
        wins["3d"] += 1
        return True
	if ((gameToCheck[8] % 2) == (gameToCheck[14] % 2) == (gameToCheck[20] % 2) and (gameToCheck[8]) != 0 and (gameToCheck[14]) != 0 and (gameToCheck[20]) != 0):
        wins["3d"] += 1
        return True
	if ((gameToCheck[8] % 2) == (gameToCheck[13] % 2) == (gameToCheck[18] % 2) and (gameToCheck[8]) != 0 and (gameToCheck[13]) != 0 and (gameToCheck[18]) != 0):
        wins["3d"] += 1
        return True
	if ((gameToCheck[8] % 2) == (gameToCheck[16] % 2) == (gameToCheck[24] % 2) and (gameToCheck[8]) != 0 and (gameToCheck[16]) != 0 and (gameToCheck[24]) != 0):
        wins["3d"] += 1
        return True

def checkWin(gameToCheck):
    if (check2dWin(gameToCheck, 0) or check2dWin(gameToCheck, 1) or check2dWin(gameToCheck, 2) or checkThroughWin(gameToCheck) or check3dWin(gameToCheck)):
        return True
    else: return False

def recursion(arr, n):
    if (checkWin(arr)):
        allGames += 1
        allWins += 1
    elif (n <= 26):        
        fillNextMove(arr, n + 1)
    else:
        allGames += 1
        drawGames += 1

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

recursion([0] * 27, 0)

def printStats():
    global allGames, allWins, xWins, oWins, wins, winningFirstMoves

    print(len(allGames), "total number of games")
    print(len(allWins), "total number of winning games")
    print(len(drawGames), "total number of drawn games")

printStats()

gameFile.write(len(allGames) + "total number of games")
gameFile.write(len(allWins) + "total number of winning games")
gameFile.write(len(drawGames) + "total number of drawn games")

gameFile.write(str(datetime.datetime.now))

gameFile.close()

