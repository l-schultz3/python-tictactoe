import random
import TicTacToe_CheckWin as check
import datetime

allWinningGames = []
foundAMatch = False
numberOfAttempts = 0

def generateGame():
    currentGameMatches = False
    currentGame = [5, 5, 5, 5, 5, 5, 5, 5, 5]
    gameWon = False
    numberOfMoves = 1 #starts at one for easy placement starting with x

    for z in range(1):
        for a in range(9):
            currentGame = [5, 5, 5, 5, 5, 5, 5, 5, 5]
            currentGame[a] = 1
            for b in range(9):
                if (currentGame[b] == 5):
                    currentGame[b] = 0
                    for c in range(9):
                        if (currentGame[c] == 5):
                            currentGame[c] = 1
                            for d in range(9):
                                if (currentGame[d] == 5):
                                    currentGame[d] = 0
                                    for e in range(9):
                                        if (currentGame[e] == 5):
                                            currentGame[e] = 1
                                            for f in range(9):
                                                if (currentGame[f] == 5):
                                                    currentGame[f] = 0
                                                    for g in range(9):
                                                        if (currentGame[g] == 5):
                                                            currentGame[g] = 1
                                                            for h in range(9):
                                                                if (currentGame[h] == 5):
                                                                    currentGame[h] = 0
                                                                    for i in range(9):
                                                                        if (currentGame[i] == 5):
                                                                            currentGame[i] = 1
                                                                            print(currentGame)
        print(currentGame)

        if (check.runCheckWin(currentGame) == "X" or check.runCheckWin(currentGame) == "O"):
            gameWon = True

        if (numberOfMoves == 9):
            break

    if (gameWon):
        """print(currentGame[0], currentGame[1], currentGame[2])
        print(currentGame[3], currentGame[4], currentGame[5])
        print(currentGame[6], currentGame[7], currentGame[8])
        print("\n")"""

        for i in range(len(allWinningGames)):
            if (currentGame == allWinningGames[i]):
                return(True)

        if (currentGameMatches == False):
            allWinningGames.append(currentGame)
            
    else:
        pass
        #print("No winner\n")

while (numberOfAttempts < 1):
    if (generateGame()):
        foundAMatch = True
    numberOfAttempts += 1
    #print("NumberOfAttempts: ", numberOfAttempts)
    #print("Found A Match: ", foundAMatch)

winFile = open("winFile.txt", "w")
winFile.write(str(datetime.datetime.now()))

for i in range(len(allWinningGames)):
    winFile.write("\n")
    for j in range(len(allWinningGames[i])):
        winFile.write(str(allWinningGames[i][j]))
    
print(allWinningGames)

winFile.close()
    
