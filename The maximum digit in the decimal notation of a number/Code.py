n = int(input('n = '))
ma = 0
while n>0 and ma != 9:
    if n%10>ma:
        ma = n%10
    n //= 10
print(ma)