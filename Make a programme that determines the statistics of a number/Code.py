from collections import Counter
 
n = input()
s = Counter(n)
print(''.join([str(s.get(str(i), 0)) for i in range(10)])