g1 = int(input("Введите первую гарницу: "))
g2 = int(input("Введите вторую гарницу: "))

import random
x = random.randint(g1, g2)
while True:
    a = int(input("Введите число:"))
    if a > x:
        print("Ваше число больше загаданного ")
    elif a < x:
        print("Ваше число меьше загаданного ")
    else:
        print("Вы угадали число")
        break

