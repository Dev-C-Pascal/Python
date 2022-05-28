def fun(arr):
    for i, v in enumerate(zip(*arr)):
        if all(e<0 for e in v):
            return i 
    return False
 
 
a = [[1,2,-3], [4,5,-6], [7,8,-9]]
for r in a:
    print(*r)
print()
 
m, n = len(a), len(a[0])
ind = fun(a)
if ind:
    for i in range(m):
        a[i][ind], a[i][n-1] = a[i][n-1], a[i][ind]
 
for r in a:
    print(*r)
