""" 02 Среднее время выполнения с количеством вызовов

Доработайте декоратор measure_time, чтобы он
- принимал параметр repeats — количество вызовов функции.

Декоратор должен
- выполнять функцию указанное число раз
- и выводить среднее время выполнения.

Пример применения:
@measure_time(10)
def compute():
    total = 0
    for i in range(10_000_000):
        total += i
    return total

Пример вывода:
Среднее время выполнения для 10 вызовов: 0.21 секунд
Результат: 49999995000000

"""
import time



def measure_time(repeats):
    def decor(func):
        def wrapper():
            total_time = 0
            result = None

            for _ in range(repeats):
                start = time.time()
                result = func()
                end = time.time()

                total_time += end - start

            avg_time = total_time / repeats

            print(f"Среднее время выполнения для {repeats} вызовов: {round(avg_time, 2)} секунд")
            print(f"Результат: {result}")

            return result

        return wrapper

    return decor





@measure_time(10)
def compute():
    total = 0
    for i in range(10_000_000):
        total += i
    return total



compute()

















# def measure_time(times=5):
#     pass
#
#
# @measure_time(10)
# def compute():
#     total = 0
#     for i in range(10_000_000):
#         total += i
#     return total
#
#
# compute()
#
# # Среднее время выполнения для 10 вызовов: 0.49 секунд
# # 49999995000000