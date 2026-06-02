""" 01 Простое число

Напишите функцию is_prime(), которая
- проверяет, является ли число n простым (делится только на 1 и само себя)
- и возвращает булев результат.


Пример проверки функции is_prime():

chack_func_is_prime(17)  # Число 17 является простым
chack_func_is_prime(18)  # Число 18 НЕ является простым
"""


def is_prime(n):
    if n < 2:
        return False

    for num in range(2, n):
        if n % num == 0:
            return False

    return True


def chack_func_is_prime(n):
    if is_prime(n):
        return f"Число {n} является простым"
    else:
        return f"Число {n} НЕ является простым"




print(chack_func_is_prime(52))  # Число 17 является простым
print(chack_func_is_prime(67))  # Число 18 НЕ является простым