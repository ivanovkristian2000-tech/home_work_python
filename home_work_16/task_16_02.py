""" 02 Правильные скобки

Напишите программу, которая
- принимает строку, содержащую любые виды скобок
    — круглые (),
    — квадратные []
    — и фигурные {}.

Необходимо проверить, правильно ли они расставлены.
Скобки считаются правильно расставленными, если:
    Каждая открывающая скобка имеет соответствующую закрывающую.
    Скобки закрываются в правильном порядке.

Пример данных:
({[]}): True
({[}]): False
([]{}): True
: True
{[()()]}: True
([)]: False
{[)(()]}: False
({[): False
"""

user_input = ')'

stak = []
sample = '({['

res = False


for char in user_input:
    if char in sample:
        stak.append(char)
    else:
        if not stak:
            res = False
            break

        last = stak.pop()
        if last == '[' and char == ']':
            res = True
        elif last == '{' and char == '}':
            res = True
        elif last == '(' and char == ')':
            res = True
        else:
            res = False
            break

if not user_input:
    res = True

if stak:
    res = False

print(user_input,':', res)

