import itertools
games = []
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

getGameArray(games)
#printGames(games)

print("completed...")
