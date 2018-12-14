print("running...")

def swap(arr, x, y):
    arr[x], arr[y] = arr[y], arr[x]

def runPermute(arr):
    permute(arr, 0, len(arr))

def permute(arr, i, n):
    global numberOfPermutes
    if (i == n):
        numberOfPermutes += 1
    else:
        for j in range(n):
            swap(arr, i, j)
            permute(arr, i + 1, n)
            swap(arr, i, j)

numberOfPermutes = 0

arr = [1, 0, 1, 0, 1, 0, 1, 0, 1]
runPermute(arr)

print(numberOfPermutes)
print("completed...")
