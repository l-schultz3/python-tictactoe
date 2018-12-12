def draw_board(board):
    template = ("[{}]" * 3 + "\n") * 3
    print(template.format(*board))

def has_winner(sequence):
    board = [" "] * 9
    for n, move in enumerate(sequence):
        board[move] = "X" if n % 2 == 0 else "O"
    draw_board(board)
    tests = [
        board[0] == board[1] == board[2] != " ",
        board[3] == board[4] == board[5] != " ",
        board[6] == board[7] == board[8] != " ",
        board[0] == board[3] == board[6] != " ",
        board[1] == board[4] == board[7] != " ",
        board[2] == board[5] == board[8] != " ",
        board[0] == board[4] == board[8] != " ",
        board[2] == board[4] == board[6] != " ",
    ]
    return any(tests)

def no_moves_left(sequence):
    return len(sequence) == 9

def generate_games(sequence):
    if has_winner(sequence):
        winner = 2 - len(sequence) % 2
        return [(sequence, winner)]
    if no_moves_left(sequence):
        return [(sequence, 0)]
    games = []
    open_spaces = [i for i in range(9) if i not in sequence]
    for new_move in open_spaces:
        new_sequence = sequence.copy()
        new_sequence.append(new_move)
        new_games = generate_games(new_sequence)
        games.extend(new_games)
    return games

print("running...")

games = generate_games([])

print(len(games))

print("completed...")
