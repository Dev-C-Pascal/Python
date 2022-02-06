m =  int(input())
max_sq = int(m ** 0.5)
while max_sq >= 1:
     if m % (max_sq ** 2) == 0:
         print(max_sq ** 2)
         break
     max_sq -= 1