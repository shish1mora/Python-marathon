#2.1
a = float(input("Введите число: "))
if int(a) % 2 == 0:
    print("четное")
else:
    print("нечетное")


#2.2
a = float(input("Введите число: "))
b = float(input("Введите число: "))
c = float(input("Введите число: "))
if a < b and a < c:
    print(a)
elif b < a and b < c:
    print(b)
elif c < a and c < b:
    print(c)
else:
    print("Введены одинаковые числа")


#2.3
a = int(input("Введите рекомендованное количество часов сна: "))
b = int(input("Введите минимальное количество часов сна: "))
c = int(input("Сколько фактически спит Аня? "))
if c <= a and c >= b:
    print("Это нормально")
elif c < b:
    print("Недосып")
else:
    print("Передосып")