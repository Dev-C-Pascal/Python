k = int(input())
m = int(input())
a = int(input())
b = int(input())
 
katya = 0
masha = 0
 
for i in range(a, b + 1):
    if i % k == 0:
        katya += 1
    if i % m == 0:
        masha += 1
print(katya - masha)