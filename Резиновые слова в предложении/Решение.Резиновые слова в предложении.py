a = input()
m = a.split()
d = max([len(i) for i in m])
res = [[' '] * ((d + 1) // 2) for i in range(len(a))]
c = 0
for i in m:
    if len(i) % 2 == 0:
        for x in range(len(i) // 2):
            res[c][x] = i[x]
            c += 1
            c1 = x + 1
        for x in range(len(i) // 2 - 1, -1, -1):
            res[c][x] = i[c1]
            c1 += 1
            c += 1
    else:
        for x in range(len(i) // 2 + 1):
            res[c][x] = i[x]
            c += 1
            c1 = x + 1
        for x in range(len(i) // 2 - 1, -1, -1):
            res[c][x] = i[c1]
            c1 += 1
            c += 1
    c += 1
for _ in range(len(res[0]) - 1, -1, -1):
    [print(h[_], end='') for h in res]
    print('')
