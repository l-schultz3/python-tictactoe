totalArr = []

def recursion(arr, n):
    if (n <= 8):        
        fillNextMove(arr, n + 1)
    else:
        #print(arr)
        totalArr.append(arr)

def fillNextMove(arr, move):
    newArrs = [[]]
    for i in range(len(arr)):
        if (arr[i] == 0):
            tempArr = arr
            tempArr[i] = move
            newArrs.append(tempArr)

    print(newArrs)
    for newArr in newArrs:
        recursion(newArr, move)
            

recursion([0, 0, 0, 0, 0, 0, 0, 0, 0], 0)

print(len(totalArr))

for game in totalArr:
    print(game)
