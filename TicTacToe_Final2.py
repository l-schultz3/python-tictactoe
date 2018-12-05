print("running...")

allGames = []
winningGames = []
winningFirstMoves = [0] * 9

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

def checkFirstMove():
    print("checking winning first moves...")
    global winningGames
    global winningFirstMoves
    for game in winningGames:
        print(game)
        for move in range(len(game)):
            if (game[move][1] == 1):
                print(move)
                winningFirstMoves[move] += 1
                

#Will my code ever work? ~ Luke
def checkWin(gameToCheck):
    if (gameToCheck[0][0] == gameToCheck[1][0] == gameToCheck[2][0] and gameToCheck[0][0] != 10):
        wins["top horizontal"] += 1
        return "top horizontal"
    elif (gameToCheck[3][0] == gameToCheck[4][0] == gameToCheck[5][0] and gameToCheck[3][0] != 10):
        wins["middle horizontal"] += 1
        return "middle horizontal"
    elif (gameToCheck[6][0] == gameToCheck[7][0] == gameToCheck[8][0] and gameToCheck[6][0] != 10):
        wins["bottom horizontal"] += 1
        return "bottom horizontal"
    elif (gameToCheck[0][0] == gameToCheck[3][0] == gameToCheck[6][0] and gameToCheck[0][0] != 10):
        wins["left vertical"] += 1
        return "left vertical"
    elif (gameToCheck[1][0] == gameToCheck[4][0] == gameToCheck[7][0] and gameToCheck[1][0] != 10):
        wins["middle vertical"] += 1
        return "middle vertical"
    elif (gameToCheck[2][0] == gameToCheck[5][0] == gameToCheck[8][0] and gameToCheck[2][0] != 10):
        wins["right vertical"] += 1
        return "right vertical"
    elif (gameToCheck[0][0] == gameToCheck[4][0] == gameToCheck[8][0] and gameToCheck[0][0] != 10):
        wins["backward diagonal"] += 1
        return "backward diagonal"
    elif (gameToCheck[2][0] == gameToCheck[4][0] == gameToCheck[6][0] and gameToCheck[2][0] != 10):
        wins["forward diagonal"] += 1
        return "forward diagonal"
    else: return False

def cleanGame(gameToClean, moveNumber):
    for j in range(9):
        if (gameToClean[j][1] >= moveNumber):
            gameToClean[j] = [10, 0]

def generateGames():
    global allGames
    global winningGames
    games = [[[10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0]]]

    for a in range(9):
        if (a == 0):
            print("generating games.", end="")
        elif (a == 8):
            print(".")
        else:
            print(".", end="")
        cleanGame(games[len(games) - 1], 1)
        games[len(games) - 1][a] = [1, 1]
        for b in range(9):
            cleanGame(games[len(games) - 1], 2)
            if (games[len(games) - 1][b] == [10, 0]):
                games[len(games) - 1][b] = [0, 2]
                for c in range(9):
                    cleanGame(games[len(games) - 1], 3)
                    if (games[len(games) - 1][c] == [10, 0]):
                        games[len(games) - 1][c] = [1, 3]
                        for d in range(9):
                            cleanGame(games[len(games) - 1], 4)
                            if (games[len(games) - 1][d] == [10, 0]):
                                games[len(games) - 1][d] = [0, 4]
                                for e in range(9):
                                    cleanGame(games[len(games) - 1], 5)
                                    if (games[len(games) - 1][e] == [10, 0]):
                                        games[len(games) - 1][e] = [1, 5]
                                        if (checkWin(games[len(games) - 1]) != False):
                                            games.append([[10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0]])
                                        else:
                                            for f in range(9):
                                                cleanGame(games[len(games) - 1], 6)
                                                if (games[len(games) - 1][f] == [10, 0]):
                                                    games[len(games) - 1][f] = [0, 6]
                                                    if (checkWin(games[len(games) - 1]) != False):
                                                        games.append([[10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0]])
                                                    else:
                                                        for g in range(9):
                                                            cleanGame(games[len(games) - 1], 7)
                                                            if (games[len(games) - 1][g] == [10, 0]):
                                                                games[len(games) - 1][g] = [1, 7]
                                                                if (checkWin(games[len(games) - 1]) != False):
                                                                    games.append([[10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0]])
                                                                else:
                                                                    for h in range(9):
                                                                        cleanGame(games[len(games) - 1], 8)
                                                                        if (games[len(games) - 1][h] == [10, 0]):
                                                                            games[len(games) - 1][h] = [0, 8]
                                                                            if (checkWin(games[len(games) - 1]) != False):
                                                                                games.append([[10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0]])
                                                                            else:
                                                                                for i in range(9):
                                                                                    cleanGame(games[len(games) - 1], 9)
                                                                                    if (games[len(games) - 1][i] == [10, 0]):
                                                                                        games[len(games) - 1][i] = [1, 9]
                                                                                        if (checkWin(games[len(games) - 1]) != False):
                                                                                            games.append([[10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0], [10, 0]])
def checkArray(array):
    for i in range(len(array)):
        if (array[i] != array[1]):
            print(array[i])
    print("checked")

generateGames()

print("Number of Possible Games:", len(allGames))
print("Number of Winning  Games:", len(winningGames), "\n")

checkArray(winningGames)

"""for game in range(len(winningGames)):
    print(str(winningGames[game]))

for win in wins:
    print(win, wins[win])"""

print("\n")
checkFirstMove()

print(winningFirstMoves)


print("completed...")
