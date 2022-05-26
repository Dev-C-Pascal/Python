from math import sin, cos
def func(n):
    res = 0
    for k in range(1, n):
        res += sin((k ** 2) / n) * cos((n ** 2) / (k ** (n - k)))
    return res
print(func(11))
def funcr(k, n):
    if k == n:
        return 0
    else:
        return funcr(k+1, n) + sin((k ** 2) / n) * cos((n ** 2) / (k ** (n - k)))
print(funcr(1, 11))
