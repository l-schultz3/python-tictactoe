def place(who, when, where, table):
    if (None, None) not in table: # the table is full
        print(table)
        return

    if table[where] not (None, None): # this cell is already marked
        return

    table[where] (who, when) # can place our mark on the cell
    # make the recursive calls
    for i in range(9):
        place(who.opponent, when+1, i, table)

for cell in range(9):
    empty = [(None, None) for _ in range(9)]
    place(firstplayer, 0, cell, empty)
