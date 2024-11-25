#3.1
def can_buy_exactly_k_balls(k):
    while k >= 0:
        if k % 3 == 0:
            return True
        k -= 5
    return False

k = int(input("Введите количество шариков мороженого: "))
if can_buy_exactly_k_balls(k):
    print("Можно купить ровно", k, "шариков мороженого.")
else:
    print("Нельзя купить ровно", k, "шариков мороженого.")

#3.2
def years_to_exceed(m, k, s):
    years = 0
    current_sum = m
    while current_sum < s:
        current_sum *= (1 + k / 100)
        years += 1
    return years

m = float(input("Введите начальную сумму вклада (в тыс. руб.): "))
k = float(input("Введите годовую процентную ставку (%): "))
s = float(input("Какая сумма должна быть превышена (в тыс. руб.)? "))
years = years_to_exceed(m, k, s)
print(f"Потребуется {years} лет, чтобы сумма вклада превысила {s} тысяч рублей.")



#3.3
def sum_of_digits(n):
    digits = list(map(int, str(n)))
    return sum(digits)

number = int(input("Введите число: "))
result = sum_of_digits(number)
print(f"Сумма цифр числа {number} равна {result}")



