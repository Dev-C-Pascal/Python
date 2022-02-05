k = int(input())
p = int(input())
s = int(input())

s *= 100
k = k * (100 + p)
count = s // k
print(count)