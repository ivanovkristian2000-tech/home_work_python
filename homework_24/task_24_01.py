""" 01 Сумма цифр числа

Напишите рекурсивную функцию, которая находит сумму всех цифр числа.

Попробуйте решить в двух вариантах: tail и non-tail.

Данные:
num = 43197
Пример вывода:
24
"""


num = 43197



def sum_digits_tail(n):
    if n == 0:
        return 0

    last_num = n % 10
    remaining_num = n // 10

    return last_num + sum_digits_tail(remaining_num)



def sum_digits_non_tail(num, accumulator=0):
    pass


print(sum_digits_tail(43197))       # 24
print(sum_digits_non_tail(43197))   # 24