def permute(lst, n, lastMove):
    global length
    ''' O(n!), optimal'''
    if n==1:
        length += 1
    else:
        for i in range(n):
            lst[i],lst[n-1] = lst[n-1],lst[i]
            permute(lst,n-1, lastMove)
            lst[i],lst[n-1] = lst[n-1],lst[i]

length = 0
permute([[5, 0], [5, 0], [5, 0], [5, 0], [5, 0], [5, 0], [5, 0], [5, 0], [5, 0]], 9, 5)
print(length)
