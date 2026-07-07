""" 01 Генератор Фибоначчи

Создайте генератор, который
- генерирует последовательность Фибоначчи бесконечно, возвращая по одному числу за раз.

Последовательность Фибоначчи — это ряд чисел, где
каждое следующее число равно сумме двух предыдущих.

Начинается с 0 и 1.

0, 1, 1, 2, 3, 5, 8, 13, 21, 34
"""

def fibonacci():
    first_num = 0
    second_num = 1

    while True:
        yield first_num
        first_num, second_num = second_num, first_num + second_num

f = fibonacci()

result = ''
for x in range(10):
    result += f'{next(f)}, '

print(f'{result}\b\b')

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34