""" 01 Звёздочки вместо чисел

Напишите программу, которая заменяет все цифры в строке на звёздочки *.

text = "My number is 123-456-789"
Пример вывода:
Строка: My number is 123-456-789
Результат: My number is ***-***-***
"""


text = "My number is 123-456-789"
print("Строка:", text)

res = ""

for char in text:
    if char.isdigit():
        res += char.replace(char, "*")
    else:
        res += char
print("Результат:", res)