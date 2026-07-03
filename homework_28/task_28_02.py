"""Объединение списков продуктов

Напишите функцию, которая принимает несколько списков с названиями продуктов и возвращает генератор,
содержащий все продукты в нижнем регистре.
Выведите содержимое генератора.

Данные:
"""
fruits = ["Apple", "Banana", "Orange"]

vegetables = ["Carrot", "Tomato", "Cucumber"]

dairy = ["Milk", "Cheese", "Yogurt"]

"""
Пример вывода:

apple

banana

orange

carrot

tomato

cucumber

milk

cheese

yogurt
"""
import itertools


def get_lowercase_products(fruits, vegetables, dairy):

    all_products = itertools.chain(fruits, vegetables, dairy)

    gen = (product.lower() for product in all_products)

    return gen




for item in get_lowercase_products(fruits, vegetables, dairy):
    print(item)
    print()