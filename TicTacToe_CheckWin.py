currentGame = [1, 1, 1, 1, 0, 0, 0, 1, 0] #x
numberOfMoves = 9

for i in range(len(currentGame)):
    if currentGame[i] == 2:
        numberOfMoves-=1
        
print(numberOfMoves)

def checkWin(value, playerToWin):
    if (currentGame[0] + currentGame[1] + currentGame[2] == value):
        print(playerToWin)
    elif (currentGame[3] + currentGame[4] + currentGame[5] == value):
        print(playerToWin)
    elif (currentGame[6] + currentGame[7] + currentGame[8] == value):
        print(playerToWin)
    elif (currentGame[0] + currentGame[3] + currentGame[6] == value):
        print(playerToWin)
    elif (currentGame[1] + currentGame[4] + currentGame[7] == value):
        print(playerToWin)
    elif (currentGame[2] + currentGame[5] + currentGame[8] == value):
        print(playerToWin)
    elif (currentGame[0] + currentGame[4] + currentGame[8] == value):
        print(playerToWin)
    elif (currentGame[2] + currentGame[4] + currentGame[6] == value):
        print(playerToWin)

if numberOfMoves % 2 == 1:
    checkWin(3, "X")
else:
    checkWin(0, "O")

