""" 01. Одно слово

Напишите программу, которая
- обрабатывает список из строк
- и удаляет все строки, содержащие более одного слова,
- а также преобразует оставшиеся строки к нижнему регистру.

ВАЖНО: НЕ создать новый список, а УДАЛИТЬ лишние элементы из существующего!

Данные:
text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
Пример вывода:
Обработанный список: ['hello', 'world', 'simple']
"""


text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
# print(text_list)


for word in text_list[:]:     # удаляем длинные слова
    if " " in word:
        text_list.remove(word)

for index, word in enumerate(text_list):    # опускаем выбранные слова
    text_list[index] = word.lower()

print(text_list)
