from random import randint
 
arr = [[randint(-99, 99) for _ in range(10)] for _ in range(10)]
print(*arr, sep='\n')
 
s = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if i == j or len(arr) - 1 - j:
            s += arr[i][j]
 
print(len([x for x in zip(*arr) if sum(x) > s]))