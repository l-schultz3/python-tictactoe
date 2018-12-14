import itertools
games = []
finalList = []
print("running...")

print("creating permutations...")
permutations = list(itertools.permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 9))
print("done.")

def getGameArray(games):
    print("getGameArray...")
    for i in range(len(permutations)):
        games.append([[5, 0], [5, 0], [5, 0], [5, 0], [5, 0], [5, 0], [5, 0], [5, 0], [5, 0]])
        for j in range(len(permutations[i])):
            games[i][j] = [permutations[i][j] % 2, permutations[i][j]]
    print("done.")

def printGames(games):
    for i in range(len(games)):
        print(games[i])

def cleanGame(move, gameToClean):
    for i in range(9):
        if (gameToClean[i][1] > move):
            gameToClean[i] = [5, 0]

def checkWin(gameToCheck, games, index):
    numberOfWins = 0
    highestMax = 10
    if (gameToCheck[0][0] + gameToCheck[1][0] + gameToCheck[2][0]) % 3 == 0:
        if max(gameToCheck[0][1], gameToCheck[1][1], gameToCheck[2][1]) < highestMax:
            highestMax = max(gameToCheck[0][1], gameToCheck[1][1], gameToCheck[2][1])
        numberOfWins += 1
    if (gameToCheck[3][0] + gameToCheck[4][0] + gameToCheck[5][0]) % 3 == 0:
        if max(gameToCheck[3][1], gameToCheck[4][1], gameToCheck[5][1]) < highestMax:
            highestMax = max(gameToCheck[3][1], gameToCheck[4][1], gameToCheck[5][1])
        numberOfWins += 1
    if (gameToCheck[6][0] + gameToCheck[7][0] + gameToCheck[8][0]) % 3 == 0:
        if max(gameToCheck[6][1] + gameToCheck[7][1] + gameToCheck[8][1]) < highestMax:
            highestMax = max(gameToCheck[6][1] + gameToCheck[7][1] + gameToCheck[8][1])
        numberOfWins += 1
    if (gameToCheck[0][0] + gameToCheck[3][0] + gameToCheck[6][0]) % 3 == 0:
        if max(gameToCheck[0][1], gameToCheck[3][1], gameToCheck[6][1]) < highestMax:
            highestMax = max(gameToCheck[0][1], gameToCheck[3][1], gameToCheck[6][1])
        numberOfWins += 1
    if (gameToCheck[1][0] + gameToCheck[4][0] + gameToCheck[7][0]) % 3 == 0:
        if max(gameToCheck[1][1], gameToCheck[4][1], gameToCheck[7][1]) < highestMax:
            highestMax = max(gameToCheck[1][1], gameToCheck[4][1], gameToCheck[7][1])
        numberOfWins += 1
    if (gameToCheck[2][0] + gameToCheck[5][0] + gameToCheck[8][0]) % 3 == 0:
        if max(gameToCheck[2][1], gameToCheck[5][1], gameToCheck[8][1]) < highestMax:
            highestMax = max(gameToCheck[2][1], gameToCheck[5][1], gameToCheck[8][1])
        numberOfWins += 1
    if (gameToCheck[0][0] + gameToCheck[4][0] + gameToCheck[8][0]) % 3 == 0:
        if max(gameToCheck[0][1], gameToCheck[4][1], gameToCheck[8][1]) < highestMax:
            highestMax = max(gameToCheck[0][1], gameToCheck[4][1], gameToCheck[8][1])
        numberOfWins += 1
    if (gameToCheck[2][0] + gameToCheck[4][0] + gameToCheck[6][0]) % 3 == 0:
        if max(gameToCheck[2][1], gameToCheck[4][1], gameToCheck[6][1]) < highestMax:
            highestMax = max(gameToCheck[2][1], gameToCheck[4][1], gameToCheck[6][1])
        numberOfWins += 1

    if (numberOfWins > 1):
        #games.pop(index)
        cleanGame(highestMax, gameToCheck)
        games[index] = gameToCheck

        """for x in range(len(games)):
            if games[x] == gameToCheck:
                games.pop(index)
                #print(len(games))"""

    if (numberOfWins == 0):
        games.pop(index)

def filterGames(games):
    print("filtering games...")
    for i in range(len(games)):
        try:
            checkWin(games[i], games, i)
        except:
            pass
    print("done...")

def remove(duplicate):
    print("removing duplicates...")
    global finalList
    for num in duplicate: 
        if num not in finalList:
            finalList.append(num)
            if (len(finalList) % 50000 == 0): print(len(finalList))
    print("done...")

getGameArray(games)
print(len(games))
filterGames(games)
print(len(games))
remove(games)
print(len(finalList))
#printGames(games)

print("completed...")
