print("running...")

totalArr=[]
netArr=[]

def cleanGame(move, gameToClean):
    for i in range(9):
        if (gameToClean[i][1] > move):
            gameToClean[i] = [5, 0]

def checkWin(gameToCheck, lastMove, value):
    global totalArr
    numberOfWins = 0
    highestMax = 10
    if (gameToCheck[0][0] + gameToCheck[1][0] + gameToCheck[2][0]) == value:
        if max(gameToCheck[0][1], gameToCheck[1][1], gameToCheck[2][1]) < highestMax:
            highestMax = max(gameToCheck[0][1], gameToCheck[1][1], gameToCheck[2][1])
        numberOfWins += 1
    if (gameToCheck[3][0] + gameToCheck[4][0] + gameToCheck[5][0]) == value:
        if max(gameToCheck[3][1], gameToCheck[4][1], gameToCheck[5][1]) < highestMax:
            highestMax = max(gameToCheck[3][1], gameToCheck[4][1], gameToCheck[5][1])
        numberOfWins += 1
    if (gameToCheck[6][0] + gameToCheck[7][0] + gameToCheck[8][0]) == value:
        if max(gameToCheck[6][1], gameToCheck[7][1], gameToCheck[8][1]) < highestMax:
            highestMax = max(gameToCheck[6][1], gameToCheck[7][1], gameToCheck[8][1])
        numberOfWins += 1
    if (gameToCheck[0][0] + gameToCheck[3][0] + gameToCheck[6][0]) == value:
        if max(gameToCheck[0][1], gameToCheck[3][1], gameToCheck[6][1]) < highestMax:
            highestMax = max(gameToCheck[0][1], gameToCheck[3][1], gameToCheck[6][1])
        numberOfWins += 1
    if (gameToCheck[1][0] + gameToCheck[4][0] + gameToCheck[7][0]) == value:
        if max(gameToCheck[1][1], gameToCheck[4][1], gameToCheck[7][1]) < highestMax:
            highestMax = max(gameToCheck[1][1], gameToCheck[4][1], gameToCheck[7][1])
        numberOfWins += 1
    if (gameToCheck[2][0] + gameToCheck[5][0] + gameToCheck[8][0]) == value:
        if max(gameToCheck[2][1], gameToCheck[5][1], gameToCheck[8][1]) < highestMax:
            highestMax = max(gameToCheck[2][1], gameToCheck[5][1], gameToCheck[8][1])
        numberOfWins += 1
    if (gameToCheck[0][0] + gameToCheck[4][0] + gameToCheck[8][0]) == value:
        if max(gameToCheck[0][1], gameToCheck[4][1], gameToCheck[8][1]) < highestMax:
            highestMax = max(gameToCheck[0][1], gameToCheck[4][1], gameToCheck[8][1])
        numberOfWins += 1
    if (gameToCheck[2][0] + gameToCheck[4][0] + gameToCheck[6][0]) == value:
        if max(gameToCheck[2][1], gameToCheck[4][1], gameToCheck[6][1]) < highestMax:
            highestMax = max(gameToCheck[2][1], gameToCheck[4][1], gameToCheck[6][1])
        numberOfWins += 1

    if (highestMax == lastMove and numberOfWins == 1):
        totalArr.append(gameToCheck)
        
def permute(lst, n, lastMove, value):
    ''' O(n!), optimal'''
    if n==1:
        checkWin(lst, lastMove, value)
    else:
        for i in range(n):
            lst[i],lst[n-1] = lst[n-1],lst[i]
            permute(lst,n-1, lastMove, value)
            lst[i],lst[n-1] = lst[n-1],lst[i]

permute([[1, 1], [0, 2], [1, 3], [0, 4], [1, 5], [5, 0], [5, 0], [5, 0], [5, 0]], 9, 5, 3)
permute([[1, 1], [0, 2], [1, 3], [0, 4], [1, 5], [0, 6], [5, 0], [5, 0], [5, 0]], 9, 6, 0)
permute([[1, 1], [0, 2], [1, 3], [0, 4], [1, 5], [0, 6], [1, 7], [5, 0], [5, 0]], 9, 7, 3)
permute([[1, 1], [0, 2], [1, 3], [0, 4], [1, 5], [0, 6], [1, 7], [0, 8], [5, 0]], 9, 8, 0)
permute([[1, 1], [0, 2], [1, 3], [0, 4], [1, 5], [0, 6], [1, 7], [0, 8], [1, 9]], 9, 9, 3)

def removeDuplicates():
    global netArr
    global totalArr
    for i in range(len(totalArr)):
        if (i == 0):
            netArr.append(totalArr[i])
        else:
            matched = False
            for j in range(len(netArr)):
                if totalArr[i] == netArr[j]:
                    matched = True
            if (matched == False):
                netArr.append(totalArr[i])
                if i % 10000 == 0:
                    print(i)

print(len(totalArr))

removeDuplicates()

print(len(totalArr))

print("completed...")
