#array index indicates move number, not pos

import itertools
games = []
print("running...")

permutations = list(itertools.permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 9))
print(len(permutations))



print("done...")
