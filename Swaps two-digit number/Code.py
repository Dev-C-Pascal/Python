def f(x):
    if 9 < x < 100:
        return x % 10 * 10 + x // 10
    return x
    
print(f(52))