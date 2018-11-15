winningGames = open("winningFile.txt", "r")
gamesArray = []
for line in winningGames:
    gamesArray.append(winningGames.read().split(',\n'))
#print(winningGames.readlines())

print(gamesArray)

winningGames.close()
