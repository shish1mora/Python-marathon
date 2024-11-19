#1.1
a = float(input("Введите число a: "))
b = float(input("Введите число b: "))

result = a ** b

print(f"{a} в степени {b} равно {result}")


#1.2
day_number = int(input("Введите число от 1 до 7: "))

days_of_week = ["Понедельник", "Вторник", "Среда","Четверг", "Пятница", "Суббота", "Воскресенье"]

if 1 <= day_number <= 7:
    print(days_of_week[day_number - 1])
else:
    print("Неверный ввод! Число должно быть от 1 до 7.")

#1.3
a = float(input("Введите число a: "))
b = float(input("Введите число b: "))
if a > b:
    print("Первое число больше второго")
else:
    print("Второе число больше первого") 

#1.4   
a = float(input("Введите число a: "))
b = 99.99
bank = a * b
print(str(bank) + " деревянных" + " Все еще лоубанк)")