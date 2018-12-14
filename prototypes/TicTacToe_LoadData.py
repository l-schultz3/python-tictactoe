print("running...")

winningGames = open("winningFile.txt", "r")
winningList = list(winningGames)
print("done loading...")
print(len(winningList))

"""for game in winningList:
    print(game)"""

if (list(winningList[0]) == [[1, 1], [0, 2], [1, 3], [0, 4], [1, 5], [0, 6], [1, 7], [5, 0], [5, 0]]):
    print("true")

print(type(winningList[0]))


print("completed...")
