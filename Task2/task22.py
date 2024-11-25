#2.1
A = int(input("Введите длину коробки: "))
B = int(input("Введите ширину коробки: "))
C = int(input("Введите высоту коробки: "))
M = int(input("Введите ширину дверного проема: "))
K = int(input("Введите высоту дверного проема: "))

if (A <= M and B <= K) or (B <= M and C <= K) or (C <= M and A <= K):
    print("Коробка пройдет через дверной проем.")
else:
    print("Коробка не пройдет через дверной проем.")


#2.2
height = int(input("Введите высоту треугольника: "))

for i in range(height):
    print(' ' * (height - i - 1), end="")
    print('*' * (2 * i + 1))


#2.3
n = int(input("Введите число N: "))
i = 1

while True:
    square = i**2
    if square >= n:
        break
    print(square)
    i += 1


