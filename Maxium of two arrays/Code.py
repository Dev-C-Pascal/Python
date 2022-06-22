a = [1, 2, 3, 1, 2, 3, 1, 2, 3, ]
b = [3, 2, 5, 2, 1, 0, 3, 5, 3, ]
print([max(a[i], b[i]) for i in range(len(a))])