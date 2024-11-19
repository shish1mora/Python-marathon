#3.1
num1 = float(input("Введите первое число: "))
operation = input("Введите операцию (+, -, *, /, mod, pow, div): ")
num2 = float(input("Введите второе число: "))
    
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    result = num1 / num2      
elif operation == 'mod':
    result = num1 % num2     
elif operation == 'pow':
    result = num1 ** num2
elif operation == 'div':
    result = num1 // num2
else:
    print("Неверная операция!")

print(f'Результат: {result}')


#3.2
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
if a % b == 0:
    print("а делится на b без остатка")
elif b % a == 0:
    print("b делится на a без остатка")
else:
    print("Оба числа не делятся без остатка")

#3.3
a = (input("Введи трёхзначное число: "))

if a[0] == a[1] or a[0] == a[2] or a[1] == a[2]:
    print("Есть одинаковые цифры")
else:
    print("Нет одинаковых цифр")

