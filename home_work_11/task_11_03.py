""" 03 Увеличение чисел

Напишите программу, которая
- заменяет все числа в строке на их эквивалент, умноженный на 10.

text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."
Пример вывода:
I have 50.0 apples and 100.0 oranges, price is 5.0 each. Card number is ....3672.
"""


text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."
print(text)
words = text.split()

res = ""

for word in words:
    if word.isdigit():
        num = float(word) * 10
        res += str(num)
        res += " "

    elif "." in word:
        parts = word.split(".")
        if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
            num_f = float(word) * 10
            res += str(num_f) + " "
        else:
            res += word + " "
    else:
        res += word + " "

print(res)