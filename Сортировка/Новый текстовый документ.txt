n = int(input())
a = map(int, input().split(maxsplit = n))
a = sorted(a)
print(*a, sep=" ")