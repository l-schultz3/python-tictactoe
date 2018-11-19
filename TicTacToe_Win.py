import TicTacToe_CheckWin as check

print("running...")

allGames = []
foundAMatch = False
numberOfAttempts = 0
checkCurrentGame = [5, 5, 5, 5, 5, 5, 5, 5, 5]
onlyWinningGames = False
numberOfFirstMoves = [0, 0, 0, 0, 0, 0, 0, 0, 0]
global stepsDown
stepsDown = 0

currentGame = [[5, 0], [5, 0], [5, 0], [5, 0], [5, 0], [5, 0], [5, 0], [5, 0], [5, 0]]

def cleanGame(move):
    for j in range(9):
        if (currentGame[j][1] >= move):
            currentGame[j] = [5, 0]

def completeMove(moveNumber):
    global stepsDown
    stepsDown = stepsDown + 1
    for i in range(9):
        cleanGame(moveNumber)
        if (currentGame[i][0] == 5):
            currentGame[i][0] = i % 2
            currentGame[i][1] = moveNumber
            print(i)
            allGames.append(currentGame)
            break
    if (stepsDown < 9):
        generateGame()

def generateGame():
    for i in range(9):
        completeMove(i)
        
generateGame()

for x in range(len(allGames)):
    print(allGames[x])
