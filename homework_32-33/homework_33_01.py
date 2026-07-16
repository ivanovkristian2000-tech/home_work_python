""" 01 Среднее время выполнения

Создайте декоратор measure_time, который
- измеряет и выводит среднее время выполнения функции за 5 вызовов.

Функция может быть любой:
    например, сортировка списка, чтение из файла или расчёты.

Пример применения:
@measure_time
def compute():
    total = 0
    for i in range(10_000_000):
        total += i
    return total

Пример вывода:
Среднее время выполнения для 5 вызовов: 0.21 секунд
Результат: 49999995000000

"""

import time



def measure_time(func):

    def wrapper():
        total_time = 0
        result = None

        for _ in range(5):
            start = time.time()
            result = func()
            end = time.time()

            total_time += end - start

        avg_time = total_time / 5

        print(f"Среднее время выполнения для 5 вызовов: {round(avg_time, 2)} секунд")
        print(f"Результат: {result}")


    return wrapper




@measure_time
def compute():
    total = 0
    for i in range(10_000_000):
        total += i
    return total



compute()
