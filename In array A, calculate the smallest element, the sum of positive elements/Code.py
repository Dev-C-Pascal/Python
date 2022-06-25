from random import randint
 
 
def is_simple(num):
    if num == 2:
        return True
    if num <= 1 or not num % 2:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if not num % i:
            return False
    return True
 
 
n = int(input())
arr = [[randint(-100, 100) for _ in range(n)] for _ in range(n)]
print(*arr, sep="\n")
print(f'Минимальный: {min([min(line) for line in arr])}')
print(f'Сумма положительных: {sum(x for line in arr for x in line if x > 0)}')
print(f'Простых по диагонали: {len([arr[i][j] for i in range(n) for j in range(n) if (i==j or i==n-1-j) and is_simple(arr[i][j])])}')