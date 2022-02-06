a1, b1 = [int(i) for  i in input().split()]
a2, c2 = [int(i) for  i in input().split()]
b3, c3 = [int(i) for  i in input().split()]

A = a1 + a2 - b1 - c2
B = b1 + b3 - a1 - c3
C = c2 + c3 - a2 - b3

if a1 > b1:
    A += 300
elif a1 < b1:
    B += 300
else:
    A += 100
    B += 100

if a2 > c2:
    A += 300
elif a2 < c2:
    C += 300
else:
    A += 100
    C += 100

if b3 > c3:
    B += 300
elif b3 < c3:
    C += 300
else:
    B += 100
    C += 100

if A > B and A > C:
    print('A')
if B > A and B > C:
    print('B')
if C > A and C > B:
    print('C')
else:
    print('Draw')