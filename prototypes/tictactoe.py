nWinO, nWinX, nDraw = 0, 0, 0

allWinningGames = []

print("running...")

def recurse(board, toMove):
    global nWinO, nWinX, nDraw, allWinningGames
    def win(board, player):
        return (any(all(board[i][j] == player for j in range(3)) for i in range(3)) or
                any(all(board[i][j] == player for i in range(3)) for j in range(3)) or
                all(board[i][i] == player for i in range(3)) or
                all(board[i][2-i] == player for i in range(3)))
    def draw(board): return all(board[i][j] != '' for i in range(3) for j in range(3))
    if win(board, 'O'):
        nWinO += 1
        allWinningGames.extend(board)
    elif win(board, 'X'):
        nWinX += 1
        allWinningGames.extend(board)
    elif draw(board):
        nDraw += 1
        allWinningGames.extend(board)
    else:
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = toMove
                    recurse(board, 'X' if toMove == 'O' else 'O')
                    allWinningGames.extend(board)
                    board[i][j] = ''
recurse([['','',''],['','',''],['','','']], 'O')
print("There are %d possible games (excluding symmetry), of which O wins %d, X wins %d and %d are drawn." % (nWinO+nWinX+nDraw,nWinO,nWinX,nDraw))

for game in range(len(allWinningGames)):
    print(allWinningGames[game])

print("completed...")
